from data_structures.stack.my_stack import MyStack

def test_is_empty():
    stack = MyStack()
    assert stack.is_empty() is True

    stack.push(10)
    assert stack.is_empty() is False

def test_push():
    stack = MyStack()
    stack.push(10)
    assert stack.peek() == 10

    stack.push(20)
    assert stack.peek() == 20

def test_pop():
    stack = MyStack()
    stack.push(10)
    stack.push(20)

    assert stack.pop() == 20
    assert stack.peek() == 10

    assert stack.pop() == 10
    assert stack.is_empty() is True
    assert stack.pop() is None

def test_peek():
    stack = MyStack()
    assert stack.peek() is None

    stack.push(10)
    assert stack.peek() == 10

    stack.push(20)
    assert stack.peek() == 20

def test_length():
    stack = MyStack()
    assert stack.length == 0

    stack.push(10)
    assert stack.length == 1

    stack.push(20)
    assert stack.length == 2

    stack.pop()
    assert stack.length == 1

    stack.pop()
    assert stack.length == 0