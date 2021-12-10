from django.contrib import admin

from home.models import MovieList
from home.models import MovieDetailList
from home.models import MovieNote
from home.models import Notice

# Register your models here.
class MovieListAdmin(admin.ModelAdmin):
    list_display=('id', 'movieNm','genreAlt','prdtYear','nationAlt')

admin.site.register(MovieList,MovieListAdmin)

class MovieDetailListAdmin(admin.ModelAdmin):
    list_display=('id','movieNm','prdtYear','openDt','showTm','nations','audits','genres')

admin.site.register(MovieDetailList,MovieDetailListAdmin)

class MovieNoteAdmin(admin.ModelAdmin):
    list_display=('email','movieNm','review','star','open','writed_date')

admin.site.register(MovieNote,MovieNoteAdmin)

class NoticeAdmin(admin.ModelAdmin):
    list_display=('username','movieNm','review','star','writed_date')

admin.site.register(Notice,NoticeAdmin)