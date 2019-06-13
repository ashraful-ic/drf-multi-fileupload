# drf-fileupload-example # 

Sample example of multiple file upload using drf

**Run Following commands**

    mkvirtualenv --python=/usr/bin/python3 django-rest-photo-uploader
    git clone git@github.com:ashraful-ic/drf-multi-fileupload.git
    cd drf-multi-fileupload
    pip install -r requirements.txt 
    python projectile/manage.py migrate
    python projectile/manage.py runserver
    
**To Test API**

    curl  -H "Accept: application/json" -F 'images=@/file/path/1' -F 'images=@/file/path/2' -F name='name_of_car'  http://127.0.0.1:8000/marketplace/
