from django.db import models


class Comment(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=50)

    class Meta:
        db_table = 'tb_comments'
