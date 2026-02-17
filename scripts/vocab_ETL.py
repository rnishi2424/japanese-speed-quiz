from pathlib import Path
import logging
import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch
from dotenv import load_dotenv
import os

# Configuation
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

DATASET_PATH = DATA_DIR / "jlpt_vocab.csv"
LOG_LEVEL = logging.INFO

# Logging
def setup_logging() -> None:
    logging.basicConfig(
        level=LOG_LEVEL,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

# Dataset
def load_dataset(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found at: {path}")
    
    logging.info("Loading dataset from %s", path)

    df = pd.read_csv(path)

    logging.info("Dataset loaded with %d rows and %d columns", df.shape[0], df.shape[1])
    return df

# Transformation/Validation
def clean_string(value: str | None) -> str | None:
    if value is None:
        return None
    if isinstance(value, float) and pd.isna(value):
        return None
    
    return value.strip()

def normalize_jlpt(jlpt_raw: str | int | None) -> int | None:
    """
    Conhverts JLPT values like 'N5' or '5' or 5 into integers.
    """
    if jlpt_raw is None:
        return None
    if isinstance(jlpt_raw, int):
        return jlpt_raw
    
    jlpt_raw = jlpt_raw.strip().upper()

    if jlpt_raw.startswith("N"):
        return int(jlpt_raw[1:])
    
    return int(jlpt_raw)

def split_meanings(meaning_raw: str | None) -> list[str]:
    """
    splits the definitions into a list of definitions (if there are multiple)
    """
    if not meaning_raw:
        return []
    
    return [
        m.strip().lower()
        for m in meaning_raw.split(";")
        if m.strip()
    ]

def clean_vocab_row(row: dict) -> dict:
    try:
        return {
            "kanji": clean_string(row.get("Original")),
            "furigana": clean_string(row.get("Furigana")),
            "jlpt_level": normalize_jlpt(row.get("JLPT Level")),
            "english": split_meanings(row.get("English"))
        }
    except Exception:
        logging.error("Failed to clean row: %s", row, exc_info=True)
        raise

def clean_vocab_dataframe(df: pd.DataFrame) -> list[dict]:
    records = df.to_dict(orient="records")
    return [clean_vocab_row(r) for r in records]

def chunked(iterable: list, size: int):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


# Database Insertion
def get_connection():
    return psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER', 'localhost'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )



def insert_vocab_batch(conn, records: list[dict]) -> None:
    sql = """
        INSERT INTO vocabulary (kanji, furigana, jlpt_level, english)
        VALUES (%(kanji)s, %(furigana)s, %(jlpt_level)s, %(english)s)
        ON CONFLICT (kanji, furigana) DO NOTHING
    """

    with conn.cursor() as cur:
        execute_batch(cur, sql, records, page_size=500)

    conn.commit()

def insert_vocab(conn, records: list[dict], batch_size: int = 500):
    for batch in chunked(records, batch_size):
        insert_vocab_batch(conn, batch)


# Main
def main () -> None:
    setup_logging()

    logging.info("Starting JLPT vocabulary ingestion")

    raw_df = load_dataset(DATASET_PATH)

    # check sample data
    # logging.info("Dataset preview:\n%s", raw_df.head())

    logging.info("Ingestion script completed (no transformations yet)")

    # check for bad rows
    bad_rows = raw_df[raw_df.isna().any(axis=1)]
    logging.info("Rows with missing values: %d", len(bad_rows))
    logging.debug("Sample bad row: %s", bad_rows.iloc[0].to_dict())

    clean_records = clean_vocab_dataframe(raw_df)

    # check sample cleaned data
    logging.info("Clean records ready for DB insert: %d", len(clean_records))
    logging.debug("Sample clean record: %s", clean_records[0])

    load_dotenv()

    conn = get_connection()
    insert_vocab(conn, clean_records)
    conn.close()

    logging.info("ETL completed successfully")

if __name__ == "__main__":
    main()