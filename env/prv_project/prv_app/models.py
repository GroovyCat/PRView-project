from django.db import models

# Create your models here.

class Url_data(models.Model):
    url_text = models.CharField(max_length = 200, verbose_name = 'URL', blank = True, primary_key=True, null=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.url_text

    class Meta:
        verbose_name_plural = '옥션 상품 URL'

class Movie_data(models.Model):
    movie_text = models.CharField(max_length = 50, verbose_name = 'Movie', blank = True, primary_key=True, null=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.movie_text
    
    class Meta:
        verbose_name_plural = '네이버 영화명'