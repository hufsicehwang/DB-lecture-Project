from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import User
# Create your views here.
def signUp(request):
    res_data = {}
    if request.method == 'GET':
        return render(request, 'signUp.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
   
        if not(email) or not(username) or not(password) or not(re_password):
            res_data['error'] = '모든 값을 입력해 주세요.'
            return render(request, 'signUp.html', res_data)

        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
            messages.warning(request, "비밀번호가 다릅니다.")
            return render(request, 'signUp.html', res_data)
        else:  # 아이디 중복 체크
            try:
                user = User.objects.get(email=email)    # 아이디가 있는지 확인 해보고
            except User.DoesNotExist:   # 아이디가 없어서 DoesNotExist이면 저장한다.
                user = User(email=email, username=username, password=make_password(password))
                user.save()
                return redirect('/login')
            if(user):
                res_data['error'] = '존재하는 Email 입니다.'
                return render(request, 'signUp.html', res_data)
