import main


def test_say_hello():
    assert main.say_hello() == "Hello World!"


def test_hey_jamal():
    assert main.hey_you("Jamal") == "Hello, Jamal!"


def test_hey_nate():
    assert main.hey_you("Nate") == "Hello, Nate!"


def test_age_in_2050_born_1990():
    assert main.age_in_2050(2000) == "You will be 50 in 2050!"


def test_can_i_take_your_order_all_1():
    assert main.can_i_take_your_order(1, 1, 1) == (4.5, 1.5, 1.0, 7)


def test_can_i_take_your_order_many():
    assert main.can_i_take_your_order(2, 3, 4) == (9.0, 4.5, 4.0, 17.50)
