import os

environment = os.getenv('ENVIRONMENT')

if environment is 'production':

    from .production_settings import *
else:
    try:
        from .local_settings import *
    except:
        pass
