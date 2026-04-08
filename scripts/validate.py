#!/usr/bin/env python3
"""
Validate GeoJSON files for the Levant Historic Railway Network project.

This script checks for:
- Valid GeoJSON syntax
- Required properties for each station
- Coordinate validity (within reasonable bounds for the region)
- Data type consistency
- Missing recommended fields

Part of the Levantrain initiative.
"""

import json
import sys
from pathlib import Path
from typing import List, Tuple


def validate_geojson(filepath: Path) -> Tuple[List[str], List[str]]:
    """
    Validate a GeoJSON file.
    
    Returns:
        Tuple of (errors, warnings) where each is a list of strings
    """
    errors = []
    warnings = []
    
    # Load file
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [f"Invalid JSON: {e}"], []
    except FileNotFoundError:
        return [f"File not found: {filepath}"], []
    
    # Check if it's a FeatureCollection
    if data.get('type') != 'FeatureCollection':
        errors.append("Must be a FeatureCollection")
        return errors, warnings
    
    # Check features exist
    if 'features' not in data:
        errors.append("No 'features' array found")
        return errors, warnings
    
    # Define required and recommended properties
    required_props = [
        'name', 
        'country', 
        'year_opened', 
        'status', 
        'station_type', 
        'gauge_mm', 
        'historic_routes'
    ]
    recommended_props = ['name_arabic', 'notes']
    
    # Valid status values
    valid_statuses = [
        'Active',
        'Active - Heritage',
        'Active - Limited',
        'Partially Active',
        'Abandoned',
        'Abandoned - Intact',
        'Abandoned - Ruins',
        'Demolished',
        'Damaged',
        'Repurposed'
    ]
    
    # Validate each feature
    for i, feature in enumerate(data['features']):
        feature_num = i + 1
        
        # Check geometry
        if 'geometry' not in feature:
            errors.append(f"Feature {feature_num}: Missing geometry")
            continue
            
        geom = feature['geometry']
        if geom['type'] != 'Point':
            errors.append(f"Feature {feature_num}: Geometry must be Point, not {geom['type']}")
        
        # Check coordinates
        if 'coordinates' not in geom or len(geom['coordinates']) != 2:
            errors.append(f"Feature {feature_num}: Invalid coordinates")
        else:
            lon, lat = geom['coordinates']
            
            # Regional bounds check (Levant region approximate)
            if not (24 <= lat <= 42):
                warnings.append(
                    f"Feature {feature_num}: Latitude {lat:.4f} outside expected "
                    f"range (24-42°N)"
                )
            if not (29 <= lon <= 43):
                warnings.append(
                    f"Feature {feature_num}: Longitude {lon:.4f} outside expected "
                    f"range (29-43°E)"
                )
        
        # Check properties
        if 'properties' not in feature:
            errors.append(f"Feature {feature_num}: Missing properties")
            continue
        
        props = feature['properties']
        station_name = props.get('name', f'unnamed-{feature_num}')
        
        # Check required properties
        for prop in required_props:
            if prop not in props or props[prop] is None or props[prop] == '':
                errors.append(
                    f"Feature {feature_num} ({station_name}): "
                    f"Missing required property '{prop}'"
                )
        
        # Check recommended properties
        for prop in recommended_props:
            if prop not in props or not props[prop]:
                warnings.append(
                    f"Feature {feature_num} ({station_name}): "
                    f"Missing recommended property '{prop}'"
                )
        
        # Validate year_opened
        if 'year_opened' in props and props['year_opened']:
            try:
                year = int(props['year_opened'])
                if not (1850 <= year <= 2030):
                    warnings.append(
                        f"Feature {feature_num} ({station_name}): "
                        f"year_opened {year} seems unusual (expected 1850-2030)"
                    )
            except (ValueError, TypeError):
                errors.append(
                    f"Feature {feature_num} ({station_name}): "
                    f"year_opened must be a number"
                )
        
        # Validate year_closed (if present)
        if 'year_closed' in props and props['year_closed']:
            try:
                year_closed = int(props['year_closed'])
                if 'year_opened' in props and props['year_opened']:
                    year_opened = int(props['year_opened'])
                    if year_closed < year_opened:
                        errors.append(
                            f"Feature {feature_num} ({station_name}): "
                            f"year_closed ({year_closed}) before year_opened ({year_opened})"
                        )
            except (ValueError, TypeError):
                errors.append(
                    f"Feature {feature_num} ({station_name}): "
                    f"year_closed must be a number"
                )
        
        # Validate status
        if 'status' in props and props['status']:
            if props['status'] not in valid_statuses:
                warnings.append(
                    f"Feature {feature_num} ({station_name}): "
                    f"status '{props['status']}' not in standard list. "
                    f"Valid values: {', '.join(valid_statuses)}"
                )
        
        # Validate gauge_mm
        if 'gauge_mm' in props and props['gauge_mm']:
            try:
                gauge = int(props['gauge_mm'])
                # Common gauges in the region: 610, 1000, 1050, 1435
                if gauge not in [610, 1000, 1050, 1435]:
                    warnings.append(
                        f"Feature {feature_num} ({station_name}): "
                        f"gauge_mm {gauge} is unusual (common: 610, 1000, 1050, 1435)"
                    )
            except (ValueError, TypeError):
                errors.append(
                    f"Feature {feature_num} ({station_name}): "
                    f"gauge_mm must be a number"
                )
    
    return errors, warnings


def main():
    """Main validation function."""
    stations_file = Path('data/stations.geojson')
    
    print("=" * 70)
    print("Levant Historic Railway Network - Data Validation")
    print("Part of the Levantrain initiative")
    print("=" * 70)
    print(f"\nChecking: {stations_file}")
    print("-" * 70)
    
    if not stations_file.exists():
        print(f"\n❌ ERROR: File not found: {stations_file}")
        print("\nMake sure you're running this from the repository root directory.")
        return 1
    
    errors, warnings = validate_geojson(stations_file)
    
    # Count features
    try:
        with open(stations_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            feature_count = len(data.get('features', []))
            print(f"\nTotal stations: {feature_count}")
    except:
        feature_count = 0
    
    # Print results
    if errors:
        print(f"\n❌ ERRORS ({len(errors)}):")
        for error in errors:
            print(f"  • {error}")
    
    if warnings:
        print(f"\n⚠️  WARNINGS ({len(warnings)}):")
        for warning in warnings:
            print(f"  • {warning}")
    
    # Summary
    print("\n" + "=" * 70)
    if not errors and not warnings:
        print("✅ Perfect! All validation checks passed!")
        print("=" * 70)
        return 0
    elif not errors:
        print(f"✅ No errors found ({len(warnings)} warnings)")
        print("=" * 70)
        print("\nWarnings are suggestions for improvement, not blocking issues.")
        return 0
    else:
        print(f"❌ Validation failed: {len(errors)} errors, {len(warnings)} warnings")
        print("=" * 70)
        print("\nPlease fix the errors above before committing.")
        return 1


if __name__ == '__main__':
    sys.exit(main())