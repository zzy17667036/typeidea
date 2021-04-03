#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author: ZZY time:2021/4/2

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

from .base import *    # NOQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
