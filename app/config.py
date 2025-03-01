from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: int = 5432
    database_password: str = "admin"
    database_name: str = "fastapi"
    database_username: str = "postgres"
    secret_key: str = "THIS IS A LONG LONG LONG SECKET KEY"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

# for some reason doesn't work!
# class Settings(BaseSettings):
#     database_hostname: str
#     database_port: int
#     database_password: str
#     database_name: str 
#     database_username: str
#     secret_key: str
#     algorithm: str
#     access_token_expire_minutes: int

#     model_config = SettingsConfigDict(env_file='.env')


settings = Settings()