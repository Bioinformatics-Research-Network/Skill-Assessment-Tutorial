import main

def test_hello():
    assert main.hello() == "Hello world!"
    assert main.hello("Friend") == "Hello Friend!"
