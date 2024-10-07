from django.conf import settings

# Manually configure settings
settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',  # You can change this to your preferred DB engine
            'NAME': 'mydatabase',
        }
    },
    INSTALLED_APPS=[
        'django.contrib.contenttypes',  # Add required apps here
        'django.contrib.auth',
    ]
)

# After setting up configurations
import django
django.setup()
