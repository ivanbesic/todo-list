
tasks = []

while True:


    print('What would you like to do? ')
    print('1 : Add a task')
    print('2 : View all tasks')
    print('3 : Remove a task')
    print('4 : exit')

    choice = input('What do you want do to? (1/2/3/4) ')

    if choice == '1':
        opt = input('What task would you like to add? ')
        tasks.append(opt)

    elif choice == '2':
        for i, n in enumerate(tasks, start = 1):
            print(f'{i} - {n}')

    elif choice == '3':
        for i, n in enumerate(tasks, start = 1):
            print(f'{i} - {n}')
        delete = int(input('Choose the number of task that you want to remove - '))
        if 1 <= delete <= len(tasks):
            tasks.pop(delete - 1)
            print('Task deleted.')
        else:
            print('Error - entered non-existable number of task. ')
    elif choice == '4':
        print('Bye!')
        break

    else:
        print('Non-existent opinion. Pick (1/2/3/4)')

    repeat = input('Do you want to continue? (yes/no) ')
    if repeat.lower() != 'yes':
        print('Thank you and bye!')
        break




    
        



    

