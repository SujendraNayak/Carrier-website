import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from urllib.parse import quote_plus

# ✅ Load environment variables
load_dotenv()

# ✅ Read DB credentials
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))  # safely encode special chars like @
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")

# ✅ Create SQLAlchemy engine
engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    pool_pre_ping=True  # auto reconnect if connection drops
)

# ✅ Helper function (optional)
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        return [dict(row._mapping) for row in result.all()]
