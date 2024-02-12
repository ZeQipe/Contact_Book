import os
import pickle


def load():
    if os.path.exists(save_path):
        with open(save_path, 'rb') as file:
            return pickle.load(file)
    else:
        raise FileNotFoundError("Файл сохранения не найден.")


def save(data):
    with open(save_path, 'wb') as file:
        pickle.dump(data, file)


def get_and_check_path(save_path: str):
    if not os.path.isdir(save_path + '\\Contacts'):
        os.mkdir(save_path + '\\Contacts')
        return get_and_check_path(save_path)

    if not os.path.isfile(save_path + '\\Contacts\\conbook.jcb'):
        file = open(save_path + '\\Contacts\\conbook.jcb', 'w')
        file.close()
        return get_and_check_path(save_path)

    return save_path + '\\Contacts\\conbook.jcb'


def export_contacts():
    pass


def import_contacts():
    pass


save_path = os.environ.get('LOCALAPPDATA')
save_path = get_and_check_path(save_path)
print(f'log: loadsaver: 41 line (path) - {save_path}')