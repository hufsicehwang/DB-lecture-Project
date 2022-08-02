from django.db import models

class User(models.Model):
    email = models.EmailField(verbose_name="이메일")
    username = models.TextField(verbose_name="이름")
    password = models.TextField(verbose_name="비밀번호")
    registerd_date = models.DateTimeField(auto_now_add=True, verbose_name='가입시간')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'
        verbose_name = '사용자 명단'
        verbose_name_plural = '사용자 명단'  # 복수명 설정