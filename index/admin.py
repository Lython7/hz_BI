from django.contrib import admin

# Register your models here.
# 后台django管理名字修改
admin.site.site_header = "禾中BI管理后台"


class News_center_Admin(admin.ModelAdmin):
    list_display = ('news_title', 'news_time', 'created_time', 'created_by', )
    search_fields = ('news_title', 'news_time', 'created_time', 'created_by', )
    ordering = ('created_time',)
    list_per_page = 20


class Recruitment_info_Admin(admin.ModelAdmin):
    list_display = ('working_area', 'position_name', 'created_time', 'created_by',)
    search_fields = ('working_area', 'position_name', 'created_time', 'created_by',)
    ordering = ('created_time',)
    list_per_page = 20


# admin.site.register(News_center, News_center_Admin)
# admin.site.register(Recruitment_info, Recruitment_info_Admin)