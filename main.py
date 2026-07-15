from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///mydatabase.db', echo=True)

base = declarative_base()

class person(base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Float)

    things = relationship('things', back_populates='person')


class things(base):
    __tablename__ = 'things'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    value = Column(Float)
    owner = Column(Integer, ForeignKey('people.id'))

    person = relationship('person', back_populates='things')


base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_person = person(name='sam', age=26)
session.add(new_person)
session.commit()

new_thing = things(description='camera', value=600 , owner = new_person.id)
session.add(new_thing)
session.commit()

new_thing.person = new_person

print([t.description for t in new_person.things])
print(new_thing.person)

