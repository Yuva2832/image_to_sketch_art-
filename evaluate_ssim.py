import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np

def evaluate_sketch_accuracy(original_path, sketch_path):
    """
    Evaluate the accuracy of the sketch compared to the original image using SSIM.

    Args:
        original_path (str): Path to the original image.
        sketch_path (str): Path to the sketch image.

    Returns:
        float: SSIM score between 0 and 1, where 1 is perfect similarity.
    """
    # Read images
    original = cv2.imread(original_path)
    sketch = cv2.imread(sketch_path)

    # Convert to grayscale if needed
    if len(original.shape) == 3:
        original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    else:
        original_gray = original

    if len(sketch.shape) == 3:
        sketch_gray = cv2.cvtColor(sketch, cv2.COLOR_BGR2GRAY)
    else:
        sketch_gray = sketch

    # Resize images to the same size if necessary
    if original_gray.shape != sketch_gray.shape:
        sketch_gray = cv2.resize(sketch_gray, (original_gray.shape[1], original_gray.shape[0]))

    # Calculate SSIM
    score, _ = ssim(original_gray, sketch_gray, full=True)
    return score

if __name__ == "__main__":
    # Example usage
    original = 'sketches/sketch_yuva 1.jpg'
    sketch = 'test_sketch_output.png'
    accuracy = evaluate_sketch_accuracy(original, sketch)
    print(f"Sketch accuracy (SSIM): {accuracy:.4f} ({accuracy*100:.2f}%)")
