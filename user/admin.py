from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# 个人资料内联 StackedInline：堆叠式内联
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


# 用户管理，基于自带的用户管理 inlines:对个人资料的内联，已在上层定义
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('id', 'username', 'nickname', 'is_staff', 'is_active', 'email', 'is_superuser')

# 修改nickname的后台显示
    def nickname(self, obj):
        return obj.profile.nickname
    nickname.short_description = "昵称"


# 重新覆盖注册 USER管理模块
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# Register your models here.

# 自定义模块，来自Model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname')
