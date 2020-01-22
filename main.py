import cv2
import sys
from openalpr import Alpr

alpr = Alpr("us", "openalpr/config/openalpr.conf.defaults", "openalpr/runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(20)
alpr.set_default_region("fl")

'''
video = cv2.VideoCapture(0)
val, frame = video.read()
results = alpr.recognize_ndarray(frame)
'''
img = cv2.imread("img3.jpg")
frame = img
results = alpr.recognize_ndarray(frame)

print(results)

i = 0
for plate in results['results']:
    i += 1
    print("Plate #%d" % i)
    print("   %12s %12s" % ("Plate", "Confidence"))
    for candidate in plate['candidates']:
        prefix = "-"
        if candidate['matches_template']:
            prefix = "*"

        print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))

# Call when completely done to release memory
alpr.unload()
