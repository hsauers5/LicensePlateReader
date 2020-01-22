sudo pip3 install -r requirements.txt
sudo apt install -y libopencv-dev libtesseract-dev git cmake build-essential libleptonica-dev
sudo apt install -y liblog4cplus-dev libcurl3-dev
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