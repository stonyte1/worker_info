from table import engine, Worker, Base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def data_input(name, surname, birthdate, responsibility, salary):
    worker_info = Worker(name, surname, birthdate, responsibility, salary)
    session.add(worker_info)
    session.commit()

def data_review():
    workers = session.query(Worker).all()
    separated_workers = []

    for worker in workers:
        worker_info = [worker.id, worker.name, worker.surname, worker.birth_day, worker.responsibility, worker.salary, worker.experience]
        separated_workers.append(worker_info)
    return separated_workers

def data_delete(id):
    delete_id = session.query(Worker).get(id)
    session.delete(delete_id)
    session.commit()

def data_update(id, choice, value):
    update_id = session.query(Worker).get(id)
    
    if choice == 'name':
        update_id.name = value
    elif choice == 'surname':
        update_id.surname = value
    elif choice == 'birth date':
        update_id.birth_day = value
    elif choice == 'responsibility':
        update_id.responsibility = value
    elif choice == 'salary':
        update_id.salary = value
    
    session.commit()