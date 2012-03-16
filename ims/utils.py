__author__ = 'agbetunsin'

import hashlib, settings
salt = settings.SECRET_KEY

def hash_password(password):
    return hashlib.sha224( salt + password ).hexdigest()