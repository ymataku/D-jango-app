from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # 変数設定
    params = {"message_me": "Hello World"}
    # 出力
    return render(request,'App_Folder_HTML/index.html',context=params)