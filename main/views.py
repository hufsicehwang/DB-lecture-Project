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
                return redirect('/main/login')
            if(user):
                res_data['error'] = '존재하는 Email 입니다.'
                return render(request, 'signUp.html', res_data)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        res_data = {}   # 딕션어리 = key, value 값을 가지는 변수
        if not(email and password):
            res_data['error'] = '모든 값을 입력하세요.'
        elif not(email):
            res_data['error'] = '이메일을 입력하세요.'
        elif not(password):
            res_data['error'] = '비밀번호를 입력하세요.'
        else:
            try:
                user = User.objects.get(email=email)  # 필드명 = 값 이면 user 객체 생성
            except User.DoesNotExist:
                res_data['error'] = '존재하지 않는 아이디 입니다.'    # 아이디가 없는 예외 처리
                return render(request, 'login.html', res_data)

            user_password = user.password
            if check_password(password, user_password):
                request.session['user'] = user.id  # session 변수에 저장
                request.session['user_email'] = user.email  # session 변수에 저장
                return redirect('/home')
            else:
                res_data['error'] = '비밀번호가 틀렸습니다.'
                return render(request, 'login.html', res_data)
        return render(request, 'login.html', res_data)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/main/login')