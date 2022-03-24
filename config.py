import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-a-secret' #Figure out how to hide this
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'websiteProject.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTh = 1024 * 1024
    UPLOAD_EXTENSIONS = ['.csv', '.docx']
    UPLOAD_FOLDER = '/Uploads'
    FILE_TYPES = ['.csv'] #temp