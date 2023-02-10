from pimage.container import Container


def test_container_initiate():
    container = Container()
    assert container.get_length() == 0


def test_container_add():
    container = Container()
    container.append_block(((0, 1), [0, 1, 2], [3, 4, 5]))
    assert container.get_length() == 1


def test_container_sort_feature():
    container = Container()
    container.append_block(((0, 3), [1, 2, 3], [4, 5, 7]))
    container.append_block(((0, 2), [1, 2, 3], [4, 5, 6]))
    container.append_block(((0, 1), [0, 1, 2], [3, 4, 5]))

    container.sort_by_features()
    assert container.get_length() == 3
    assert container.container == [
        ((0, 1), [0, 1, 2], [3, 4, 5]),
        ((0, 2), [1, 2, 3], [4, 5, 6]),
        ((0, 3), [1, 2, 3], [4, 5, 7])
    ]
