import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///workers.db')
Base = declarative_base()
class Worker(Base):
    __tablename__ = 'Worker'
    id = Column(Integer, primary_key=True)
    name = Column('Name', String)
    surname = Column('Surname', String)
    birth_day = Column('Birth date', DateTime)
    responsibility = Column('Responsibility', String)
    salary = Column('Salary', Float)
    experience = Column('Works since', DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, surname, birth_day, responsibility, salary):
        self.name = name
        self.surname = surname
        self.birth_day = birth_day
        self.responsibility = responsibility
        self.salary = salary

    def __repr__(self):
        return f'{self.id} {self.name} {self.surname} {self.birth_day}, {self.responsibility} {self.salary}'

Base.metadata.create_all(engine)
