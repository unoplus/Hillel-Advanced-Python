# Create by Bender
import sys


def read_file(some_file: str) -> list:
    """
    This function takes a string with the name of the file from which it reads
    information and stores it in a list of strings.
    :param some_file: accepts a string with a filename
    :return: list of strings
    """
    try:
        with open(some_file, 'r') as file:
            text_data = file.read().split('\n')
            return text_data
    except FileNotFoundError as e:
        print(e)
        sys.exit(0)


def _check_input(some_input: str) -> bool:
    """
    This function checks the user input against conditions. Must be a number
    in the range [0, 5].
    :param some_input: string of user input
    :return: True or False
    """
    if some_input.isdigit():
        if 0 <= int(some_input) <= 5:
            return True
        else:
            return False
    else:
        return False


def start_poll(some_list: list) -> dict:
    """
    This function launches an interactive poll of the user about his
    knowledge of the Python language. The questions are contained in the list
    accepted by the function. The answers are given by the user, according to
    the displayed hint. The function also analyzes the user's response to match
    the condition.
    :param some_list: the list of questions
    :return: dict with questions and answers
    """
    dict_data = {}
    instruction = """
    Возле каждого пункта проставить оценку:
    1 - даже не слышал
    2 - просто слышал
    3 - было рассмотрено, но очень поверхностно
    4 - было рассмотрено
    5 - На тему было выделено достаточно времени, чтобы понимать это хорошо
    0 - Я разбирался с этим сам в независимости от того, было ли это на занятии
    ===========================================================================
    """
    for question in some_list:
        while True:
            print(instruction)
            print(question)
            user_answer = input('Type your answer: ')
            if _check_input(user_answer):
                temp_dict = {question: user_answer}
                break
            else:
                print('Incorrect answer! Please read the instructions!')
        dict_data.update(temp_dict)
    return dict_data


def write_file(some_dict: dict) -> None:
    """
    This function takes a data dictionary and saves it in a formatted form to a
    text file.
    :param some_dict: data dictionary
    :return:
    """
    with open('python_knowledges.txt', 'w') as file:
        file.write('=' * 110)
        for key, value in some_dict.items():
            file.write('\n|| {:100s}|| {:2s}||\n'.format(key, str(value)))
            file.write('=' * 110)


if __name__ == '__main__':
    questions = read_file('source/source.txt')
    answers = start_poll(questions)
    write_file(answers)
