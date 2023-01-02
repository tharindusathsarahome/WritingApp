# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))
    
    PUBLISHABLE_KEY='pk_test_TYooMQauvdEDq54NiTphI7jx' 
    SECRET_KEY_S='sk_test_4eC39HqLyjWDarjtT1zdp7dc'
    # Set up the App SECRET_KEY
    # SECRET_KEY = config('SECRET_KEY'  , default='S#perS3crEt_007')
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_007')

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')    
    
    # https://beta.openai.com/account/api-keys
    OPENAI_API_KEY = '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'# Open ai key
    
    
    # Email UserID & APP Password(otp code)
    # https://myaccount.google.com/u/1/security
    EMAIL_ID = "ishan2017kanchana@gmail.com" #UserID
    EMAIL_APP_PASSWORD ="dtfojxsahxjgskzo" #APP Password
    
    # GOOGLE CLIENT ID (google login)
    # https://console.cloud.google.com/apis/credentials?authuser=1&project=esoteric-pad-334905
    # http://127.0.0.1:5000/callback
    
    GOOGLE_CLIENT_ID = "501298001027-puskcu3jk2v29ke6mkljd50kdimegm5q.apps.googleusercontent.com" # CLIENT ID 
    
    # stripe payment gateway API key
    # https://dashboard.stripe.com/login
    PAYMENT_API_KEY = '' # stripe API key
    
    # admin user
    ADMIN_USER = 'ishan2017kanchana@gmail.com'
    
class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        os.getenv('DB_ENGINE'   , 'mysql'),
        os.getenv('DB_USERNAME' , 'appseed_db_usr'),
        os.getenv('DB_PASS'     , 'pass'),
        os.getenv('DB_HOST'     , 'localhost'),
        os.getenv('DB_PORT'     , 3306),
        os.getenv('DB_NAME'     , 'appseed_db')
    ) 

class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}

