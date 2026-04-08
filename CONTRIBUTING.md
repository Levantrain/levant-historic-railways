# Contributing to Levant Historic Railway Network

Thank you for your interest in contributing to this project! This database is part of the **Levantrain** initiative exploring modern high-speed rail for the Middle East. By documenting historic railways, we're building the foundation for understanding how modern regional rail could work.

## How You Can Help

### Types of Contributions We Need

1. **Historical Data** - Station locations, opening/closing dates, route details
2. **Current Infrastructure Status** - Which stations still stand? Which rights-of-way are clear?
3. **Field Verification** - GPS coordinates, photographs, condition assessments
4. **Engineering Details** - Track gauge, bridges, tunnels, gradients
5. **Sources & References** - Historical maps, documents, academic papers
6. **Modern Context** - Current land use, ownership, obstacles to reuse

## How to Contribute

### Reporting Issues

Found an error or missing information? Please open an issue with:

- **Station/route name**
- **What's incorrect or missing** (location, dates, status, infrastructure condition)
- **Correct information** (if known)
- **Source/reference** for the information
- **Relevance to modern planning** (if applicable)

### Adding or Editing Data

#### Option 1: GitHub (Recommended)

1. **Fork** this repository
2. **Clone** your fork locally
3. **Edit** `data/stations.geojson` or `data/stations.csv`
4. **Add sources** to `docs/sources.md`
5. **Commit** with a clear message describing your changes
6. **Push** to your fork
7. **Submit** a Pull Request

#### Option 2: Direct Edit on GitHub

For small changes:
1. Navigate to the file you want to edit
2. Click the pencil icon (Edit)
3. Make your changes
4. Propose the changes via a pull request

### Data Standards

#### Geographic Data
- Use **WGS84** coordinate system (EPSG:4326)
- Coordinates in **decimal degrees** (e.g., 33.5138, 36.2765)
- Place coordinates at the **historic station location**
- If the historic site has been demolished, note modern coordinates if relevant

#### Dates
- Use **YYYY** format for years
- Leave `year_closed` empty if station is still operational
- For uncertain dates, add a note in the `notes` field

#### Station Status Categories
- **Active** - Currently operational railway station
- **Active - Heritage** - Operates as heritage/tourist railway
- **Active - Limited** - Limited or sporadic service
- **Partially Active** - Some infrastructure remains in use
- **Abandoned** - No longer in use, but infrastructure may remain
- **Abandoned - Intact** - Station building or infrastructure survives
- **Abandoned - Ruins** - Partial remains visible
- **Demolished** - Infrastructure completely removed
- **Damaged** - War damage or natural disaster
- **Repurposed** - Building exists but serves different function

#### Current Infrastructure Assessment
Where possible, add notes about:
- **Surviving structures** - Station buildings, platforms, warehouses
- **Right-of-way status** - Clear, partially obstructed, fully developed
- **Engineering works** - Bridges, tunnels, cuttings, embankments still present
- **Current use** - Heritage site, commercial building, residential, abandoned
- **Accessibility** - Can the site be reached? Legal status?

This information is crucial for assessing reuse potential for modern rail.

#### Station Types
- **Terminus/Major** - End of line or major junction
- **Major** - Important regional station
- **Minor** - Small local station
- **Junction** - Meeting point of multiple lines
- **Border Station** - International crossing point
- **Water Station** - Primarily for water supply

#### Naming Conventions
- Use commonly recognized **English transliterations**
- Include **Arabic script** in `name_arabic` field
- For stations with multiple historical names, use the most common and note alternatives in `notes`

### Source Requirements

All data additions must include sources. Add references to `docs/sources.md` using this format:

Start with two hash marks, then the station name in square brackets, followed by your source details with asterisks for bullet points, including description of source, full citation, URL if available, archive reference if applicable, and date verified for field observations.

Acceptable sources include:
- Historical maps and railway timetables
- Academic publications
- Government archives
- Archaeological and heritage surveys
- Satellite imagery (for verification)
- Field surveys with GPS coordinates
- Contemporary photographs
- Engineering assessments

### Quality Guidelines

#### Before Submitting
- [ ] Coordinates verified against satellite imagery or GPS
- [ ] Dates cross-referenced with multiple sources
- [ ] Current condition noted (if known)
- [ ] Arabic transliterations checked
- [ ] Sources added to `docs/sources.md`
- [ ] GeoJSON syntax is valid (use geojson.io to verify)

#### Pull Request Checklist
- Clear description of what was added/changed
- Reasoning for the changes
- Source citations included
- Relevance to modern planning noted (if applicable)
- One logical change per PR (easier to review)

### Code of Conduct

This is a collaborative project focused on infrastructure and regional connectivity. We expect:

- **Respectful** communication
- **Evidence-based** contributions
- **Good faith** engagement with differing interpretations
- **Attribution** of sources and other contributors' work
- **Focus on infrastructure**, not politics

Our goal is to explore how modern rail could serve all communities in the region. Political or ethnic disputes should be set aside in favor of accurate technical documentation.

### Questions?

- Open a **GitHub Discussion** for general questions
- Open an **Issue** for specific data questions
- Visit levantrain.net to learn more about the broader initiative

## Development Setup (Optional)

For contributors working with validation scripts:

Clone the repository, install Python dependencies if needed for validation, and run the validation script to check GeoJSON files.

## Special Contribution Opportunities

### Field Verification Needed
We especially need contributors who can:
- Visit historic station sites and document current condition
- Take GPS readings and photographs
- Assess right-of-way status
- Document surviving bridges, tunnels, and engineering works
- Interview local communities about railway heritage

### Engineering Analysis Needed
Engineers and planners can contribute:
- Assessment of reusable infrastructure
- Analysis of grades, curves, and alignment
- Bridge and tunnel condition reports
- Right-of-way availability analysis

---

Thank you for helping document the past to enable the future of regional rail!

Part of the Levantrain initiative