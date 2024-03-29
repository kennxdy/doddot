from helpers import FULLPATH, doing, done, todo


def show_tasks():
    try:
        with open(FULLPATH, 'r') as data:
            lines = data.readlines()
            if len(lines) > 0:
                todo_length = len(lines[0].split(',')) - 1
                print('TODO')
                for item in range(todo_length):
                    print('  [ ] {}'.format(lines[0].split(',')[item]))
                print('')
            else:
                print('TODO')
            if len(lines) > 1:
                doing_length = len(lines[1].split(',')) - 1
                print('DOING')
                for item in range(doing_length):
                    print('  [-] {}'.format(lines[1].split(',')[item]))
                print('')
            else:
                print('DOING')
            if len(lines) > 2:
                done_length = len(lines[2].split(',')) - 1
                print('DONE')
                for item in range(done_length):
                    print('  [x] {}'.format(lines[2].split(',')[item]))
            else:
                print('DONE')
    except FileNotFoundError as err:
        print('An error has occurred: {}'.format(err.filename))


def add_task(text):
    if text == '':
        return
    command = text.split(' ')[-1]
    if command == 'todo':
        words = text.split(' ')
        words.remove('todo')
        task = ''
        for i in range(len(words)):
            task += words[i] + ' '
        if task in todo:
            return
        if task in doing:
            return
        if task in done:
            return
        todo.append(task)
    elif command == 'doing':
        words = text.split(' ')
        words.remove('doing')
        task = ''
        for i in range(len(words)):
            task += words[i] + ' '
        if task in todo:
            return
        if task in doing:
            return
        if task in done:
            return
        doing.append(task)
    elif command == 'done':
        words = text.split(' ')
        words.remove('done')
        task = ''
        for i in range(len(words)):
            task += words[i] + ' '
        if task in todo:
            return
        if task in doing:
            return
        if task in done:
            return
        done.append(task)
    else:
        return
    try:
        with open(FULLPATH, 'r+') as data:
            for i in range(len(todo)):
                data.write('{},'.format(todo[i]))
            data.write('\n')
            for i in range(len(doing)):
                data.write('{},'.format(doing[i]))
            data.write('\n')
            for i in range(len(done)):
                data.write('{},'.format(done[i]))
    except FileNotFoundError as err:
        print('An error has occurred: {}'.format(err.filename))


def move_task(text):
    if text == '':
        return
    command = text.split(' ')[-1]
    if command == 'todo':
        words = text.split(' ')
        words.remove('todo')
        task = ''
        for i in range(len(words)):
            task += words[i] + ' '
        if task in doing:
            doing.remove(task)
        elif task in done:
            done.remove(task)
        else:
            return
        todo.append(task)
    if command == 'doing':
        words = text.split(' ')
        words.remove('doing')
        task = ''
        for i in range(len(words)):
            task += words[i] + ' '
        if task in todo:
            todo.remove(task)
        elif task in done:
            done.remove(task)
        else:
            return
        doing.append(task)
    if command == 'done':
        words = text.split(' ')
        words.remove('done')
        task = ''
        for i in range(len(words)):
            task += words[i] + ' '
        if task in todo:
            todo.remove(task)
        elif task in doing:
            doing.remove(task)
        else:
            return
        done.append(task)
    try:
        with open(FULLPATH, 'w') as data:
            for i in range(len(todo)):
                data.write('{},'.format(todo[i]))
            data.write('\n')
            for i in range(len(doing)):
                data.write('{},'.format(doing[i]))
            data.write('\n')
            for i in range(len(done)):
                data.write('{},'.format(done[i]))
    except FileNotFoundError as err:
        print('An error has occurred: {}'.format(err.filename))


def delete_task(text):
    if text == '':
        return
    task = text + ' '
    if task in todo:
        todo.remove(task)
    if task in doing:
        doing.remove(task)
    if task in done:
        done.remove(task)
    try:
        with open(FULLPATH, 'w') as data:
            for i in range(len(todo)):
                data.write('{},'.format(todo[i]))
            data.write('\n')
            for i in range(len(doing)):
                data.write('{},'.format(doing[i]))
            data.write('\n')
            for i in range(len(done)):
                data.write('{},'.format(done[i]))
    except FileNotFoundError as err:
        print('An error has occurred: {}'.format(err.filename))


def empty_category(category):
    if category == 'todo':
        todo.clear()
    if category == 'doing':
        doing.clear()
    if category == 'done':
        done.clear()
    try:
        with open(FULLPATH, 'w') as data:
            for i in range(len(todo)):
                data.write('{},'.format(todo[i]))
            data.write('\n')
            for i in range(len(doing)):
                data.write('{},'.format(doing[i]))
            data.write('\n')
            for i in range(len(done)):
                data.write('{},'.format(done[i]))
    except FileNotFoundError as err:
        print('An error has occurred: {}'.format(err.filename))


def empty_tasks():
    todo.clear()
    doing.clear()
    done.clear()
    try:
        with open(FULLPATH, 'w') as data:
            data.write('')
    except FileNotFoundError as err:
        print('An error has occurred: {}'.format(err.filename))
