# japanese-speed-quiz
simple app to rapidly quiz yourself on Japanese vocabulary

## Setup
1. Python 3.14 recommended
2. Create virtual environment
3. Run pip install -r requirements.txt
4. Add .env file (Check .env.template for an example of variables you need)
5. Backend: cd to /backend/api directory and run: uvicorn main:app --reload

Optional (setup PostgreSQL to test on local database)
1. Install [postgresql](https://www.postgresql.org/)
2. Rewrite .env DB variables to reflect your local databases credentials
3. Run schema.sql commands to create tables
4. Run vocab_ETL.py script to populate the Vocab dataset with data
