import time
from pathlib import Path
from typing import Tuple, List

import imageio
import numpy

from . import image_object


def detect(input_path, block_size=32, verbose=False) -> Tuple[List, numpy.ndarray, numpy.ndarray]:
    """
    Detects an image under a specific directory and returns the image data
    :param input_path: path to input image
    :param block_size: the block size of the image pointer (eg. 32, 64, 128)
    The smaller the block size, the more accurate the result is, but takes more time, vice versa.
    :param verbose: if true, step by step progress and iteration with tqdm is printed
    :return: None
    """

    input_path = Path(input_path)
    if not input_path.exists():
        print(f"Error: Source Directory \"{str(input_path)}\" did not exist.")
        exit(1)

    single_image = image_object.ImageObject(input_path, block_size, verbose)
    return single_image.run()


def detect_and_export(input_path, output_path=".", block_size=32, verbose=False):
    """
    Detects an image under a specific directory and export the result into image file
    """

    input_path = Path(input_path)
    filename = input_path.name
    output_path = Path(output_path)
    if not input_path.exists():
        print(f"Error: Source Directory \"{str(input_path)}\" did not exist.")
        exit(1)
    if not output_path.exists():
        print(f"Error: Output Directory \"{str(output_path)}\" did not exist.")
        exit(1)

    fraud_list, ground_truth_image, result_image = detect(input_path, block_size, verbose)

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    imageio.imwrite(output_path / (timestamp + "_" + filename), ground_truth_image)
    imageio.imwrite(output_path / (timestamp + "_lined_" + filename), result_image)

    return fraud_list
