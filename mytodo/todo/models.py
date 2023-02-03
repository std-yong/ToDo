from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    #인스턴스 이름을 출력하는 메서드에 대입했을 때 호출되는 함수
    def __str__(self):
        return self.title