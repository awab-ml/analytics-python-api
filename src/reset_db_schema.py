
import timescaledb
from sqlmodel import SQLModel, create_engine, text
from api.events.models import EventModel
from api.db.config import DB_TIMEZONE

# Override with localhost connection string for running outside docker
DATABASE_URL = "postgresql+psycopg://time-user:time-password@localhost:5432/timescaledb"

# Use timescaledb wrapper if possible, or standard engine
try:
    engine = timescaledb.create_engine(DATABASE_URL, timezone=DB_TIMEZONE)
except Exception:
    engine = create_engine(DATABASE_URL)

def reset_table():
    print("Dropping EventModel table...")
    try:
        EventModel.__table__.drop(engine)
        print("Dropped table 'eventmodel'.")
    except Exception as e:
        print(f"Error dropping table: {e}")
        pass

    print("Re-creating tables...")
    SQLModel.metadata.create_all(engine)
    
    print("Creating hypertables...")
    try:
        timescaledb.metadata.create_all(engine)
    except Exception as e:
         print(f"Warning: Timescale metadata creation failed (maybe already hypertable?): {e}")

    print("Done.")

if __name__ == "__main__":
    reset_table()
