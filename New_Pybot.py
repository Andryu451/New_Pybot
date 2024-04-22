# Пытаемся написать бота, начнём с простого:
cmd = """
help - Показать существующие команды
add - Добавить задачу в TODO
show - показать все добавленные задачи
"""
tasks = []
run = True
while run:
    command = input("Введите команду: ")
    if command  == "help":
        print(help)
    elif command == "add":
        task = input("Какую задачу добавить в TODO?: ")
        tasks.append(task)
        print("Задача добавлена")
    elif command == "show":
        print(tasks)
    else:
        print("Неизвестаня команда")
        break
print("До скорой встречи!")
