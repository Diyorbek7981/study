from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avas/',blank=True,null=True)
    bio = models.TextField('Bio',blank=True,null=True)



class Category(models.Model):
    cat_name = models.CharField(max_length=150)

    def __str__(self):
        return self.cat_name

    #Bu Meta funksialari bn ishlovchi klas
    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
        ordering = ["cat_name"]



class RommModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    #categoriya obektlarini boglash
    category = models.ForeignKey(Category,on_delete=models.PROTECT,null=True)
    participants = models.ManyToManyField(User, related_name='ptns',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created','-update']

    def __str__(self):
        return self.title



class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(RommModel,on_delete=models.CASCADE)
    message = models.TextField()
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    res_active = models.BooleanField(verbose_name='Resent Active', default=True)

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.message[0:50]