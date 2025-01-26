from my_linked_list import MyLinkedList

def test_is_empty():
    ll = MyLinkedList()
    assert ll.is_empty() is True

    ll.append(10)
    assert ll.is_empty() is False

def test_append():
    ll = MyLinkedList()
    ll.append(10)
    assert ll.get(0) == 10

    ll.append(20)
    assert ll.get(1) == 20

def test_prepend():
    ll = MyLinkedList()
    ll.prepend(10)
    assert ll.get(0) == 10

    ll.prepend(5)
    assert ll.get(0) == 5
    assert ll.get(1) == 10

def test_get():
    ll = MyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)

    assert ll.get(0) == 10
    assert ll.get(1) == 20
    assert ll.get(2) == 30
    assert ll.get(3) is None

def test_insert_at():
    ll = MyLinkedList()
    ll.append(10)
    ll.append(20)

    ll.insert_at(1, 15)
    assert ll.get(0) == 10
    assert ll.get(1) == 15
    assert ll.get(2) == 20

    ll.insert_at(0, 5)
    assert ll.get(0) == 5
    assert ll.get(1) == 10

def test_remove():
    ll = MyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)

    ll.remove(20)
    assert ll.get(0) == 10
    assert ll.get(1) == 30

    ll.remove(10)
    assert ll.get(0) == 30

    ll.remove(30)
    assert ll.is_empty() is True

def test_remove_at():
    ll = MyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)

    ll.remove_at(1)
    assert ll.get(0) == 10
    assert ll.get(1) == 30

    ll.remove_at(0)
    assert ll.get(0) == 30

    ll.remove_at(0)
    assert ll.is_empty() is True

def test_length():
    ll = MyLinkedList()
    assert ll.length == 0

    ll.append(10)
    assert ll.length == 1

    ll.append(20)
    assert ll.length == 2

    ll.remove(10)
    assert ll.length == 1

    ll.remove(20)
    assert ll.length == 0
