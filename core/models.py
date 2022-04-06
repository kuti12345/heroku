from asyncio.windows_events import NULL
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Post(models.Model):
    class Meta:
        verbose_name="Post"
        verbose_name_plural="post"
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    desctiption=models.TextField()
    data=models.DateField()
    now_data=models.DateField(auto_now=True)
    visit=models.IntegerField(default=0)
    def __str__(self):
        return self.title
class Comment(models.Model):
    class Meta:
        verbose_name="Comment"
        verbose_name_plural="comment"
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    text=models.TextField()
    content=RichTextField(null=True,blank=True)
    image=models.ImageField(upload_to="media/category/",null=True,blank=True)
    def __str__(self):
        return self.author
        