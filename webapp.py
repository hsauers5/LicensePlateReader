from flask import Flask, jsonify, request, abort, render_template, Response
import cv2
import sys
import numpy as np
from openalpr import Alpr

alpr = Alpr("us", "openalpr/config/openalpr.conf.defaults", "openalpr/runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(20)
alpr.set_default_region("fl")


# return the most likely plate
def read_plate(nparray):
    results = alpr.recognize_ndarray(nparray)
    if len(results['results']) != 0:
        plate = results['results'][0]
        return plate
    else:
        abort(Response(response='Could not find a license plate.', status=400))


app = Flask(__name__, static_folder='.', static_url_path='', template_folder='')
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/', methods=['GET'])
def root():
    return "Welcome to the UCF Parking API. "


@app.route('/upload', methods=['POST'])
def upload():
    img = request.files.get('image').read()
    nparr = cv2.imdecode(np.fromstring(img, np.uint8), cv2.IMREAD_COLOR)
    my_plate = read_plate(nparr)
    
    resp = jsonify(my_plate['plate'])
    
    return resp
    
    
@app.route('/test', methods=['GET'])
def test():
    return render_template('upload.html')


# start listening
if __name__ == "__main__":
    app.run(debug=False, port='5000', host='0.0.0.0')
    

alpr.unload()

