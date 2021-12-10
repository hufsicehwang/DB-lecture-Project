from typing import Generator
from typing_extensions import Required
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from urllib.request import urlopen , Request
from main.models import User
from .models import *
import re
import json
from django.core.paginator import Paginator, EmptyPage
def review(request):
    if request.method =="GET":
        # print(detail_getJson)
        # genres = MovieDetailList.objects.get(id=2)
        # # gg = re.sub("\[|\]|\{|\}|\'|\:|\ ","",genres.genres).split(",")
        # # for i in range(0,len(gg)):
        # #     print(gg[i][7:])
        # # print(gg)

        # gg = re.sub("\[|\]|\{|\}|\'|\:|\ |\,","",genres.genres).split("genreNm")
        # print(gg[1])
        return render(request,'review.html')
    elif request.method=="POST":
        print(request.POST)
        name = request.POST.get('name')
        open1 = request.POST.getlist('open')
        nonopen1 = request.POST.getlist('non-open')
        message = request.POST.get('message')
        print(name, open1, nonopen1, message,"!!!!!!!!!")
        return render(request,'review.html')
def data_insert(request):
    if request.method == "GET":
        url = "https://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=002ee3abcc24ccf55fe7d7c47c76894f&itemPerPage=100"
        detail_url = "https://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=002ee3abcc24ccf55fe7d7c47c76894f"
        for j in range(598,852):
            request = Request(url+"&curPage="+str(j))
            
            response_body = urlopen(request).read()
            # print(response_body)
            getJson = json.loads(response_body)["movieListResult"]["movieList"]
            for i in range(0,len(getJson)):
                list = getJson[i]
                print(list)
                #기본 정보 저장
                movie = MovieList(movieNm=list["movieNm"],genreAlt=list["genreAlt"],prdtYear=list["prdtYear"],nationAlt=list["nationAlt"])
                movie.save()
                #상세 정보 저장
                detail_request= Request(detail_url+"&movieCd="+list["movieCd"])
                detail_response_body = urlopen(detail_request).read()
                detail_getJson = json.loads(detail_response_body)['movieInfoResult']["movieInfo"]
                detail_getJson_genres = detail_getJson["genres"]
                detail_movie = MovieDetailList(movieNm=detail_getJson["movieNm"],showTm=detail_getJson["showTm"],prdtYear=detail_getJson["prdtYear"],openDt=detail_getJson["openDt"],nations=detail_getJson["nations"],genres=detail_getJson_genres,audits=detail_getJson["audits"])
                detail_movie.save()
                
        return render(request,'review.html')



def home(request):
    res_data = {}
    user_session = request.session.get('user')              # 로그인 체크
    if user_session:
        user = User.objects.get(pk=user_session)

        if request.method == 'GET':
            return render(request, 'home.html', res_data)
        elif request.method == 'POST':
            return render(request, 'home.html', res_data)
    else:
        return redirect('/main/login')

def list(request):
    res_data = {}
    user_session = request.session.get('user')              # 로그인 체크
    if user_session:
        user = User.objects.get(pk=user_session)

        page = request.GET.get("page",1)
        all_list = Notice.objects.all().order_by('-writed_date')
        paginator = Paginator(all_list,100,orphans=5)
        try:
            notice = paginator.page(int(page))
        except EmptyPage:
            pass
        res_data["page"] = notice

        if request.method == 'GET':
            return render(request, 'list.html', res_data)
        elif request.method == 'POST':
            return render(request, 'list.html', res_data)
    else:
        return redirect('/main/login')

def mylist(request):
    res_data = {}
    user_session = request.session.get('user')              # 로그인 체크
    if user_session:
        user = User.objects.get(pk=user_session)

        page = request.GET.get("page",1)
        all_list = MovieNote.objects.filter(email =user.email).order_by('-writed_date')
        paginator = Paginator(all_list,100,orphans=5)
        try:
            notice = paginator.page(int(page))
        except EmptyPage:
            pass
        res_data["page"] = notice
        res_data["username"] = user.username
        if request.method == 'GET':
            return render(request, 'mylist.html', res_data)
        elif request.method == 'POST':
            return render(request, 'mylist.html', res_data)
    else:
        return redirect('/main/login')

def detail(request,pk):
    res_data = {}
    user_session = request.session.get('user')              # 로그인 체크
    if user_session:
        user = User.objects.get(pk=user_session)
        notice = Notice.objects.get(pk=pk)
        
        res_data["title"] = notice.movieNm
        res_data["review"] = notice.review
        res_data["star"] = notice.star
        res_data["writer"] = notice.username
        res_data["writed_date"] = notice.writed_date

        movie = MovieList.objects.get(movieNm=notice.movieNm)
        res_data["genre"] = movie.genreAlt
        movieD = MovieDetailList.objects.get(movieNm=notice.movieNm)
        res_data["Syear"] = movieD.prdtYear
        res_data["Oyear"] = movieD.openDt
        res_data["time"] = movieD.showTm
        res_data["age"] = movieD.audits

        if request.method == 'GET':
            return render(request, 'detail.html', res_data)
        elif request.method == 'POST':
            return render(request, 'home.html', res_data)
    else:
        return redirect('/main/login')

        