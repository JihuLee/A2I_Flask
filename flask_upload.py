from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

# upload HTML rendering
@app.route('/upload')
def render_file():
    return render_template('upload.html')

# file upload
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.methods == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        
        return 'uploads directory -> file upload success!'
    
if __name__ == '__main__':
    app.run(debug = True)