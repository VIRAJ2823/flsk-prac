from sqlalchemy import create_engine ,Interger ,String ,Float ,column
from sqlalchemy.orm import declarative_base , sessionmaker , relationship

engine = create_engine('sqlite:///mydatabase.db', echo = True)