from hello import hello

def test_hello():
    for name in ["Kaan", "David", "Ken"]:
        assert hello(name) == f"hello {name}"
    
def test_defualt():
    assert hello() == "hello world"