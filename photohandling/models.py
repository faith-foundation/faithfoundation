from django.db import models

# Create your models here.


class album_1(models.Model):
    album_name = models.CharField(max_length=150)
    album_date = models.DateTimeField()
    album_cover = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.album_name

class album_2(models.Model):
    album_name = models.CharField(max_length=150)
    album_date = models.DateTimeField()
    album_cover = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.album_name

class album_3(models.Model):
    album_name = models.CharField(max_length=150)
    album_date = models.DateTimeField()
    album_cover = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.album_name

class album_4(models.Model):
    album_name = models.CharField(max_length=150)
    album_date = models.DateTimeField()
    album_cover = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.album_name

class album_5(models.Model):
    album_name = models.CharField(max_length=150)
    album_date = models.DateTimeField()
    album_cover = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.album_name

class album_6(models.Model):
    album_name = models.CharField(max_length=150)
    album_date = models.DateTimeField()
    album_cover = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.album_name

class album_7(models.Model):
    album_name = models.CharField(max_length=150)
    album_date = models.DateTimeField()
    album_cover = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.album_name

class album_8(models.Model):
    album_name = models.CharField(max_length=150)
    album_date = models.DateTimeField()
    album_cover = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.album_name


class album_9(models.Model):
    album_name = models.CharField(max_length=150)
    album_date = models.DateTimeField()
    album_cover = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.album_name


class album_10(models.Model):
    album_name = models.CharField(max_length=150)
    album_date = models.DateTimeField()
    album_cover = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.album_name

# Album code ends here

# Photos code starts here

class photo_album_1(models.Model):
    photo_title = models.CharField(max_length=150)
    photo_description = models.CharField(max_length=150)
    photo_date = models.DateTimeField()
    photo_1 = models.ImageField(upload_to='uploads/')
    photo_3 = models.ImageField(upload_to='uploads/')
    photo_4 = models.ImageField(upload_to='uploads/')
    photo_5 = models.ImageField(upload_to='uploads/')
    photo_6 = models.ImageField(upload_to='uploads/')
    photo_7 = models.ImageField(upload_to='uploads/')
    photo_8 = models.ImageField(upload_to='uploads/')
    photo_9 = models.ImageField(upload_to='uploads/')
    photo_10 = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.photo_title

