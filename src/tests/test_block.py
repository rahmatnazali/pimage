from pimage.block import Block
from PIL import Image

rgb_image = Image.new(mode="RGB", size=(64, 64))
grayscale_image = Image.new(mode="L", size=(64, 64))


def test_block_initiate():
    block = Block(grayscale_image, rgb_image, 10, 20, 32)
    assert block.block_dimension == 32
    assert block.coordinate == (10, 20)


def test_block_compute_pca():
    block = Block(grayscale_image, rgb_image, 10, 20, 32)
    result = block.compute_pca()
    assert isinstance(result, list)
    assert len(result) == 64
    assert result[0] == 1.0
    assert result[1] == 0.0


def test_block_compute_characteristic_feature():
    block = Block(grayscale_image, rgb_image, 10, 20, 32)
    result = block.compute_characteristic_features()
    assert isinstance(result, list)
    assert len(result) == 7
    assert result == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
