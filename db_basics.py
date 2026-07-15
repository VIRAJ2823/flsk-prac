
from sqlalchemy import MetaData, create_engine, text ,  MetaData , Table , Column , Integer , String , Insert , Float , ForeignKey, values , func

engine = create_engine('sqlite:///mydatabase.db', echo = True)

meta = MetaData()

people = Table(
    'people',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)

things = Table(
    'things',
    meta,
    Column('id',Integer, primary_key = True),
    Column('description' , String , nullable = False),
    Column('value', Float),
    Column('owner', Integer,ForeignKey('people.id'))
)

meta.create_all(engine)

conn = engine.connect()

# stmt1 = Insert(people).values(id=1, name="viraj", age=25)
# stmt2 = Insert(people).values(id=2, name="nikhil", age=15)
# stmt3 = Insert(people).values(id=3, name="sachin", age=30)

# #conn.execute(stmt1)
# #conn.execute(stmt2)
# conn.execute(stmt3)
# #conn.commit()


# delete_statement = people.delete().where(people.c.name == "sachin")
# conn.execute(delete_statement)
# conn.commit()       # Save the update

# # Now execute a SELECT query
# select_statement = people.select()

# result = conn.execute(select_statement)

# for row in result.fetchall():
#     print(row)

# insert_people = people.insert().values([
#     {'name': 'viraj', 'age': 25},
#     {'name': 'nikhil', 'age': 15},
#     {'name': 'sachin', 'age': 30},
#     {'name': 'yujin', 'age': 20},
# ])

# insert_things = things.insert().values([
#     {'owner': 1 , 'description':'laptop', 'value': 1000.0},
#     {'owner':2, 'description': 'phone', 'value': 500.0},
#     {'owner':3, 'description': 'tablet', 'value': 300.0},
#     {'owner':4, 'description': 'watch', 'value': 200.0},
#     {'owner':1, 'description': 'headphones', 'value': 150.0},
#     {'owner':2, 'description': 'keyboard', 'value': 100.0} 
# ])

# conn.execute(insert_people)
# conn.commit()

# conn.execute(insert_things)
# conn.commit()

# join_statement = people.join(things, people.c.id  == things.c.owner)
# select_statement = people.select().with_only_columns(people.c.name, things.c.description).select_from(join_statement) 

# result = conn.execute(select_statement)

# for row in result.fetchall():
#     print(row)


group_by_statement = things.select().with_only_columns(things.c.owner,  func.sum(things.c.value)).group_by(things.c.owner)
result = conn.execute(group_by_statement)

for row in result.fetchall():
    print(row)