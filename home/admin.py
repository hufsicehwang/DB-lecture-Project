from django.contrib import admin

from home.models import MovieList
from home.models import MovieDetailList

# Register your models here.
class MovieListAdmin(admin.ModelAdmin):
    list_display=('id', 'movieNm','genreAlt','prdtYear','nationAlt')

admin.site.register(MovieList,MovieListAdmin)

class MovieDetailListAdmin(admin.ModelAdmin):
    list_display=('id','movieNm','prdtYear','openDt','showTm','nations','audits','genres')

admin.site.register(MovieDetailList,MovieDetailListAdmin)