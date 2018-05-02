def product(num1, num2):
    """ #43: calculate product of two numbers
    :param num1: <int>
    :param num2: <int>
    :return: product of two numbers
    :rtype: <int>
    """
    return num1 * num2


def date(num):
    """ #44: date display converter
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


def frequency(arr, term):
    """ 51: check frequency of a given term in a list
    :return: frequency that term shows up in arr
    :rtype: <int>
    """
    if not arr:
        return "arr is None"

    count = 0
    for item in arr:
        if item == term:
            count += 1
    return count


def multiply_even_numbers(arr):
    """ 52: multiply even numbers within a list
    :return: product of the even number
    :rtype: <int>
    """
    product = 1
    count = 0
    for num in arr:
        if num % 2 == 0:
            product *= num
            count += 1
    if count == 0:
        return "no even numbers in this list"
    return product


def capitalize(strr):
    """ 53: capitalize first character of a single word
    :return: same word after modified.
    :rtype: <str>
    """
    return strr[0].upper() + strr[1:]


def capitalize2_0(strr):
    """ 53: capitalize first character of every words
    :return: same string after modified.
    :rtype: <str>
    """
    arr = strr.split()
    res = []
    for word in arr:
        res.append(word[0].upper() + word[1:])
    return ' '.join(res)


def compact(arr):
    """ 54: check nullability of item in a list
    :param arr: array contains both true and None value
    :return: a list of true value
    :rtype: <list>
    """
    return [item for item in arr if item]


def intersection(arr1, arr2):
    """ 55: return a list contains common items from the two input lists
    :rtype: <list>
    """
    # return [item for item in set(arr1) if item in arr2]
    return list(set(arr1) & set(arr2))


def partition(arr):
    """ 56: partition a list into two lists based on the boolean callback
    :rtype: <list of list>
    """
    def callback(num):
        """
        Check for even numbers
        :rtype: <bool>
        """
        return num % 2 == 0
    return [[item for item in arr if callback(item)], [item for item in arr if not callback(item)]]


def contains_purple(*args):
    """ 57: check if str 'purple' is within args
    :param *args: arbituary type
    :rtype: <bool>
    """
    return True if "purple" in args else False


def combine_words(word, **kargs):
    """ 58: add prefix or suffix to a given word
    :param word: <str>
    :param **kargs: key-value pair either queue in or stack in the string.
    :rtype: <str>
    """
    return kargs.get('prefix', '') + word + kargs.get('suffix', '')








































if __name__ == '__main__':
    print(combine_words("hell", prefix="no"))
    print(combine_words("hell", suffix="no"))



# yuzhoujr's github solutions to all exercises | star it if you like it !
