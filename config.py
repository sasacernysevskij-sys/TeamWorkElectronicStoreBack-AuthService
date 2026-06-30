import os

SECRET_KEY = os.getenv("SECRET_KEY", "auth-secret-key-123")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///auth.db")
JWT_EXPIRATION_HOURS = 24