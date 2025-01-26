from data_structures.queue.my_queue import MyQueue


def test_is_empty():
    queue = MyQueue()
    assert queue.is_empty() is True

    queue.enqueue(10)
    assert queue.is_empty() is False


def test_enqueue():
    queue = MyQueue()
    assert queue.peek() is None

    queue.enqueue(5)
    assert queue.peek() == 5

    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)

    assert queue.pop() == 5
    assert queue.pop() == 10
    assert queue.pop() == 15
    assert queue.pop() == 20
    assert queue.pop() is None
    assert queue.peek() is None

    print("hello")