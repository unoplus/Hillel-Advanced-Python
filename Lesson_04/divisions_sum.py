#!/usr/bin/env python3
# create by Bender

def get_denominator(file_name: str) -> int:
    """
    The function reads one number from the file, the name of which is passed as
    an argument. The file must exist and contain only one number. As a result,
    the function should return the number read from the file.
    :param file_name: File name.
    :return: Number from file.
    """
    try:
        with open(file_name, 'r') as file:
            file_data = file.read()
    except FileNotFoundError as e:
        print(e)
    if not file_data.isdigit():
        raise TypeError(f'Is not digit! Value = {file_data}')
    if file_data == '0':
        raise ZeroDivisionError(f'Can`t be zero! Value = {file_data}')
    file_data = int(file_data)

    return file_data


def get_list_of_numbers(denominator: int) -> list:
    """
    The function reads and returns a list with integers that are divisible
    by the number, which is passed as an argument to the function.
    :param denominator: Number from file.
    :return: List with integers.
    """
    list_with_numbers = [_ for _ in range(1, 101) if _ % denominator == 0]

    return list_with_numbers


def get_sum(list_of_numbers: list) -> int:
    """
    The function calculates and returns the sum of all numbers in the list
    passed as an argument.
    :param list_of_numbers: List with integers.
    :return: Sum of integers.
    """
    return sum(list_of_numbers)


def write_result(number: int, name_of_result_file: str) -> None:
    """
    The function writes the number passed as the first argument to the file
    whose name is passed in the second argument.
    :param number: Sum of integers.
    :param name_of_result_file: File name.
    :return:
    """
    with open(name_of_result_file, 'w') as file:
        file.write(str(number))


if __name__ == '__main__':
    denominator_num = get_denominator('d.txt')
    list_of_quotient = get_list_of_numbers(denominator_num)
    sum_result = get_sum(list_of_quotient)
    write_result(sum_result, 'result_file.txt')
