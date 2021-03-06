"""
Django settings for hz_BI project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+)@33%c3*6kl0^no-8m)-ji5yih8zqh%%)#n6$!muad5e_*u(-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # 'suit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'index',# bi系统展示的页面
    'uprofile',# 用户信息拓展
    'yoback',# 后台 上传excel 读取并写入数据库
    'hzyg',# 禾中优供数据库数据读取
    'yotools',# 辅助工具 短信验证
]

#api框架
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],

        # 'rest_framework.pagination.LimitOffsetPagination',# ？？？
        # 'rest_framework.pagination.PageNumberPagination',# ？？？
}

# username、邮箱、手机等作为用户名来登录
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',# 标准username验证登录
    'uprofile.authentication.EmailAuthBackend',# 邮箱作为用户名登录
    'uprofile.authentication.CellphoneAuthBackend',# 手机号作为用户登录
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hz_BI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates') ,],
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

WSGI_APPLICATION = 'hz_BI.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': '2531',
        'HOST': '192.168.117.110',
        'PORT': '3306',
        'NAME': 'hz_bi',
    },
    # 迁徙备份的数据库，可做查询
    'hzyg':{
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'malin',
        'PASSWORD': 'hzbl@123@malin',
        'HOST': '47.92.133.25',
        'PORT': '3306',
        'NAME': 'dxh_b2b',
    }
}

SESSION_COOKIE_AGE = 60 * 2 # 2分钟
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True # 关闭浏览器，则COOKIE失效


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans' # 中文

TIME_ZONE = 'Asia/Shanghai' # 上海时区

USE_I18N = True

USE_L10N = False

USE_TZ = False # 选择Fasle使修改TIME_ZONE的时区生效。

# 静态文件配置
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static') # 部署时需要使用

# 文件、图片上传路径
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# django-suit 时间bug
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'

SUIT_CONFIG = {
    'ADMIN_NAME': '禾中BI后台管理',
    'LIST_PER_PAGE': 10,
}
