import pandas as pd
from shapely.wkb import loads
import binascii

# Coordinates are in 25380 EPSG

def extract_coordinates(input_csv, output_csv):
    # Load the CSV file
    df = pd.read_csv(input_csv)
    
    # Convert geometry column from WKB (hex) to Shapely Point and extract coordinates
    df["geometry"] = df["geom"].apply(lambda x: loads(binascii.unhexlify(x)) if isinstance(x, str) else None)
    df["longitude"] = df["geometry"].apply(lambda g: g.x if g else None)
    df["latitude"] = df["geometry"].apply(lambda g: g.y if g else None)
    
    # Save the updated dataframe with extracted coordinates
    df.to_csv(output_csv, index=False)
    print(f"File saved: {output_csv}")

# Example usage
input_csv = "WKB(geom point).csv"  # Replace with your input file
output_csv = "WKB(geom point)_with_coordinates.csv"  # Replace with desired output file
extract_coordinates(input_csv, output_csv)
