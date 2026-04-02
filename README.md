# japanese-speed-quiz
Simple app to rapidly quiz yourself on Japanese vocabulary. The focus of this app is to increase reading and vocabulary recognition speed rather than learning definitions.

## Setup
### Backend
1. python 3.14 recommended
2. navigate to root directory
3. pip install -r requirements.txt
4. add .env file (Check .env.template for an example of variables you need)
5. cd /backend/api
6. uvicorn main:app --reload

### Frontend
More detailed instructions can be found in the frontend README.md
1. cd /frontend
2. npm install
3. npm run dev

### Optional (local database for PostgreSQL)
1. Install [postgresql](https://www.postgresql.org/)
2. Rewrite .env DB variables to reflect your local databases credentials
3. Run schema.sql commands to create tables
4. Run vocab_ETL.py script to populate the Vocab dataset with data
