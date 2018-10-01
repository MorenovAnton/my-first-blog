from django.db import models
from django.utils import timezone


class Post(models.Model): # — строка определяет нашу модель (объект). class — ключевое слово для определения объектов. Post — это имя нашей модели, 
							# мы можем поменять его при желании. models.Model означает, что объект Post является моделью Django, 
	# Далее задаем свойства нашей модели                                            # так Django поймет, что он должен сохранить его в базу данных.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)   # models.ForeignKey — ссылка на другую модель.
    title = models.CharField(max_length=200) # models.CharField — так мы определяем текстовое поле с ограничением на количество символов.
    text = models.TextField() # models.TextField — так определяется поле для неограниченно длинного текста. Выглядит подходящим для содержимого поста, верно?
    created_date = models.DateTimeField(                  #models.DateTimeField — дата и время.
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):  # метод публикации для записи, о котором мы говорили. def означает, что создаётся функция/метод, а publish — это название этого метода
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title 