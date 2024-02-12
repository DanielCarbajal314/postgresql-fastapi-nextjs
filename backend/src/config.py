from os import environ
from pydantic import BaseModel


class DatabaseSettings(BaseModel):
    port: int
    name: str
    user: str
    password: str
    server: str


class ConfigurationVariables(BaseModel):
    database: DatabaseSettings


configuration = ConfigurationVariables(
    database=DatabaseSettings(
        port=int(environ["POSTGRES_PORT"]),
        name=environ["POSTGRES_DB"],
        user=environ["POSTGRES_USER"],
        password=environ["POSTGRES_PASSWORD"],
        server=environ["POSTGRES_SERVER"],
    )
)
