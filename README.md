# japanese-speed-quiz
Simple app to rapidly quiz yourself on Japanese vocabulary. The focus of this app is to increase reading and vocabulary recognition speed rather than learning definitions.

## Setup
### Docker
- Install [docker](https://www.docker.com/)
- to build/run the containers: docker-compose up
- to stop the containers: docker-compose down

### Backend
- python 3.14 recommended
- add .env file to project root directory (Check .env.template for an example of variables you need)
- navigate to backend directory
- pip install -r requirements.txt
- uvicorn app.main:app --reload

### Frontend
More detailed instructions can be found in the frontend README.md
- cd /frontend
- npm install
- npm run dev

### Optional (local database for PostgreSQL)
- Install [postgresql](https://www.postgresql.org/)
- Rewrite .env DB variables to reflect your local databases credentials
- Run schema.sql commands to create tables
- Run vocab_ETL.py script to populate the Vocab table with data
