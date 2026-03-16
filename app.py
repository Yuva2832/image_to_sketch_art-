from flask import Flask, request, jsonify, send_file, render_template_string
from sketch_module import convert_to_sketch, save_sketch
import os
import tempfile

app = Flask(__name__, static_folder='static')

UPLOAD_FOLDER = 'uploads'
SKETCH_FOLDER = 'sketches'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(SKETCH_FOLDER):
    os.makedirs(SKETCH_FOLDER)

@app.route('/')
def home():
    with open('index.html', 'r') as f:
        html_content = f.read()
    return render_template_string(html_content)

@app.route('/convert', methods=['POST'])
def convert_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image selected'}), 400

    # Save the uploaded image temporarily
    temp_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(temp_path)

    try:
        # Convert to sketch
        sketch = convert_to_sketch(temp_path)

        # Save the sketch
        sketch_filename = f"sketch_{file.filename}"
        sketch_path = os.path.join(SKETCH_FOLDER, sketch_filename)
        save_sketch(sketch, sketch_path)

        # Return the sketch file
        return send_file(sketch_path, mimetype='image/png')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Clean up the uploaded file
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == '__main__':
    app.run(debug=True)
