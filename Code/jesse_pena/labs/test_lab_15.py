from lab_15 import clock_to_phrase

def test_clock_to_phrase():
    actual = clock_to_phrase()
    print(actual)
    expected = 'twelve twenty-five'
    print(expected)
    assert actual == expected

if __name__ == "__main__":
    test_clock_to_phrase()