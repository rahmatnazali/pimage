import time
from pathlib import Path
from typing import Tuple, List, Optional

import imageio
import numpy

from . import image_object
from .configuration import Configuration


def detect(input_path: str,
           configuration: Optional[Configuration] = None,
           verbose=False) -> Tuple[List, numpy.ndarray, numpy.ndarray]:
    """
    Detect an image with optionally supplied configuration and return the detection result.

    Args:
        input_path (str): image input path
        configuration (Configuration): optional Configuration object. If omitted, default configuration will be used
        verbose (bool): whether to enable verbose mode

    Returns: Tuple of `fraud_list`, `ground_truth_image`, `result image`
    """

    input_path = Path(input_path)
    if not input_path.exists():
        print(f"Error: Source Directory \"{str(input_path)}\" did not exist.")
        exit(1)

    if configuration is None:
        configuration = Configuration()

    single_image = image_object.ImageObject(str(input_path), configuration, verbose)
    return single_image.run()


def detect_and_export(input_path: str,
                      output_path: str = ".",
                      configuration: Configuration = None,
                      verbose: bool = False):
    """
    Detects an image under a specific directory and export the result into image file.

    Args:
        input_path (str): image input path
        output_path (str): output path of the result image
        configuration (Configuration): optional Configuration object. If omitted, default configuration will be used
        verbose (bool): whether to enable verbose mode

    Returns: fraud_list
    """

    input_path = Path(input_path)
    output_path = Path(output_path)
    if not input_path.exists():
        print(f"Error: Source Directory \"{str(input_path)}\" did not exist.")
        exit(1)
    if not output_path.exists():
        print(f"Error: Output Directory \"{str(output_path)}\" did not exist.")
        exit(1)

    fraud_list, ground_truth_image, result_image = detect(str(input_path), configuration, verbose)

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = input_path.name
    imageio.imwrite(output_path / (timestamp + "_" + filename), ground_truth_image)
    imageio.imwrite(output_path / (timestamp + "_lined_" + filename), result_image)

    return fraud_list
