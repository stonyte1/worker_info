from table import engine, Worker, Base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()

def data_input():
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    birthdate = datetime.strptime(input('Enter birthdate: '), '%Y-%m-%d')
    responsibility = input('Enter responsibility: ')
    salary = float(input('Enter salary: '))

    worker_info = Worker(name, surname, birthdate, responsibility, salary)
    session.add(worker_info)
    session.commit()

def data_review():
    workers = session.query(Worker).all()
    for worker in workers:
        print(worker)

def data_delete():
    id = int(input('Enter the ID to delete: '))
    delete_id = session.query(Worker).get(id)
    session.delete(delete_id)
    session.commit()

def data_update():
    id = int(input('Enter the ID to update: '))
    update_id = session.query(Worker).get(id)
    
    while True:
        choice = input('Enter witch update to make: name, surname, birth date, responsibility, salary ')
        if choice == 'name':
            update_id.name = input('Enter new name: ')
        elif choice == 'surname':
            update_id.surname = input('Enter new surname: ')
        elif choice == 'birth date':
            update_id.birth_day = datetime.strftime(input('Enter new birth date: '), '%Y-%m-%d')
        elif choice == 'responsibility':
            update_id.responsibility = input('Enter new responsability: ')
        elif choice == 'salary':
            update_id.salary = float(input('Enter new salary: '))
        else:
            print('Wrong input, try again')
        choice = int(input('Press 0 to exit'))
        if choice == 0:
            break


