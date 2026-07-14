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

stmt1 = Insert(people).values(id=1, name="viraj", age=25)
stmt2 = Insert(people).values(id=2, name="nikhil", age=15)

#conn.execute(stmt1)
#conn.execute(stmt2)
#conn.commit()


select_statement = people.select().where(people.c.age > 20)

result = conn.execute(select_statement)

for row in result.fetchall():
    print(row)