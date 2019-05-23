import pytest
import mat_expressions_to_text.application


def test_1():

    """"перевірка чи всі символи у  є допустимими (0-9,+,-,*,/,=)"""

    with pytest.raises(Exception):
        application.check_input_string('5 5f +55 1ff+sa*8')


def test_2():

    """перевірка чи починається строка знаком математинчих операцій ('+', '*', '/', '=')"""

    with pytest.raises(Exception):
        application.check_input_string('+556 +8+125')


def test_3():

    """перевірка чи закінчується строка знаком математичних операцій ('+','-','*','/','=')"""

    with pytest.raises(Exception):
        application.check_input_string('14+ 15 6+95=')


def test_4():

    """перевірка чи містить строка більшн ніж один знак математичних операцій підряд"""

    with pytest.raises(Exception):
        application.check_input_string('695+ * 551/ 5-362')


def test_5():

    """перевірка чи число не більше ніж 999 999"""

    with pytest.raises(Exception):
        application.check_input_string('1+9999999')


def test_6():

    """ перевірка на прикладі конвертаціїї цифр у слова"""

    assert mat_expressions_to_text.application.convert_number_to_word('100001') == 'one hundred  thousand one'


def test_7():

    """перевірка на прикладі конвертації чисел та знаків математичних операцій в слова"""

    assert mat_expressions_to_text.application.translate_mat_string(['11', '=', '10', '+', '1']) == 'eleven equals ten plus one'
