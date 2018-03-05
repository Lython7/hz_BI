from django.contrib.auth.models import User

# 邮箱作为用户名登录验证
from.models import Uprofile


class EmailAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class CellphoneAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(pk=Uprofile.objects.get(ucellphone=int(username)).pk)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None