import traceback


def load_qss(file_name):
    try:
        with open(file_name, 'r') as fh:
            return fh.read()
    except FileNotFoundError as err:
        print(traceback.format_exc())
        return ''
