# Copy-Move Detection on Digital Image using Python

Hi! I got piles of emails of thanks regarding how this code help them on their affairs or getting their Degree :)

If you want to support me, you can <a href="https://www.buymeacoffee.com/EyWFfgS" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a> so I can keep this repository maintained :)

### Udpdate
**Update 18 Oct 2019**: I believe it is time to rewrite and optimize on python 3! Currenlty WIP :)

**Update**: I just released english version for english reader! You can have it via [Release tag](https://github.com/rahmatnazali/image-copy-move-detection/releases/tag/English_Version) or by pulling the newest code.


## Description
This is an implementation of python script to detect a copy-move manipulation attack on digital image based on Overlapping Blocks.

This script is implemented with a modification of two algoritms publicated in a scientific journals:
1. Duplication detection algorithm, taken from [Exposing Digital Forgeries by Detecting Duplicated Image Region](http://www.ists.dartmouth.edu/library/102.pdf); Fast and smooth attack detection algorithm on digital image using [principal component analysys](https://en.wikipedia.org/wiki/Principal_component_analysis), but sensitive to noise and _post region duplication process_ (explained in the paper above)
2. Robust detection algorithm, taken from [Robust Detection of Region-Duplication Forgery in Digital Image](http://ieeexplore.ieee.org/document/1699948/); Slower and having rough result attack detection algorithm but are considered robust towards noise and _post region duplication process_

By modify those algorithm, this script will have a tolerance regarding variety of the input image (i.e. the result will be both smooth and robust, with a trade-off in run time)

This project was used for my Undergraduate Thesis that you can find it in [here](http://repository.its.ac.id/1801/), but please note that it was written in Indonesian.

## Example of original and forgered image
### Original image
![Original image](/screenshot/horse.png?raw=true) 
### Forgered image
![Forgered image](/screenshot/horse_blur.png?raw=true)

## GUI
![GUI screenshoot](/screenshot/02_home_result.PNG?raw=true)

By default, the script will log entire detection process like so:
![Log screenshoot](/screenshot/03_log.PNG?raw=true)


## Getting Started
Make sure you already have:
* [Python 2.7](https://www.python.org/)
* [Anaconda](https://www.anaconda.com/)

Also the required python libraries:
* [Numpy](https://pypi.python.org/pypi/numpy)
* [SKLearn/scikit-learn](https://pypi.python.org/pypi/scikit-learn/0.18.1)
* [Python Image Library (PIL)](https://pypi.python.org/pypi/PIL)
* [Scipy](https://pypi.python.org/pypi/scipy/0.7.0)
* [tqdm](https://pypi.python.org/pypi/tqdm)

## Starting
### Running GUI version
1. Run [main_GUI.py](/copy_move_detection_python_2/main_GUI.py)
2. A new window will apear, click open file and choose your image
3. Click detect and the detection process will start
4. After done, the detection result will be written in your CLI, while the result image will be shown in GUI
### Running CLI version
By default, you can run it using [main_CLI.py](/copy_move_detection_python_2/main_CLI.py).
But you can also modify it, or even make your own python script with the format below:
1. Make sure to import ```CopyMoveDetection``` package
2. Directly call function ```detect``` or ```detect_dir``` and give the proper parameter

Your scirpt will likely looks like so:
```
import CopyMoveDetection

# To detect all images on a single folder, use detect_dir function
CopyMoveDetection.detect_dir('your/directory/path/', 'your/result/directory/' [, blockSize])

# To detect single image on a certain path, use detect function
CopyMoveDetection.detect('your/directory/path/', 'your_image.png', 'your/result/directory/' [, blockSize])
```
If _blockSize_ parameter was not given, the default value would be 32 (integer).

  
## Built With
* [Python 2.7](https://www.python.org/) - Base language
* [Anaconda 4.3.1](https://www.continuum.io/downloads) - Python data science package
* [Pycharm 4.5.5](https://confluence.jetbrains.com/display/PYH/Previous+PyCharm+Releases) - IDE

## Authors
* **Rahmat Nazali S** - [LinkedIn](https://www.linkedin.com/in/rahmat-nazali-s-43391a13b/)
* **Hudan Studiawan** (Undergraduate Thesis Adviser) - [Github](https://github.com/studiawan)

## License
This project is licensed under the MIT License - see the [LICENSE.md](/LICENSE) file for details

## Acknowledgments
I mainly learnt how to do PCA on image using Python from [here](http://www.janeriksolem.net/2009/01/pca-for-images-using-python.html) written by Jan Erik Solem, but the page has been erased. Shortly after knowing the page was gone, I found that the author are now founder & CEO at [Mapillary](https://www.mapillary.com/) (Hail, and hat tip).
