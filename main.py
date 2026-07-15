from sqlalchemy import create_engine ,Integer ,String ,Float ,Column ,ForeignKey
from sqlalchemy.orm import declarative_base , sessionmaker , relationship

engine = create_engine('sqlite:///mydatabase.db', echo = True)

base = declarative_base()

class person(base):
    __tablename__ = 'people'
    id = Column(Integer,primary_key=True)
    name = Column(String , nullable=False)
    age = Column(Float)

    things = relationship('thing',back_populates='person')



class things(base):
    __tablename__ = 'thing'
    id = Column(Integer,primary_key=True)
    description = Column(String , nullable = False)
    value = Column(Float)
    owner = Column(Integer, ForeignKey = ('people.id'))

    person = relationship('people',back_populates='things')