"""
Django settings for mysite project.
Generated by 'django-admin startproject' using Django 1.8.13.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# 该文件为工程的所有系统配置文件
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 默认路径设置

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7i8zh4hk_r(#p45zepu26dwlg86sp1$r+!oqd07j7p@j&_tnl6'
# Django应用的专有密钥，为创建应用时自动生成

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# 调试信息选项，也就是log日志，当前为开启
ALLOWED_HOSTS = []
# 允许访问的用户ip，当前为全部

# Application definition

INSTALLED_APPS = (
# 工程下声明的应用
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'haystack',
)

MIDDLEWARE_CLASSES = (
# 处理请求的关键代码，此处为自动生成
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mysite.urls'
# 默认的url解析器当前为mysite下的urls.py

TEMPLATES = [
# 模版路径，当前为默认，空，也就是当前的blog/template
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'
# 服务器配置信息，当前默认

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


DATABASES = {
# 数据库配置信息
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 数据库驱动，为mysql
        'NAME': 'vicker$mysite',
        'USER': 'vicker',
        'PASSWORD': '!QAZ2wsx',
        'HOST': 'vicker.mysql.pythonanywhere-services.com',
    }
}

# full text search
# 全文搜索配置，此处也为默认
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
# 默认语言

# TIME_ZONE = 'UTC'

TIME_ZONE = 'Asia/Shanghai'
# 默认时间时区

USE_I18N = True

USE_L10N = True

USE_TZ = True
# 以上三处为默认

LOGIN_REDIRECT_URL = '/'
# 登录选项，此处为默认

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
# 静态文件路径，blog下的static文件夹

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# 静态文件目录，同上
