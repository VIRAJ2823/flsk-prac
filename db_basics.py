from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///my_database.db', echo = True)

conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS users ( name TEXT, age INTEGER)"))

conn.commit()