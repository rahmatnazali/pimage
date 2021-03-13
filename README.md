# Copy-Move Detection on Digital Image using Python

**Old Python 2 version**:This repository now host the python 3 version. You can find the old module written with python 2 on this [repository](https://github.com/rahmatnazali/image-copy-move-detection-python2).

## Description
This is an implementation of python script to detect a copy-move manipulation attack on digital image based on Overlapping Blocks.

This script is implemented with a modification of two algoritms publicated in a scientific journals:
1. Duplication detection algorithm, taken from [Exposing Digital Forgeries by Detecting Duplicated Image Region](http://www.ists.dartmouth.edu/library/102.pdf) (old link is dead, go to [alternative link](https://www.semanticscholar.org/paper/Exposing-Digital-Forgeries-by-Detecting-Duplicated-Popescu-Farid/b888c1b19014fe5663fd47703edbcb1d6e4124ab)); Fast and smooth attack detection algorithm on digital image using [principal component analysis](https://en.wikipedia.org/wiki/Principal_component_analysis), but sensitive to noise and _post region duplication process_ (explained in the paper above)
2. Robust detection algorithm, taken from [Robust Detection of Region-Duplication Forgery in Digital Image](http://ieeexplore.ieee.org/document/1699948/); Slower and having rough result attack detection algorithm but are considered robust towards noise and _post region duplication process_

### How do we modify them?

We know that Duplication detection algorithm (Paper 1) has `coordinate` and `principal_component` features, and then on Robust detection algorithm (Paper 2) it has `coordinate` and `seven_features` mentioned inside the paper.

Knowing that, we then attempt to give a tolerance by adding all of the features like so:

![Modification diagram](/assets/modification_diagram.PNG?raw=true) 

and then sort it lexicoghrapically.

The principal component will bring similar block closer, while the seven features will also bring closer similar block that can't be detected by principal component (that are for example blurred).

By modifying the algorithms like mentioned above, this script will have a tolerance regarding variety of the input image (i.e. the result will be both smooth and robust, with a trade-off in run time)

This project was used for my Undergraduate Thesis that you can find it in [here](http://repository.its.ac.id/1801/), but please note that it was written in Indonesian.

## Example image
### Original image
![Original image](/assets/dataset_example.png?raw=true) 
### Forgered image
![Forgered image](/assets/dataset_example_blur.png?raw=true)
### Example result after detection
![Result image](/output/20191125_094809_lined_dataset_example_blur.png)

## GUI
![GUI screenshoot](/assets/gui_result.PNG?raw=true)

**Note**: This version does not support GUI. If you want to implement it, you can visit the old repo mentioned above for the snippets.

## Getting Started

Assuming you already have Python 3.x on your machine:
- clone this repo
- create a [virtual environment](https://docs.python.org/3/library/venv.html) and enter into it
- run `pip3 install -r requirements.txt`

## Example

```python3
from copy_move_detection import detect
detect.detect('assets/', 'dataset_example_blur.png', 'output/', block_size=32)
```

If _blockSize_ parameter was not given, the default value would be 32 (integer).

You can also see directly at the [code](examples/example_01.py).

## License
This project is licensed under the MIT License - see the [LICENSE.md](/LICENSE) file for details

## Acknowledgments
I mainly learnt how to do PCA on image using Python from [here](http://www.janeriksolem.net/2009/01/pca-for-images-using-python.html) written by Jan Erik Solem, but the page has been erased. Shortly after knowing the page was gone, I found that the author are now founder & CEO at [Mapillary](https://www.mapillary.com/) (Hail, and hat tip).

## Support

Hi! I got piles email of thanks regarding how this code help them on their affairs or getting their Degree :) 

Maintain the repository took time and effort, if you want to support me, please consider <a href="https://www.buymeacoffee.com/EyWFfgS" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
