from django.db import models

class MovieList(models.Model):
    id = models.AutoField(primary_key=True)
    movieNmEn = models.TextField(verbose_name="movieNmEn")#제목
    genreAlt = models.TextField(verbose_name="genreAlt")#장르
    predtYear = models.TextField(verbose_name="predtYear")#개봉일
    nationAlt = models.TextField(verbose_name="nationAlt")#개봉나라
    
    