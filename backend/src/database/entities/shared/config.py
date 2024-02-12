from src.config import configuration

db = configuration.database
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{db.user}:{db.password}@{db.server}:{db.port}/{db.name}"
)
