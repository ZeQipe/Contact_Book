import os
import pickle


"""
The functions of saving and loading the container are implemented here.
"""


def load():
    if os.path.exists(save_path):
        with open(save_path, 'rb') as file:
            return pickle.load(file)
    else:
        print(f'log: loadsaver: load:15l: file not found')
        raise FileNotFoundError("Файл сохранения не найден.")


def save(data):
    with open(save_path, 'wb') as file:
        pickle.dump(data, file)


def get_and_check_path(path_to_save: str):
    if not os.path.isdir(path_to_save + '\\Contacts'):
        os.mkdir(path_to_save + '\\Contacts')
        return get_and_check_path(path_to_save)

    if not os.path.isfile(path_to_save + '\\Contacts\\conbook.jcb'):
        file = open(path_to_save + '\\Contacts\\conbook.jcb', 'w')
        file.close()
        return get_and_check_path(path_to_save)

    return path_to_save + '\\Contacts\\conbook.jcb'


save_path = os.environ.get('LOCALAPPDATA')
save_path = get_and_check_path(save_path)
print(f'log: loadsaver: 39l: path to save - {save_path}')
