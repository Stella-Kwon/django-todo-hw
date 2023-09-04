from django.db import models

# Create your models here.
class Todo(models.Model):

    class Meta:
        db_table = "todo_list"
    context = models.TextField(max_length= 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done_at = models.BooleanField(default=False)
    # 그냥 코드가 어드민에서 잘 돌아가는지 체크하는 boolean?

    def __str__(self):
        return self.context