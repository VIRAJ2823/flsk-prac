from sqlalchemy import MetaData, create_engine, text ,  MetaData , Table , Column , Integer , String , Insert

engine = create_engine('sqlite:///mydatabase.db', echo = True)

meta = MetaData()

people = Table(
    'people',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)

meta.create_all(engine)

conn = engine.connect()

insert_statement = Insert(people).values(id = 1 ,name= 'viraj', age= 25)
result = conn.execute(insert_statement)
conn.commit()