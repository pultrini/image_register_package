import matplotlib.pyplot as plt
from skimage.transform import AffineTransform, warp, resize
from skimage.feature import ORB, match_descriptors, plot_matches
from skimage.measure import ransac

def plot_matches(image1_path, image2_path, keypoints1, keypoints2):
    assert isinstance(image1_path, str), "The Image 1 path it must be String."
    assert isinstance(image2_path, str), "The Image 2 path it must be String."
    
    image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    
    assert image1 is None or image2 is None, "One or Both images failed to load. Check the file."
    
    image1 = resize(image1, (500,500), anti_aliasing=True)
    image2 = resize(image2, (500,500), anti_aliasing=True)
    
    fig, ax = plt.subplots(1,1, figsize = (12,6))
    plt.gray()
    
    plot_matches(ax, image1, image2, keypoints1, keypoints2)
    ax.axis("off")
    ax.set_title("Keypoints Matches")
    plt.show()
    
    if len(matches) < 4:
        raise ValueError("Not enough matches to compute a reliable transformation")
    
def plot_register_image(image1_path, image2_path, src, dst):
    assert isinstance(image1_path, str), "The Image 1 path it must be String."
    assert isinstance(image2_path, str), "The Image 2 path it must be String."
    
    image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    
    assert image1 is None or image2 is None, "One or Both images failed to load. Check the file."
    
    image1 = resize(image1, (500,500), anti_aliasing=True)
    image2 = resize(image2, (500,500), anti_aliasing=True)
    
    model_robust, inliers = ransac((dst, src), AffineTransform, min_samples=4, residual_threshold=2, max_trials=1000)
    
    register_image = warp(image1, model_robust.inverse, output_shape=image2.shape)
    
    plt.figure(figsize=(12,6))
    plt.subplot(1,3,1)
    plt.title("Image 1")
    plt.imshow(image1, cmap='gray')
    
    plt.figure(figsize=(12,6))
    plt.subplot(1,3,2)
    plt.title("Image 2")
    plt.imshow(image2, cmap='gray')
    
    plt.figure(figsize=(12,6))
    plt.subplot(1,3,3)
    plt.title("Image Register")
    plt.imshow(register_image, cmap='gray')
    
    plt.show()
    
    
    
    
    