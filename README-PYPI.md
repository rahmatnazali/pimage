This is a python package for detecting copy-move attack on a digital image.

More documentation is detailed on the [Github page](https://github.com/rahmatnazali/pimage).

## Using the package

To install the package, simply hit it with pip: `pip3 install pimage`

### API for the detection process

- The API for detection process is provided via `copy_move.detect(image_path, block_size)` method. 
- Determining the `block_size`: The first algorithm use block size of `32` pixels so this package will use the same value by default. Increasing the size means faster run time at a reduced accuracy. Analogically, decreasing the size means longer run time with increased accuracy.

For example:

```python3
from pimage import copy_move

fraud_list, ground_truth_image, result_image = copy_move.detect("dataset_example_blur.png", block_size=32)
```

- `fraud_list` will be the list of `(x_coordinate, y_coordinate)` of the blocks group and the total number of the blocks it is formed with. If this list is not empty, we can assume that the image is being tampered. For example:
    ```
    ((-57, -123), 2178)
    ((-11, 140), 2178)
    ((-280, 114), 2178)
    ((-34, -305), 2178)
    ((-37, 148), 2178)
    ```
  the above output means there are 5 possible matched/identical region with 2178 overlapping blocks on each of it
- `ground_truth_image` contains the black and white ground truth of the detection result. This is useful for comparing accuracy, MSE, etc with the ground truth from the dataset
- `result_image` is the given image where the possible fraud region will be color-bordered (if any)

`ground_truth_image` and `result_image` will be formatted as `numpy.ndarray`. It can further be processed as needed. For example, it can be programmatically modified and then exported later as image like so:

```python
import imageio

imageio.imwrite("result_image.png", result_image)
imageio.imwrite("ground_truth_image.png", ground_truth_image)
```

### Quick command to detect an image

To quickly run the detection command for your image, the `copy_move.detect_and_export()` is also provided. The command is identical with `.detect()` but it also save the result to desired output path.

```python
from pimage import copy_move

copy_move.detect_and_export('dataset_example_blur.png', 'output', block_size=32)
```

this code will save the `ground_truth_image` and `result_image` inside `output` folder.