# Methodology

This document explains how data was collected, verified, and structured for the Levant Historic Railway Network database.

## Project Context

This database is part of the **Levantrain initiative**, which explores the feasibility of modern high-speed rail connecting the countries of the Levant. Understanding historic railway networks serves two critical purposes:

1. **Historical preservation** - Documenting railway heritage
2. **Infrastructure assessment** - Identifying reusable assets (rights-of-way, stations, engineering works) for modern rail development

## Data Collection

### Primary Sources
1. Historical railway timetables and company records
2. Ottoman and colonial government documents
3. Archaeological surveys and heritage assessments
4. Historical maps (Ottoman, British Mandate, French Mandate)
5. **Field surveys and GPS verification**
6. **Contemporary infrastructure assessments**

### Secondary Sources
1. Academic publications on Middle Eastern railway history
2. Railway heritage organizations
3. Local historical societies
4. Engineering studies and feasibility reports

### Verification Methods
1. Cross-referencing multiple independent sources
2. Satellite imagery analysis for abandoned routes
3. **Field verification where possible** (GPS, photography)
4. Expert consultation (historians, engineers, local experts)
5. **Current infrastructure condition assessments**

## Coordinate Accuracy

### Known Limitations
- Many coordinates are **approximate**, derived from:
  - Historical maps (georeferenced)
  - Descriptions in historical documents
  - Satellite imagery of ruins/traces
  
- Coordinates should be treated as **best estimates** pending:
  - Field GPS surveys
  - Archaeological verification
  - Engineering assessments

### Confidence Levels
We recommend future work to add a confidence rating:
- **High** - GPS surveyed or verified from detailed modern maps
- **Medium** - Cross-referenced from multiple historical sources
- **Low** - Estimated from general descriptions

## Current Infrastructure Status

### Why This Matters
For modern rail planning, knowing what infrastructure survives is as important as knowing what existed historically. We document:

1. **Station buildings** - Standing, ruins, demolished, repurposed
2. **Rights-of-way** - Clear, partially obstructed, fully developed
3. **Engineering works** - Bridges, tunnels, cuttings, embankments
4. **Legal status** - Ownership, accessibility, heritage protection
5. **Reuse potential** - Technical feasibility for modern rail

### Assessment Methodology
- Satellite imagery analysis (Google Earth, Sentinel)
- Field verification where accessible
- Comparison with historical photographs
- Local knowledge and interviews
- Heritage site documentation

## Temporal Data

### Dating Methodology
- **Opening dates**: When regular service began
- **Closing dates**: When service permanently ended
- Partial/intermittent service noted in `status` and `notes`

### Challenges
- Many stations had intermittent service during WWI and WWII
- Some stations reopened under different administrations
- Exact dates often unavailable for minor stations
- Political changes affected operations and record-keeping

## Infrastructure Reuse Analysis

### Key Questions for Modern Planning
For each historic station and route segment, we aim to document:

1. **Physical survival** - What remains?
2. **Condition** - Usable, repairable, or demolished?
3. **Right-of-way** - Is the corridor still available?
4. **Obstacles** - Buildings, roads, development blocking historic routes?
5. **Ownership** - Who controls the land/infrastructure?
6. **Heritage value** - Should it be preserved vs. redeveloped?

This information will support future engineering and feasibility studies.

## Future Improvements

### Needed Research
1. **Systematic field surveys** of all major stations and routes
2. GPS verification of all station locations
3. Photographic documentation (historic vs. current)
4. Engineering assessments of surviving infrastructure
5. Legal research on property ownership and rights-of-way
6. Integration with modern transport planning data

### Technical Enhancements
1. Add confidence ratings for all data points
2. Temporal database structure (valid-from/valid-to)
3. Multiple geometries for stations that relocated
4. Infrastructure condition database (separate from historic data)
5. Integration with GIS planning tools
6. 3D models of key infrastructure

### Integration with Levantrain Planning
This historic database will eventually integrate with:
- Modern transport demand analysis
- High-speed rail corridor studies
- Cost-benefit analysis of infrastructure reuse
- Community engagement and visualization tools

## Data Standards Alignment

We align with international standards where possible:
- Coordinates: WGS84 (EPSG:4326)
- Date formats: ISO 8601
- GeoJSON: RFC 7946
- Attribution: ODbL requirements

## Collaboration

We actively seek collaboration with:
- Railway heritage organizations
- Archaeological institutes
- Transport planning agencies
- Engineering firms
- Academic researchers
- Local communities and historians

---

**From documentation to planning** — rigorous methodology for preserving the past and enabling the future.

*Last updated: April 2026*