import pandas as pd
from shapely.wkb import loads
import binascii

def extract_coordinates(input_csv, output_csv, geom_column="geom"):
    # Load the CSV file
    df = pd.read_csv(input_csv)
    
    # Check if the specified geometry column exists
    if geom_column not in df.columns:
        raise ValueError(f"Column '{geom_column}' not found in the dataset.")
    
    # Convert geometry column from WKB (hex) to Shapely Point and extract coordinates
    df["geometry"] = df[geom_column].apply(lambda x: loads(binascii.unhexlify(x)) if isinstance(x, str) else None)
    df["longitude"] = df["geometry"].apply(lambda g: g.x if g else None)
    df["latitude"] = df["geometry"].apply(lambda g: g.y if g else None)
    
    # Save the updated dataframe with extracted coordinates
    df.to_csv(output_csv, index=False)
    print(f"File saved: {output_csv}")

# Example usage
input_csv = "WKB.csv"  # Replace with your input file
output_csv = "WKB.csv"  # Replace with desired output file
extract_coordinates(input_csv, output_csv, geom_column="geom")
