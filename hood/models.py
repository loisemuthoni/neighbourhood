from django.db import models

# Create your models here.

class Business(models.Model):
    business_image=models.ImageField(upload_to='businesses',null=True)
    business_name=models.CharField(max_length =30)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    neighborhood=models.ForeignKey(NeighborHood,on_delete=models.CASCADE,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)

    def save_business(self):
        self.save()
    def delete_business(self):
        self.delete()


    def update_business(self):
        self.business_image=business_image
        self.business_name=business_name
        self.user=location
        self.neighborhood=neighborhood
        self.email=email
        self.save()

    @classmethod
    def filter_by_neighborhood(cls,neighborhood_id):
        businesses=cls.objects.filter(id=neighborhood_id)
        return businesses


    @classmethod
    def find_business_by_id(cls,business_id):
        business=cls.objects.get(id=business_id)
        return business


    @classmethod
    def get_all_businesses(cls):
        businesses=cls.objects.all()
        return businesses


    @classmethod
    def search_by_business_name(cls,search_term):
        businesses = cls.objects.filter(business_name__icontains=search_term)
        return businesses



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
