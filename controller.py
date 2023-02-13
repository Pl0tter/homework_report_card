import view
import model


def start():
    while True:
        our_class = view.input_class()
        if model.class_check(our_class):
            model.set_class(our_class)
            view.list_of_subject(model.open_subject())
            break
        else:
            view.class_none()

    while True:
        model.set_subject(view.input_subject())
        our_report_card = model.open_file()
        if our_report_card == 'none':
            view.subject_none()
        else:
            model.set_report_card(our_report_card)
            break

    while True:
        report_card = model.get_journal()
        view.list_of_child(report_card)
        while True:
            pupil = model.pupil_check(view.who_answer())
            if pupil == 'none':
                view.pupil_none()
            else:
                break
        if pupil == 'exit':
            break
        while True:
            mark = int(view.what_mark(pupil))
            if 1 <= mark <= 5:
                break
            else:
                view.mark_none()
        model.pupil_mark(pupil, mark)
    model.save_file()
