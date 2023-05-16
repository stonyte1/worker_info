import PySimpleGUI as sg
from processing_data import data_input, data_update, data_delete, data_review


def window_add():
    layout = [
        [sg.Input('Name', key='name', enable_events=True, s=(50,70))],
        [sg.Input('Surname', key='surname', enable_events=True, s=(50,70))],
        [sg.Input('Birth date YYYY-MM-DD', key='birth date', enable_events=True, s=(50,70))],
        [sg.Input('Position', key='position', enable_events=True, s=(50,70))],
        [sg.Input('Salary', key='salary', enable_events=True, s=(50,70))],
        [sg.Button('Done', key='done', enable_events=True, size=(5, 1))]
    ]

    window = sg.Window('Add workers', layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'done'):
            break
    data_input(values['name'], values['surname'], values['birth date'], values['position'], int(values['salary']))
    window.close()

def window_update():
    default_info = ['name', 'surname', 'birth date', 'responsibility', 'salary']
    workers = data_review()
    workers_id = []
    workers_name = []
    for worker in workers:
        workers_id.append(worker[0])
        workers_name.append(worker[1])

    layout = [
        [sg.Combo(workers_name, key='name', enable_events=True, s=(50,70))],
        [sg.Combo(default_info, key='choice', enable_events=True)],
        [sg.Input('New value', key='new input', enable_events=True)],
        [sg.Button('Enter', key='exit', enable_events=True, size=(5, 1))]
    ]

    window = sg.Window('Update data', layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'exit'):
            break
        
    index = workers_name.index(values['name'])
    ID = workers_id[index]
    data_update(ID, values['choice'], values['new input'])
    window.close()

def window_delete():
    layout = [
        [sg.Text('Delete data', font=('Helvetica', 20))],
        [sg.Input('ID', key='ID', enable_events=True, s=(50,70))],
        [sg.Button('Enter', key='exit', enable_events=True, size=(5, 1))]
    ]

    window = sg.Window('Delete data', layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'exit'):
            break
    data_delete(values['ID'])
    window.close()
