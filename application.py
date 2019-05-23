import re


class MyException(Exception):
    pass


mat_operations = ['+', '-', '*', '/', '=']


valid_char = [str(s) for s in range(10)] + mat_operations + list(' ')


def check_input_string(string):

    """перевірка вхідної строки:
       1.чи всі символи є допустимими (0-9,+,-,*,/,=)
       2.строка не може починатися з таких символів ('+', '*', '/', '=')
       3.строка не може закінчуватися знаком математичних операцій ('+','-','*','/','=')
       4.у строці не може бути два знаком математичних операцій підряд
       5.чило не може бути більше 6 знаків"""

    loop = True
    string = re.sub(r'\s+', '', string)
    try:
        # допустимі символи (0-9,+,-,*,/,=)
        for char in string:
                if char in valid_char:
                    continue
                else:
                    loop = False
                    raise MyException('invalid input')
        # строка не може починатися з таких символів ('+', '*', '/', '=')
        if string[0] in ['+', '*', '/', '=']:
            loop = False
            raise MyException('invalid input')
        # строка не може закінчуватися символом математичних операцій ('+','-','*','/','=')
        elif string[-1] in mat_operations:
            loop = False
            raise MyException('invalid input')
        # у строці не може бути два символи знаків математичних операцій підряд
        elif len(string) >= 2:
            count_digits = 0
            for i in range(len(string)-1):
                if string[i] in mat_operations and string[i+1] in mat_operations:
                    loop = False
                    raise MyException('invalid input')
                elif string[i] not in mat_operations and string[i+1] not in mat_operations:
                    count_digits += 1
                    # чило від 0 до 999 9999
                    if count_digits > 6:
                        loop = False
                        raise MyException('invalid input')
                elif string[i] not in mat_operations and string[i+1] in mat_operations:
                    count_digits = 0
                elif string[i] in mat_operations and string[i+1] not in mat_operations:
                    count_digits += 1
    except MyException as error:
        print(error)
    return loop, string


mat_operations_str = {'+': 'plus', '-': 'minus', '*': 'multiply', '/': 'divide', '=': 'equals'}

one_to_nineteen = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                   'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                   'sixteen', 'seventeen', 'eighteen', 'nineteen')

decs = ('', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sivty', 'seventy', 'eighty', 'ninety')


def convert_string_to_znak(string):

    """функція конвертації знаків математичних операцій в слова"""

    return mat_operations_str[string]


def convert_number_to_word(string):

    """функція переводу числа від 0 до 999 999 в слова"""

    res = ''
    integer = int(string)
    length = len(string)
    
    if length == 1:
        return one_to_nineteen[integer]
    
    elif length == 2:
        if integer in range(20):
                return one_to_nineteen[integer]

        elif integer in range(20, 100):
                
                res += decs[int(string[0])]
                res += ' '
                
                if string[1] != '0':
                    res += convert_number_to_word(string[1])
        return res
    
    elif length == 3:

        if int(string[:-2]) != 0:
            res += convert_number_to_word(string[:-2])
            res += ' hundred '
            
            if int(string[-2:]) != 0:
                res += convert_number_to_word(string[-2:])
            return res

        elif int(string[:-2]) == 0:
            
            res += convert_number_to_word(string[-2:])
            return res

    elif length in range(4, 7):
        if int(string[:-3]) != 0:
            res += convert_number_to_word(string[:-3])
            res += ' thousand '
            
            if int(string[-3:]) != 0:
                res += convert_number_to_word(string[-3:])
            return res

        elif int(string[:-3]) == 0:
            res += convert_number_to_word(string[-3:])
            return res
    return res


def convert_string_to_list(input_string):

    """функція конвертації строки в список чисел та знаків математичних операцій"""

    pattern = re.compile(r'[0-9]+|[=*+-/]')
    return pattern.findall(input_string)


def translate_mat_string(list):

    """функція конвертації списка чисел та знаків математичних операцій в слова"""
    res = ''
    for elem in list:
        if elem.isdigit():
            res += (convert_number_to_word(elem))
            res += ' '
        else:
            res += (convert_string_to_znak(elem))
            res += ' '
    return res[:-1]


def main():
    loop = False
    valid_text = ''
    while loop == False:
        text = str(input('input string: '))
        loop, valid_text = check_input_string(text)
    else:
        text_list = convert_string_to_list(valid_text)
        print(translate_mat_string(text_list))


if __name__ == '__main__':
    main()
