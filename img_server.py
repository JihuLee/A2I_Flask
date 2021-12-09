from flask import Flask, render_template, request
import pandas as pd
import cv2
import numpy as np
import base64
from PIL import Image
from io import BytesIO
import os
import matplotlib
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename

#matplotlib.use('TkAgg')

app = Flask(__name__)
path = './hololens/'

@app.route('/hololens', methods=['GET', 'POST'])
def add_face():
    if request.method == 'POST':
        # read encoded image
        #imageString = base64.b64decode(request.form['img'])
        filename = request.form['name']
        h = request.form['height']
        w = request.form['width']
        #print(imageString)
        
        img = Image.open(BytesIO(base64.b64decode(request.form['img'])))
        
        # convert binary data to numpy array
        #nparr = np.fromstring(imageString, np.uint8)
        #print(nparr)
        #print(len(nparr))
        
        # opencv: decode image
        #img = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR);
        #cv2.imshow("frame", img)
        #cv2.waitKey(0)
        
        #Image.fromarray(nparr).save(request.form['img'].filename)
        #img = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)
        #nparr = np.reshape(nparr, (w, h))
        #cv2.imwrite(path+filename+'.jpeg', nparr)
        #cv2.imwrite('/hololens/test.jpeg', nparr)
        #cv2.imwrite(path+filename+'.jpeg', nparr)
        #cv2.imwrite(path+filename+'.jpeg', img)
        img.save(path+filename+'.jpg')
        
        #plt.imshow(img)
        #plt.show()
        
        #cv2.imshow("frame", img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        
    return "hololens sucks"

if __name__ == "__main__":
    app.run(debug=True, 
            host="192.168.0.40", 
            port=5000)
        