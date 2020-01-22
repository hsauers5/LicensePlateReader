# LicensePlateReader
Requirements: Ubuntu 18.04, Python 3
####Setup:
```
git clone https://github.com/hsauers5/LicensePlateReader
cd LicensePlateReader
chmod +x setup.sh
./setup.sh
gunicorn --bind 0.0.0.0:5000 -w 8 wsgi:app
```

Alternately, 
```
git clone https://github.com/hsauers5/LicensePlateReader
cd LicensePlateReader

sudo pip3 install requirements.txt
sudo apt-get install libopencv-dev libtesseract-dev git cmake build-essential libleptonica-dev
sudo apt-get install liblog4cplus-dev libcurl3-dev
git clone https://github.com/openalpr/openalpr.git
cd openalpr/src
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc ..
make
sudo make install

cd ../../
cd src/bindings/python/
sudo python3 setup.py install
gunicorn --bind 0.0.0.0:5000 -w 8 wsgi:app
```