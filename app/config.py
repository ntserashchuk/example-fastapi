from pydantic_settings import BaseSettings, SettingsConfigDict

# class Settings(BaseSettings):
#     database_hostname: str = "localhost"
#     database_port: int = 5432
#     database_password: str = "admin"
#     database_name: str = "fastapi"
#     database_username: str = "postgres"
#     secret_key: str = "THIS IS A LONG LONG LONG SECKET KEY"
#     algorithm: str = "HS256"
#     access_token_expire_minutes: int = 30

class Settings(BaseSettings):
    database_hostname: str = "cd27da2sn4hj7h.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com"
    database_port: int = 5432
    database_password: str = "p101c97d74ddcd8a9a2c5602dd712060483e4189bdcccbfc8e202eac99aaaf4ca"
    database_name: str = "d371hkmnrk7qpj"
    database_username: str = "ufrtmg8atbr6fk"
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