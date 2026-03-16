from sketch_module import convert_to_sketch, save_sketch
import os

# Test with different image formats
def test_different_formats():
    test_images = [
        'sketches/sketch_yuva 1.jpg',  # JPG
        'sketches/sketch_Gemini_Generated_Image_ehjmztehjmztehjm.png',  # PNG
    ]

    for img_path in test_images:
        if os.path.exists(img_path):
            print(f"Testing format: {os.path.splitext(img_path)[1]} with {img_path}")
            try:
                sketch = convert_to_sketch(img_path)
                output_path = f"test_sketch_{os.path.basename(img_path)}"
                save_sketch(sketch, output_path)
                print(f"Success: Sketch saved to {output_path}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(f"Image not found: {img_path}")

if __name__ == "__main__":
    test_different_formats()
