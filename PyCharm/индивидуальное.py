# -*- coding: utf-8 -*-

def create_greeting_template(template):
    def inner_function(last_name, first_name):
        formatted_template = template.replace('%F%', last_name).replace('%N%', first_name)
        return formatted_template
    return inner_function

if __name__ == "__main__":
    n = input("Введите вашу фамилию: ")
    l = input("Введите ваше имя: ")

    # Создаем замыкание с шаблоном
    greeting_template = create_greeting_template("Уважаемый %F%, %N%! Вы делаете работу по замыканиям функций.")

    # Вызываем внутреннюю функцию замыкания и отображаем результат
    result = greeting_template(n, l)
    print(result)