# pytest распознает функции как тестовые если начинаются с test_*
def test_user_login():
    print('Hello')


# pytest распознает классы как тестовые если начинаются с Test
class TestUserLogin:
    ...

    def test_1(self):
        ...

    def test_2(self):
        ...


# python -m pytest - поиск и запуск всех тестов
# python -m pytest -s -v -k "test": -s вывод консольных сообщений/-v детализированный вывод инфы о тестах/-k поиск по названию тестов

def test_assert_positive_case():
    assert 2 + 2 == 4


def test_assert_negative_case():
    assert 2 + 2 == 5
