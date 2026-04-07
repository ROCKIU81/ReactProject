from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Описываем, какие переменные мы ждем
    DBNAME: str
    USER: str
    PASSWORD: str
    PORT: int  # Он сам превратит строку "5432" в число!
    HOST: str

    # Указываем, где искать файл (относительно запуска)
    model_config = SettingsConfigDict(env_file="app/.env")

# Создаем один экземпляр настроек
config = Settings()