import model


def input_class():
    return input('С каким классом работаем? ').upper()


def class_none():
    print('Такого учебного класса нет. Попробуйте еще раз.')


def input_subject():
    return input('Какой предмет? ').lower()


def subject_none():
    print('Такого предмета нет в журнале. Попробуйте еще раз.')


def who_answer():
    return input('Кто будет отвечать? (Введите ФИО или номер. При завершении отправить exit) ')


def pupil_none():
    print('Такого ученика нет в списке. Попробуйте еще раз.')


def what_mark(pupil: str):
    return input(f'На какую оценку ответил {pupil}? ')


def mark_none():
    print('Введите оценку от 1 до 5.')


def list_of_child(report_card: dict):
    for i, pupil in enumerate(report_card, 1):
        print(f'{i}. {pupil:20} {report_card.get(pupil)}')


def list_of_subject(subjects: list):
    for i, subject in enumerate(subjects, 1):
        print(f'{i}. {subject:20}')
