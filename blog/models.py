from django.db import models
from django.db.models.fields import CharField, DateField, EmailField, TextField, SlugField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    email_address = EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"


class Post(models.Model):
    author = ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    title = CharField(max_length=150)
    excerpt = CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = DateField(auto_now=True)
    slug = SlugField(unique=True, db_index=True)
    tags = ManyToManyField(Tag)
    content = TextField(validators=[MinLengthValidator(10)])

class Comment(models.Model):
    user_name = CharField(max_length=120)
    user_email = EmailField()
    text = TextField(max_length=400)
    post = ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

