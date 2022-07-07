# Doddot

To-Do CLI app to organize your tasks.

## Screenshots

<img src="screenshots/todo-cli.png" alt="menu">
<img src="screenshots/todo-cli2.png" alt="task-list">

## How to use?

A task must belong to one of three categories: **TODO**, **DOING**, **DONE**.

### Add task

To add a task:

`~$ <task> <category_name>`

Example:

```
[-] ~$ Handle all exceptions todo
```

***Note**: The category name must be in lowercase*.

### Move task

To move a task:

`~$ <task> <category_name>`

Example:

```
[-] ~$ Delete temporary files done
```

***Note**: The task must belong to a category*.

### Delete task

To delete a task:

`~$ <task>`

Example:

```
[-] ~$ Create .gitignore file
```

***Note**: The task must belong to a category*.

## License

This project is lincesed under [MIT License](LICENSE).
