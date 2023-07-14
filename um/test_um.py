from um import count

def main():
    test_expression()

def test_expression():
    assert count("instrumentation") == 0
    assert count("yummi") == 0
    assert count("yum") == 0
    assert count("Um, thanks for the, um, album") == 2
    assert count("um?") == 1

if __name__ == "__main__":
    main()