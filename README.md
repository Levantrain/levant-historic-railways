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

The database includes historic railway infrastructure across Turkey, Syria, Lebanon, Jordan, Israel/Palestine, Saudi Arabia, and Egypt at its maximum historical extent:

- **Historic railway stations** with precise geolocation data
- **Railway routes** connecting these stations
- **Metadata** including years of operation, current status, gauge, and condition
- **Multiple railway systems**: Hejaz Railway, Baghdad Railway, Taurus Express, Palestine Railways, Egyptian State Railways, and more

## Interactive Map

Explore the historic network on our interactive map: [uMap Viewer](https://umap.openstreetmap.fr/) *(link to be added)*

## Data

All data is provided in open, standard formats:

- **GeoJSON** - `data/stations.geojson` - Geographic data for all stations
- **CSV** - `data/stations.csv` - Tabular format for easy editing
- **Route Geometries** - `data/routes.geojson` - Railway line geometries (coming soon)

### Data Fields

Each station includes:
- `name` - Station name (English/transliterated)
- `name_arabic` - Station name in Arabic script
- `latitude` / `longitude` - Geographic coordinates (WGS84)
- `year_opened` - Year the station opened
- `year_closed` - Year the station closed (if applicable)
- `current_status` - Active, Abandoned, Damaged, Partially Active, etc.
- `station_type` - Major, Minor, Terminus, Junction, etc.
- `country` - Current country
- `gauge_mm` - Track gauge in millimeters
- `historic_routes` - Which railway lines served this station
- `notes` - Additional historical context and current condition

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