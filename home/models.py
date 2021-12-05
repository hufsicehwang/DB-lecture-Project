from django.db import models

class MovieList(models.Model):
    id = models.AutoField(primary_key=True)
    movieCd=models.TextField(verbose_name="movieCd", default='0')
    movieNm = models.TextField(verbose_name="movieNmEn")#제목
    genreAlt = models.TextField(verbose_name="genreAlt")#장르
    prdtYear = models.TextField(verbose_name="prdtYear")#개봉년도
    nationAlt = models.TextField(verbose_name="nationAlt")#개봉나라
class MovieDetailList(models.Model):
    id = models.AutoField(primary_key=True)
    movieNm = models.TextField(verbose_name="movieNmEn")#제목
    prdtYear = models.TextField(verbose_name="prdtYear")#개봉년도
    openDt=models.TextField(verbose_name="openDt")#개봉년도
    showTm = models.TextField(verbose_name="showTm")#상영시간
    nations = models.TextField(verbose_name="nations")#제작국가들
    genres = models.TextField(verbose_name="genres")#장르들
    audits=models.TextField(verbose_name="audits")#심의정보들
    

    
    