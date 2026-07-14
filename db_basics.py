from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///mydatabase.db', echo = True)

conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS people ( name TEXT, age INTEGER)"))

conn.commit()

from sqlalchemy.orm import Session

session = Session(engine)

session.execute(text('INSERT INTO PEOPLE (name,age)  VALUES ("VIRAJ", 19)'))

session.commit()
