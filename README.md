# package_name

Description. 
The package package_name is used to:
	Processing:
		- Register: Receives two images paths and generate the data to third being the register of the first over the second.
		- Transform: Resize the image.
	Utils:
		- Read image
		- Save image
		- Plot images and results.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
pip install register_package
```

## How To Use
To use this package you must need a 2 images.

To get the parameter to plot the registration and view you must be import the package
```python
from image_register_package.processing import register
from image_register_package.utils import io, plot
``` 
With the code import you can get the key points of the first and second image. This key points are used to 
alignment the images and made the registration. With them we can produce the matches, the matches are the connections of key points.

You can get the destination (dst) and source(src), src means the original image, and dst is the image want to register. So basically the src are the coordinates of origin image and dst is the coordinates of destiny images.
```python
keypoints1, keypoints2, matches, dst, src = register.transform(image1_path, image2_path)
``` 

To plot the images is easy with the code.

plot_matches function made the matches of the key points.

plot_register_image functions plot the original image, the second image and the register image.
```python
plot.plot_matches(image1_path=image1_path, image2_path=image2_path, keypoints1=keypoints1,
                  keypoints2=keypoints2, matches = matches)

plot.plot_register_image(image1_path=image1_path, image2_path=image2_path, src=src, dst=dst)
``` 


## Author
Davi Rodrigues Pultrini


## License
[MIT](https://choosealicense.com/licenses/mit/)