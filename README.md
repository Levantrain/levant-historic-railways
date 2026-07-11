# Levant Historic Railway Network

[![Levantrain](https://img.shields.io/badge/Project-Levantrain-blue)](https://levantrain.net)
[![License: ODbL](https://img.shields.io/badge/License-ODbL-brightgreen.svg)](https://opendatacommons.org/licenses/odbl/)

An open-source database of historic railway stations and routes in the Levant region.

**Part of the [Levantrain](https://levantrain.net) initiative** — a community exploration into high-speed rail linking the countries of the Levant (Syria, Lebanon, Jordan, Israel, and Palestine) and their neighbors.

## About Levantrain

Levantrain explores connectivity, peace, and shared prosperity in the Middle East through modern high-speed rail infrastructure. We're investigating whether and how a modern railway system (high-speed passenger rail, freight networks, green energy-powered) could be built across the region — and at what cost.

**Understanding the past is essential to planning the future.** This database documents the historic railway networks that once connected the Levant, cataloging stations, routes, and infrastructure that may still exist today. Historic rights-of-way, railway stations, bridges, and tunnels could prove invaluable for modern rail development.

Learn more at [levantrain.net](https://levantrain.net).

## Why This Database Matters

This historical documentation serves multiple purposes:

1. **Infrastructure Assessment** - Identify existing rights-of-way, station locations, and engineering works that could be reused
2. **Route Planning** - Understand historical corridors and successful/unsuccessful routes
3. **Cost Analysis** - Learn from past construction challenges and solutions
4. **Heritage Preservation** - Document and protect important railway heritage sites
5. **Community Engagement** - Connect people to the region's railway history and future potential

## Overview

The database spans historic railway infrastructure across Turkey, Syria, Lebanon, Jordan, Israel/Palestine, Saudi Arabia, and Egypt at its maximum historical extent. This snapshot (**2026-07-11**) contains **21 routes · 218 stations · 217 segments · 7 bridges/tunnels**, every fact cited to one of **37 sources** (~1,460 citations). Station coordinates were verified against public gazetteers — **194 of 218 now carry a sourced, verified coordinate**:

- **Historic railway stations** with geolocation and a stated location **precision**
- **Railway routes** as ordered, per-segment geometries carrying **confidence** and geometry provenance
- **Full provenance** — every feature cites its sources; **105 segments carry real OpenStreetMap track geometry**
- **Multiple railway systems**: Hejaz Railway, Baghdad Railway, Taurus Express, Palestine Railways, Egyptian State Railways, and more

## Interactive map

Explore the network on the Levantrain map: **[levantrain.net/map](https://levantrain.net/map)**.

## Data

This repository is a **point-in-time snapshot (2026-07-11)** generated from the Levantrain database
(the live single source of truth). It is provided in open, standard formats:

| Path | Contents |
| --- | --- |
| `data/stations/historic/stations.geojson` | 218 stations (Point features) |
| `data/routes/historic/*.geojson` | 21 routes, one file each — a Feature per **segment** (LineString) plus route metadata under a top-level `route` object |
| `data/infrastructure/historic.geojson` | 7 historic bridges/tunnels (Point features) |
| `data/sources.json` | The 37 sources every fact is cited to |
| `data/source_links.json` | 1,462 attribute-level citations (which source backs which field of which feature) |
| `data/snapshot.json` | Snapshot metadata (date + counts) |

Every feature carries a `source_ids` array referencing `data/sources.json`, so provenance travels with
the data. For finer, per-attribute provenance (e.g. *which* source backs a station's gauge vs. its
coordinates), see `data/source_links.json`.

**105 of 217 route segments carry real surveyed track geometry** recovered from OpenStreetMap; the rest
are best-guess corridors — see each segment's `geometry_status` and `corridor_confidence`.

### Station fields

- `station_id` — stable slug identifier
- `name` / `name_arabic` / `name_he` — names
- `latitude` / `longitude` — WGS84 (in the GeoJSON geometry)
- `country`, `role`, `elevation_m`
- `precision` — how well the location is known: `exact` / `approx` / `town` / `unknown`
- `confidence` — overall confidence in the record: `high` / `medium` / `low`
- `year_opened` / `year_closed`, `gauge_mm`, `status`, `historic_routes`
- `source_ids` — citations (→ `data/sources.json`)

### Route & segment fields

Route metadata (`route` object): `route_id`, `name`, `name_arabic`, `countries`, `gauge_mm`,
`year_opened`/`year_closed`, `era`, `route_type`, `status`, `corridor_confidence`, `description`,
`history`, `notes`, `source_ids`. Each segment Feature: `sequence`, `from`/`to` (+ `_id`),
`geometry_status` (`surveyed` / `partial` / `schematic`), `geometry_source`, `corridor_confidence`,
`connection_status`, `source_ids`.

### Attribution

Track geometry for surveyed segments is derived from **© OpenStreetMap contributors**
([ODbL](https://www.openstreetmap.org/copyright)). This database is released under the ODbL (see below),
which keeps that geometry properly share-alike.

## Contributing

We welcome contributions from historians, railway enthusiasts, engineers, urban planners, researchers, and local experts! See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Quick Start

1. **Found an error?** Open an [issue](../../issues)
2. **Want to add data?** Fork the repo, edit the files, and submit a pull request
3. **Know about surviving infrastructure?** Add details about current condition
4. **Have sources?** Add them to `docs/sources.md`

## Historic Railway Networks Included

- **Hejaz Railway** (1908-1918) - Damascus to Medina
- **Baghdad Railway** (1903-1940) - Istanbul to Baghdad (Levant portion)
- **Taurus Express** - Luxury service on Baghdad Railway route
- **Jaffa-Jerusalem Railway** (1892-present)
- **Palestine Railways** - British Mandate era network
- **Egyptian State Railways** - Eastern lines connecting to the Levant
- **Beirut-Damascus Railway** (1895-present)
- **Tripoli-Homs Railway**
- **Jezreel Valley Railway**
- **Haifa-Deraa Line**

## Project Goals

### Immediate (Historic Documentation)
1. **Document** all historic railway infrastructure at maximum extent
2. **Map** surviving infrastructure: rights-of-way, stations, bridges, tunnels
3. **Assess** current condition and ownership status
4. **Preserve** knowledge of abandoned and damaged railways

### Long-term (Future Planning)
1. **Identify** reusable infrastructure for modern rail development
2. **Analyze** historic route corridors for high-speed rail feasibility
3. **Support** engineering studies and feasibility assessments
4. **Enable** community discussion about regional rail connectivity

## Data Quality

This is an ongoing research project. Coordinates are approximate and should be verified against:
- Historical maps and documents
- Satellite imagery
- Field surveys
- Current infrastructure assessments
- Academic sources

We especially welcome contributions about **current infrastructure status** — which station buildings survive, which rights-of-way are still clear, which bridges and tunnels remain usable.

## License

- **Data**: Open Database License (ODbL) - see [LICENSE-DATA.md](LICENSE-DATA.md)
- **Code/Scripts**: MIT License - see [LICENSE-CODE.md](LICENSE-CODE.md)

## Contact

- **Levantrain Website**: [levantrain.net](https://levantrain.net)
- **GitHub Organization**: [@levantrain](https://github.com/levantrain)
- **Issues**: Use the [issue tracker](https://github.com/levantrain/levant-historic-railways/issues)
- **Discussions**: Use [GitHub Discussions](https://github.com/levantrain/levant-historic-railways/discussions)

## Acknowledgments

This project builds on the work of railway historians, archivists, engineers, and preservationists across the Middle East. We are grateful to all contributors and sources documented in `docs/sources.md`.

## Roadmap

### Phase 1: Historic Documentation (Current)
- [x] Initial station database (Hejaz, Baghdad, Palestine railways)
- [ ] Complete route geometries (line strings)
- [ ] Document surviving infrastructure and current condition
- [ ] Field verification of key sites

### Phase 2: Modern Assessment (Future)
- [ ] Survey of reusable rights-of-way
- [ ] Engineering assessment of surviving infrastructure
- [ ] Integration with modern transport planning data
- [ ] Cost-benefit analysis for infrastructure reuse

### Phase 3: Future Planning Support (Future)
- [ ] High-speed rail corridor analysis
- [ ] Integration with Levantrain feasibility studies
- [ ] Community engagement tools
- [ ] API for transport planning applications

---

**From the past to the future** — documenting historic railways to enable modern regional connectivity.

*Part of the Levantrain initiative • Last updated: April 2026*