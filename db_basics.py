
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
stmt3 = Insert(people).values(id=3, name="sachin", age=30)

#conn.execute(stmt1)
#conn.execute(stmt2)
conn.execute(stmt3)
#conn.commit()


delete_statement = people.delete().where(people.c.name == "sachin")
conn.execute(delete_statement)
conn.commit()       # Save the update

# Now execute a SELECT query
select_statement = people.select()

result = conn.execute(select_statement)

for row in result.fetchall():
    print(row)