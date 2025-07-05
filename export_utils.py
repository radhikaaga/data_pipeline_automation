# export_utils.py

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import fastavro
import os

def export_collection(db, collection_name, output_dir="exports/"):
    os.makedirs(output_dir, exist_ok=True)

    data = list(db[collection_name].find())

    if not data:
        print(f"[!] No data in collection: {collection_name}")
        return

    df = pd.DataFrame(data)
    df.drop(columns=["_id"], inplace=True, errors="ignore")

    # CSV
    df.to_csv(f"{output_dir}{collection_name}.csv", index=False)

    # Parquet
    table = pa.Table.from_pandas(df)
    pq.write_table(table, f"{output_dir}{collection_name}.parquet")

    # Avro
    schema = {
        "type": "record",
        "name": "Row",
        "fields": [{"name": col, "type": "string"} for col in df.columns]
    }

    with open(f"{output_dir}{collection_name}.avro", "wb") as out:
        records = df.astype(str).to_dict(orient="records")
        fastavro.writer(out, schema, records)

    print(f"[✓] Exported: {collection_name} → CSV, Parquet, Avro")
