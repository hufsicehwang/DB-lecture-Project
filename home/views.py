from typing import Generator
from typing_extensions import Required
from django.http.request import HttpRequest
from django.shortcuts import render
from urllib.request import urlopen , Request
from .models import *
import re
import json
import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
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
@csrf_exempt
def searchMovie(request):
    if request.method=="POST":
        req = request.body.decode('utf-8')
        print(req)
        my_response = list(MovieList.objects.filter(movieNm=req).values())
        print(my_response)
        return HttpResponse((my_response))
        