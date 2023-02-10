from pimage.container import Container


def test_container_initiate():
    container = Container()
    assert container.get_length() == 0

