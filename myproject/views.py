from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .models import Test
from django import forms 
# from models import User

def index(request):
    sample_list = Test.objects.all()
    params = {"message_me": "Hello World"}
    # form = SampleForm(request.POST or None)
    context = {
        'sample_list':sample_list,
        'params':params,
    }
    # 変数設定
    
    # 出力
    if request.method == 'POST':
        user_name = is_private = request.POST.get('name', False)
        user_id = is_private = request.POST.get('id', False)
        Test.objects.create(
            test_name=user_name,
            tesetr_id=user_id,
        )
            # create()の場合
            # sample.objects.create(**form.cleaned_data)

            # save()の場合
            # sample = Sample(**form.cleaned_data)
            # sample.save
    return render(request,'App_Folder_HTML/index.html',context=context)

