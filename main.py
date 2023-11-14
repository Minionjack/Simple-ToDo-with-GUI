from functions import get_todos, write_todos
while True:
    user_action = input('Type add, show, edit, complete or exit:')
    user_action = user_action.strip()

    if user_action.startswith('Add'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos, 'todos.txt')

    elif user_action.startswith('Show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index+1}-{item}'
            print(row)
    elif user_action.startswith('Edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()

            new_todo = input('Enter new todo ')
            todos[number] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print('Your command is not valid')
            continue

    elif user_action.startswith('Complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos)
            message = f'Todos {todo_to_remove} was removed from the list.'
            print(message)
        except IndexError:
            print('There was no item with that number')
            continue

    elif user_action.startswith('Exit'):
        break
    else:
        print('Command not valid.')

print('bye')



