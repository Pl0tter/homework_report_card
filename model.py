import os

report_card = {}
subject = ''
path = 'Python/Examples/Seminar014_ReportCard/class1.txt'


def set_class(class_path: str):
    global path
    path = class_path + '.txt'


def set_subject(our_subject: str):
    global subject
    subject = our_subject


def set_report_card(our_report_card: dict):
    global report_card
    report_card = our_report_card


def open_subject():
    subject_list = []
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for line in file:
        subject_list.append(line.split(';')[0])
    return subject_list


def open_file():
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for line in file:
        if line.split(';')[0] == subject:
            for study in line.split(';')[1].strip().split(', '):
                report_card[study.split(':')[0]] = list(
                    map(int, study.split(':')[1].split()))
            return report_card
        else:
            return 'none'


def save_file():
    new_file = []
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for line in file:
        if line.split(';')[0] != subject:
            new_file.append(line.strip())
    item = []
    for pupil, marks in report_card.items():
        item.append(pupil + ':' + ' '.join(list(map(str, marks))))
    item = subject + ';' + ', '.join(item)
    new_file.append(item)
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(new_file))


def pupil_mark(pupil: str, mark: int):
    marks = report_card.get(pupil)
    marks.append(mark)
    report_card[pupil] = marks


def get_journal():
    return report_card


def pupil_check(pupil: str):
    if pupil in report_card.keys() or pupil == 'exit':
        return pupil
    elif pupil.isdigit() and 1 <= int(pupil) <= len(report_card):
        for i, pupil_name in enumerate(report_card, 1):
            if i == int(pupil):
                return pupil_name
    else:
        return "none"


def class_check(our_class: str):
    return os.path.exists(our_class + '.txt')
