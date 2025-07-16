DB_USER = "root"
DB_PASSWORD = "juseondo"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "todo_db"
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
)