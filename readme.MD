# drf-fileupload-example
Sample example of multiple file upload using drf

mkvirtualenv --python=/usr/bin/python3 django-rest-photo-uploader
git clone git@github.com:ashraful-ic/drf-multi-fileupload.git
cd drf-multi-fileupload
pip install -r requirements.txt 
python projectile/manage.py migrate
python projectile/manage.py runserver

* To test endpoint *

curl  -H "Accept: application/json" -F 'images=@/home/ashraful/Pictures/sc_1.png' -F 'images=@/home/ashraful/Pictures/sc_2.png' -F name='BMW'  http://127.0.0.1:8000/marketplace/
