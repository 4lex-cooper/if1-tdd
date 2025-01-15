from fizzbuzz import fizzbuzz


def test_fizz():
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(72) == "fizz"


def test_buzz():
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(95) == "buzz"


def test_fizzbuzz():
    assert fizzbuzz(15) == "fizzbuzz"
    assert fizzbuzz(75) == "fizzbuzz"


def test_number():
    assert fizzbuzz(2) == 2
    assert fizzbuzz(98) == 98
