def product(num1, num2):
    """ #43: calculate product of two numbers
    :param num1: <int>
    :param num2: <int>
    :return: product of two numbers
    :rtype: <int>
    """
    return num1 * num2


def date(num):
    """ 44: date display converter
    :param num: <int>
    :return: corresponding date in English
    :rtype: <str>
    """
    date = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']
    if 1 <= num <= 7 and isinstance(num, int):
        return date[num-1]
    return None


def last_element(arr):
    """ 45: return last element of an array
    :param arr: <list>
    :return: last element of an array
    :rtype: <anything>
    """
    if arr:
        return arr[-1]
    return None


def number_compare(num1, num2):
    """ 46: compare given input number
    :param num1 and num2: <int>
    :return: greater value of the two input
    :rtype: <int>
    """
    if num1 > num2:
        return "first is greater"
    elif num1 < num2:
        return "second is greater"
    return "they are equal"


def single_letter_count(strr, letter):
    """ 47: check apperench of a letter in a string
    :param strr: character string
    :param char: single character
    :return: apperench of a letter in a string
    :rtype: <int>
    """
    count = 0
    for char in strr.lower():
        if char == letter.lower():
            count += 1
    return count


def multiple_letter_count(strr):
    """ 48: return multiple letter count in a dict form
    :param strr: character string
    :return: multiple letter count in a dict form
    :rtype: <dict>
    """
    dict = {}
    for char in strr.lower():
        dict[char] = dict.get(char, 0) + 1
    return dict


def list_manipulation(arr, operation, location, value=None):
    """ 49: perform add/remove operations on beginning/end of a list
    :param arr: <list>
    :param operation: <str> with 'add' or 'remove' options
    :param location: <str> with 'beginning' or 'end' options
    :param value: <int> only for add operation
    :return: end result array
    :rtype: <list>
    """
    if operation == "add":
        if not location or not value:
            return "please input where to add or an value"
        if location == "beginning":
            arr.insert(0, value)
        elif location == "end":
            arr.append(value)

    elif operation == "remove":
        if value:
            return "Get rid of value parameter on remove"
        if not arr:
            return "List is empty"
        if location == "beginning":
            arr.pop(0)
        elif location == "end":
            arr.pop()

    return arr


def is_palindrome(strr):
    """ 50: check if a character string is palindrome
    :param strr: <str>
    :return: Boolean on whether a string is palidrome
    :rtype: <bool>
    """
    strr = ''.join(strr.split())
    return strr.lower() == strr[::-1].lower()


if __name__ == '__main__':
    print(is_palindrome('testing'))
    print(is_palindrome('amanaplanacanalpanama'))
    print(is_palindrome('a man a plan a canal Panama'))
