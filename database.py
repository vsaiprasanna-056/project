from sqlalchemy import create_engine
#to create connection with database
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/products_db"
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_okX1RFsckRw31m5aeyz@mysqldb-saiprasannav999-dcd7.e.aivencloud.com:16816/defaultdb"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "ssl":{}
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

