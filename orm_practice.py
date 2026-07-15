from sqlalchemy import create_engine , Integer, String, Float, Column, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker ,relationship

engine = create_engine('sqlite:///OrmPractice.db' , echo = True)
base = declarative_base()