from sqlalchemy import create_engine, Integer, String, Column, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///OrmPractice.db', echo=True)

base = declarative_base()


class person(base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

    things = relationship('things', back_populates='person')


class things(base):
    __tablename__ = 'things'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    value = Column(Integer)
    owner_id = Column(Integer, ForeignKey('people.id'))

    person = relationship('person', back_populates='things')


# Create tables
base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# Create persons
p1 = person(name="Viraj", age=22)
p2 = person(name="Sachin", age=25)
p3 = person(name="Nikhil", age=22)
p4 = person(name="Shawn", age=20)
p5 = person(name="Delta", age=15)


# Create related things
t1 = things(description="Laptop", value=50000, person=p1)
t2 = things(description="Phone", value=20000, person=p1)
t3 = things(description="Keyboard", value=2000, person=p1)
t4 = things(description="Bike", value=200000, person=p2)
t5 = things(description="AC", value=4000, person=p3)
t6 = things(description="Watch", value=50000, person=p3)
t7 = things(description="Pencil", value=700, person=p4)
t8 = things(description="Pen", value=20, person=p4)
t9 = things(description="Book", value=90, person=p5)


# session.add_all([p1, p2, p3, p4, p5])
# session.add_all([t1, t2, t3, t4, t5, t6, t7, t8, t9])

session.commit()

# read people
result = session.query(person).all()

for row in result:
    print(row.id,row.name,row.age)


result =  session.query(person).filter_by(id=1).first()
