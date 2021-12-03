import os

# This defines the base dir for all relative imports for our project, put the file in your root folder so the
# base_dir points to the root folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# According to your data file, you can change the engine, like mysql, postgresql, mongodb etc make sure your data is
# directly placed in the same folder as this file, if it is not, please direct the 'NAME' field to its actual path.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shuttle_buddy',
        'USER': 'shuttlebuddy',
        'PASSWORD': 'shuttlebuddy',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
#Since we only have one app which we use
INSTALLED_APPS = (
    'shuttleBuddy',
)

# Write a random secret key here
SECRET_KEY = '4e&6aw+(5&cg^_!05r(&7_#d3cfd_pdgopq(yk)xa^bog7j)^*j'