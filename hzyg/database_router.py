from django.conf import settings

DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING

# 使用方法
# YourModel.objects.using('db1').all()
# 或者 YourModel.objects.using('db2').all()

class DatabaseRouter(object):
    '''
        database路由
    '''
    def db_for_read(self, model, **hints):
        """"Point all read operations to the specific database."""
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    # def db_for_write(self, model, **hints):
    #     """Point all write operations to the specific database."""
    #     if model._meta.app_label in DATABASE_MAPPING:
    #         return DATABASE_MAPPING[model._meta.app_label]
    #     return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation between apps that use the same database."""
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     if db in DATABASE_MAPPING.values():
    #         return DATABASE_MAPPING.get(app_label) == db
    #     elif app_label in DATABASE_MAPPING:
    #         return False
    #     return None

