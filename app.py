import time
import os
import base64
from flask import Flask, render_template, request

app = Flask(__name__)
UPLOAD_FOLDER = 'snapshots'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    timestamp = int(time.time())  
    

    image_b64 = request.form.get('image')
    if image_b64:
        header, encoded = image_b64.split(",", 1)
        image_data = base64.b64decode(encoded)
        image_filename = f"snapshot_{timestamp}.png"
        with open(os.path.join(UPLOAD_FOLDER, image_filename), "wb") as f:
            f.write(image_data)

    # Save form data as text file
    name = request.form.get('name', 'Unknown').replace(' ', '_')
    email = request.form.get('email', 'Unknown')
    message = request.form.get('message', '')

    text_filename = f"{name}_{timestamp}_data.txt"
    filepath = os.path.join(UPLOAD_FOLDER, text_filename)

    with open(filepath, 'w') as f:
        f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n")

    return "Admission formed filled and saved properly"

if __name__ == '__main__':
    app.run(debug=True)
