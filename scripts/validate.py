#!/usr/bin/env python3
"""Validate the Levant Historic Railway dataset. Standard library only.

Checks GeoJSON validity, coordinate ranges, controlled vocabularies, provenance
integrity (every cited source exists), uniqueness, and snapshot counts.

Usage:  python3 scripts/validate.py     # exits non-zero if any errors
"""
import json, pathlib, sys, glob

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors, warnings = [], []
def err(m): errors.append(m)
def warn(m): warnings.append(m)

def load(rel):
    try:
        return json.loads((ROOT / rel).read_text())
    except Exception as e:
        err(f"{rel}: cannot parse ({e})")
        return None

PRECISION = {"exact", "approx", "town", "unknown"}
GEOM_STATUS = {"surveyed", "partial", "schematic", "none"}
# Levant/Middle East bounding box (generous).
LON, LAT = (24.0, 52.0), (12.0, 43.0)

sources = load("data/sources.json") or []
source_ids = {s.get("id") for s in sources}
if not source_ids:
    err("data/sources.json: no sources found")

def check_source_ids(ids, where):
    for sid in ids or []:
        if sid not in source_ids:
            err(f"{where}: unknown source_id '{sid}'")

# --- stations ---
stations = load("data/stations/historic/stations.geojson")
station_count = 0
seen_ids = set()
if stations:
    for i, f in enumerate(stations.get("features", [])):
        station_count += 1
        p = f.get("properties", {})
        sid = p.get("station_id")
        where = f"stations[{sid or i}]"
        if not sid:
            err(f"{where}: missing station_id")
        elif sid in seen_ids:
            err(f"{where}: duplicate station_id")
        else:
            seen_ids.add(sid)
        g = f.get("geometry") or {}
        if g.get("type") != "Point":
            err(f"{where}: geometry is not a Point")
        else:
            lon, lat = (g.get("coordinates") or [None, None])[:2]
            if lon is None or lat is None:
                err(f"{where}: missing coordinates")
            elif not (LON[0] <= lon <= LON[1] and LAT[0] <= lat <= LAT[1]):
                warn(f"{where}: coordinates {lon},{lat} outside the expected region")
        if p.get("precision") and p["precision"] not in PRECISION:
            err(f"{where}: invalid precision '{p['precision']}'")
        check_source_ids(p.get("source_ids"), where)

# --- routes ---
route_count = seg_count = 0
for path in sorted(glob.glob(str(ROOT / "data/routes/**/*.geojson"), recursive=True)):
    rel = pathlib.Path(path).relative_to(ROOT)
    gj = load(str(rel))
    if not gj:
        continue
    route_count += 1
    meta = gj.get("route", {})
    check_source_ids(meta.get("source_ids"), f"{rel}:route")
    for j, f in enumerate(gj.get("features", [])):
        seg_count += 1
        p = f.get("properties", {})
        where = f"{rel}[{p.get('sequence', j)}]"
        g = f.get("geometry") or {}
        if g.get("type") != "LineString" or len(g.get("coordinates", [])) < 2:
            err(f"{where}: segment is not a valid LineString")
        if p.get("geometry_status") and p["geometry_status"] not in GEOM_STATUS:
            err(f"{where}: invalid geometry_status '{p['geometry_status']}'")
        check_source_ids(p.get("source_ids"), where)

# --- infrastructure ---
infra = load("data/infrastructure/historic.geojson")
infra_count = len(infra.get("features", [])) if infra else 0
if infra:
    for i, f in enumerate(infra["features"]):
        check_source_ids((f.get("properties") or {}).get("source_ids"), f"infrastructure[{i}]")

# --- source_links ---
links = load("data/source_links.json") or []
for i, l in enumerate(links):
    if l.get("source_id") not in source_ids:
        err(f"source_links[{i}]: unknown source_id '{l.get('source_id')}'")

# --- snapshot counts ---
snap = load("data/snapshot.json") or {}
for key, actual in [("stations", station_count), ("routes", route_count),
                    ("segments", seg_count), ("infrastructure", infra_count),
                    ("sources", len(sources)), ("source_links", len(links))]:
    if key in snap and snap[key] != actual:
        err(f"snapshot.json {key}={snap[key]} but found {actual}")

# --- report ---
print(f"stations={station_count} routes={route_count} segments={seg_count} "
      f"infrastructure={infra_count} sources={len(sources)} source_links={len(links)}")
for w in warnings:
    print(f"WARN  {w}")
if errors:
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1)
print(f"OK — valid ({len(warnings)} warning(s))")
