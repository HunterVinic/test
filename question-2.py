from celery import Celery
import requests
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.exc import SQLAlchemyError


app = Celery('tasks', broker='redis://localhost:6379/0')

DATABASE_URI = "sqlite:///data.db"
engine = create_engine(DATABASE_URI)
metadata = MetaData()

data_table = Table(
    'data_table', metadata,
    Column('id', Integer, primary_key=True),
    Column('value', String, nullable=False)
)
metadata.create_all(engine)

@app.task(bind=True, max_retries=3)
def fetch_and_store_data(self, api_url):
    """
    Fetches data from a REST API, processes it, and stores it in a database.
    """
    try:
        # Fetch data
        print(f"Fetching data from {api_url}...")
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"Data fetched successfully: {len(data)} records.")

        # Store data in the database
        with engine.connect() as conn:
            for item in data:
                try:
                    conn.execute(data_table.insert().values(id=item['id'], value=item['value']))
                    print(f"Inserted record with ID {item['id']}.")
                except SQLAlchemyError as db_err:
                    print(f"Database error for record {item['id']}: {str(db_err)}")
    except requests.RequestException as exc:
        print(f"Request error: {str(exc)}")
        raise self.retry(exc=exc)

if __name__ == "__main__":
    fetch_and_store_data.delay("https://api.example.com/data")
