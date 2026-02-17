# JLPT Vocabulary Ingestion

Source: [JLPT vocabulary](https://www.kaggle.com/datasets/robinpourtaud/jlpt-words-by-level)
Format: CSV
Rows: ~8000

Steps:
1. Normalize fields
2. Insert into vocabulary table
3. Skip duplicates by (word, reading, level)