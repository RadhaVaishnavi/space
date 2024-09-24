from flask import Flask, render_template, request, redirect, url_for
from model.model import generate_caption
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        image = request.files['image']
        if image:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)
            caption = generate_caption(image_path)
            return render_template('result.html', caption=caption, image_url=image.filename)

if __name__ == '__main__':
    app.run(debug=True)

