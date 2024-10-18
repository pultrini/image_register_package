# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import ORB, match_descriptors, plot_matches
from skimage.transform import AffineTransform, warp, resize
from skimage.measure import ransac

def transform(image1_path, image2_path):
    assert isinstance(image1_path, str), "The Image 1 path it must be String."
    assert isinstance(image2_path, str), "The Image 2 path it must be String."
    
    image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    #print(image1)
    
    #assert image1 is None, "One or Both images failed to load. Check the file paths."
    #assert image2 is None, "One or Both images failed to load. Check the file paths."
    
    image1 = resize(image1, (500,500), anti_aliasing=True)
    image2 = resize(image2, (500,500), anti_aliasing=True)
    
    orb = ORB(n_keypoints=500)
    
    orb.detect_and_extract(image1)
    keypoints1 = orb.keypoints
    descriptor1 = orb.descriptors
    
    
    orb.detect_and_extract(image2)
    keypoints2 = orb.keypoints
    descriptor2 = orb.descriptors
    
    matches = match_descriptors(descriptor1, descriptor2, cross_check=True)
    
    src = keypoints1[matches[:, 0]]
    dst = keypoints2[matches[:, 1]]
    
    print(f"Number of matches: {len(matches)}")
    
    return keypoints1, keypoints2, matches, dst, src

