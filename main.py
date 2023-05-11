from processing_data import data_input, data_review, data_delete, data_update

while True:
    #MENIU
    choice = int(input(' 1 - Input data \n 2 - Review data \n 3 - Delete date \n 4 - Update data \n 0 - Leave program \n'))
    if choice == 0:
        print('Bye')
        break
    elif choice == 1:
        try:
            data_input()
        except:
            print('Wrong input try again')  
    elif choice == 2:
        data_review()
    elif choice == 3:
        data_review()
        try:
            data_delete()
        except:
            print('Wrong input try again')
    elif choice == 4:
        data_review()
        try:
            data_update()
        except:
            print('Wrong input try again')




