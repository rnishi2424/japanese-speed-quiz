FROM python:3.14.2

WORKDIR /app

# copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# expose FastAPI port
EXPOSE 8000

# run server locally
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]