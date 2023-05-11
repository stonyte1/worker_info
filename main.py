import PySimpleGUI as sg
from frontend import window_add, window_delete, window_update
from processing_data import data_review

headings = ['Name', 'Surname', 'Birth date', 'Position', 'Salary', 'Enter date']
functions = ['Add', 'Update', 'Delete']

workers = data_review()

layout =[ 
[sg.Text('Data processing options: ', font=('Helvetica', 20))],
[sg.Combo(functions, key='function', enable_events=True, s=(50,70))],
[sg.Text('WORKERS INFO: ', justification='center', font=('Helvetica', 15))],
[sg.Table(values=workers, headings=headings, max_col_width=25, auto_size_columns=True,
justification='center', num_rows=len(workers), key='table', enable_events=True)]
]

window = sg.Window('Workers info', layout)

while True:
    try:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'function':
            choosen_function = values['function']
            if choosen_function == 'Add':
                window_add()
            elif choosen_function == 'Update':
                window_update()
            elif choosen_function == 'Delete':
                window_delete()
    except: 
        print('No changes')

window.close()