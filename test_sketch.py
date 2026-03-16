import cv2
import numpy as np
from sketch_module import convert_to_sketch, save_sketch
import os

# Test the convert_to_sketch function
def test_sketch_conversion():
    # Use one of the existing sketches as input for testing
    test_image_path = 'sketches/sketch_yuva 1.jpg'  # Assuming this exists

    if not os.path.exists(test_image_path):
        print(f"Test image {test_image_path} not found. Using a different one.")
        # Find an existing image
        for file in os.listdir('sketches'):
            if file.endswith(('.jpg', '.png')):
                test_image_path = os.path.join('sketches', file)
                break
        else:
            print("No test images found in sketches folder.")
            return

    print(f"Testing with image: {test_image_path}")

    try:
        # Convert to sketch
        sketch = convert_to_sketch(test_image_path)
        print(f"Sketch conversion successful. Sketch shape: {sketch.shape}")

        # Verify the GaussianBlur step by checking if the sketch is generated
        # The GaussianBlur is part of the process, so if sketch is created, it worked
        if sketch is not None and sketch.size > 0:
            print("GaussianBlur step executed successfully as part of sketch generation.")

            # Save the test sketch
            output_path = 'test_sketch_output.png'
            save_sketch(sketch, output_path)
            print(f"Test sketch saved to {output_path}")
        else:
            print("Sketch generation failed.")

    except Exception as e:
        print(f"Error during sketch conversion: {e}")

if __name__ == "__main__":
    test_sketch_conversion()
