from django.contrib import admin

# Register your models here.

#下の２行を追加
# from アプリケーション名.models import マイグレーションのクラス名
from .models import Test
from .models import User
admin.site.register(Test)
admin.site.register(User)

