from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=500)
    blog_text = models.TextField()
    img = models.ImageField(upload_to="blog_images")

    def __str__(self) -> str:
        return self.title
    

