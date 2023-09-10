from django.db import models


# Create your models here.
class Todo(models.Model):

    class Meta:
        db_table = "todo_list"
    author = models.ForeignKey('users.UserModel', verbose_name="글쓴이", on_delete=models.CASCADE)
    title = models.CharField(max_length= 100)
    context = models.TextField(max_length= 1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    # 그냥 코드가 어드민에서 잘 돌아가는지 체크하는 boolean?
    image = models.ImageField(null=True,blank=True)
    # file = models.FileField(upload_to='file/',null=True,blank=True)
    def __str__(self): 
        return self.context #보여질 때 미리보기에 콘텐츠내용이 보이게