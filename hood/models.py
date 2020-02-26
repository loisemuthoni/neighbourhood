from django.db import models

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post,blank=True, on_delete=models.CASCADE,null=True,related_name='comment')
    commenter=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    comment=models.TextField(max_length =30)



    def delete_comment(self):
        self.delete()

    def save_comment(self):
        self.save()

    @classmethod
    def get_comments(cls):
        comments=cls.objects.all()
        return comments

    @classmethod
    def get_comments_by_post_id(cls,post_id):
        comments=cls.objects.filter(id=post_id)
        return comments
