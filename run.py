from flask import Flask, request, jsonify
from ml.model import generate_caption
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  # Serve the frontend HTML directly from Flask
  return app.send_static_file('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  if 'image' not in request.files:
    return jsonify({'error': 'No image file provided.'})

  file = request.files['image']
  if file.filename == '':
    return jsonify({'error': 'No image file selected.'})

  try:
    image = Image.open(file.stream)
    caption = generate_caption(image)
    return jsonify({'caption': caption})
  except Exception as e:
    return jsonify({'error': str(e)})

if __name__ == '__main__':
  app.run(debug=True)
