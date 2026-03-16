# Image to Sketch Converter

An AI-based system that converts digital images into pencil sketch versions using computer vision and deep learning techniques.

## Features

- Automated sketch creation process
- Web-based interface for easy image upload
- Real-time conversion using OpenCV
- Downloadable sketch results

## Technologies Used

- **Backend**: Python, Flask, OpenCV, NumPy
- **Frontend**: HTML, CSS, JavaScript
- **Libraries**: OpenCV for image processing, Flask for web server

## Installation

1. Clone the repository:
   ```
  git clone https://github.com/Yuva2832/image_to_sketch_art-.git
   cd image_to_sketch_art-
   ```

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Upload an image using the file input on the web interface
2. Click "Convert to Sketch" to process the image
3. View and download the generated sketch

## How It Works

The system processes input images through the following steps:

1. **Grayscale Conversion**: Convert the image to grayscale
2. **Noise Reduction**: Apply Gaussian blur to smooth details
3. **Image Inversion**: Invert the blurred image
4. **Division**: Divide grayscale by inverted blurred image to create sketch effect

## Project Structure

```
image_to_sketch_art-/
├── app.py                 # Flask application
├── sketch_module.py       # Image processing functions
├── requirements.txt       # Python dependencies
├── index.html            # Web interface
├── uploads/              # Temporary upload directory
└── sketches/             # Generated sketches directory
```

## Advantages

- Fully automated sketch generation
- Fast and efficient processing
- High accuracy results
- No manual editing required

## Applications

- Digital art and design
- Cartoon creation
- Image editing tools
- AI-based creative platforms

## Future Enhancements

- Color sketch generation
- Style-based sketching with deep learning
- Mobile app version
- Real-time camera-based sketch generation

## License

This project is open-source and available under the MIT License.
