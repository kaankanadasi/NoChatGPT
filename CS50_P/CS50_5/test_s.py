from CS50_P.CS50_5.square import square

def main():
    test()

def test():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try: 
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
    
"""
    try:
        for i in range(-2,2):
            assert square(i) == i *i
    except AssertionError:
        print(f"{i} squared was not {i*i}")
"""

if __name__ == "__main__":
    main()