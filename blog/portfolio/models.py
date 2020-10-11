from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'images/')   # images라는 디렉토리에 넣는다.
    description = models.CharField(max_length = 500)   # 최대 500글자

    def __str__(self):   # admin사이트에 objectnumber 말고 title 뜨게 하고싶다.
        return self.title

# image 효율적으로 쓰기위해 