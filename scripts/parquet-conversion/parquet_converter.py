import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

INPUT_FILE = "postgres_archive.csv"
OUTPUT_FILE = "postgres_archive.parquet"

print("Loading CSV archive")

dataframe = pd.read_csv(INPUT_FILE)

table = pa.Table.from_pandas(dataframe)

pq.write_table(
    table,
    OUTPUT_FILE,
    compression="snappy"
)

print(f"Parquet archive created: {OUTPUT_FILE}")
