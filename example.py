# %%
from image_register_package.processing import register, transform
from image_register_package.utils import io, plot

# %%
image1_path = r'C:\Users\davip\Desktop\image_register_packege\image_register_package\livro1.png'
image2_path = r'C:\Users\davip\Desktop\image_register_packege\image_register_package\livro2.png'

keypoints1, keypoints2, matches, dst, src = register.transform(image1_path, image2_path)


# %%
plot.plot_register_image(image1_path=image1_path, image2_path=image2_path, src=src, dst=dst)
# %%
plot.plot_matches(image1_path=image1_path, image2_path=image2_path, keypoints1=keypoints1,
                  keypoints2=keypoints2, matches = matches)
