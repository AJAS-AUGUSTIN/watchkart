from django.db import models
from django.db.models.base import Model
from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.db.models.enums import Choices

from accounts.models import Account

# Create your models here.
class Categories(models.Model):
    id            = models.AutoField(primary_key=True)
    title         = models.CharField(max_length=100)
    url_slug      = models.CharField(max_length=100)
    thumbnail     = models.FileField()
    description   = models.TextField(max_length=300, blank=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    is_active     = models.IntegerField(default=1)

class SubCategories(models.Model):
    id            = models.AutoField(primary_key=True)
    category_id   = models.ForeignKey(Categories, on_delete=models.CASCADE    )
    title         = models.CharField(max_length=100)
    url_slug      = models.CharField(max_length=100)
    thumbnail     = models.FileField()
    description   = models.TextField(max_length=300, blank=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    is_active     = models.IntegerField(default=1)

class Products(models.Model):
    id                       = models.AutoField(primary_key=True)
    SubCategories_id         = models.ForeignKey(SubCategories,on_delete=models.CASCADE)
    product_name             = models.CharField(max_length=200)
    url_slug                 = models.CharField(max_length=100)
    brand                    = models.CharField(max_length=200)
    product_max_price        = models.CharField(max_length=255)
    product_discount_price   = models.IntegerField()
    product_description      = models.TextField(max_length=500)
    product_long_description = models.TextField(max_length=500)
    created_at               = models.DateTimeField(auto_now_add=True)
    in_stock_total           = models.IntegerField(default=1)
    is_active                = models.IntegerField(default=1)
    image1                 = models.ImageField(upload_to='pics',blank = True,null = True)
    image2                = models.ImageField(upload_to='pics',blank = True,null = True)
    image3                 = models.ImageField(upload_to='pics',blank = True,null = True)
    image4                 = models.ImageField(upload_to='pics',blank = True,null = True)

    def get_url(self):
        return reverse('product_detail',args=[self.category.slug, self.slug])

class Address(models.Model):
    user_id = models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50)
    email        = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10)
    address_line_1 = models.TextField()
    address_line_2 = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    order_note = models.TextField(max_length=100)
    pincode = models.IntegerField()


# class ProductMedia(models.Model):
#     id             = models.AutoField(primary_key=True)
#     product_id     = models.ForeignKey(Products, on_delete=models.CASCADE)
#     media_type_choice = ((1,"Image"),(2,"Video"))
#     media_type     = models.CharField(max_length=255)
#     media_content  = models.FileField()
#     created_at     = models.DateTimeField(auto_now_add=True)
#     is_active      = models.IntegerField(default=1)

# class ProductTransaction(models.Model):
#     id             = models.AutoField(primary_key=True)
#     product_id     = models.ForeignKey(Products, on_delete=models.CASCADE)
#     transaction_type_choices = ((1,"BUY"),(2,"SELL"))
#     transaction_product_count = models.IntegerField(default=1)
#     transaction_type = models.Choices(Choices = transaction_type_choices, max_length = 255)
#     transaction_description = models.CharField(max_length=255)
#     created_at     = models.DateTimeField(auto_now_add=True)

# class ProductDetails(models.Model):
#     id            = models.AutoField(primary_key=True)
#     product_id    = models.ForeignKey(Products, on_delete=models.CASCADE)
#     title         = models.CharField(max_length=255)
#     title_details = models.CharField(max_length=255)
#     created_at    = models.DateTimeField(auto_now_add=True)  
#     is_active     = models.IntegerField(default=1)

# class ProductAbout(models.Model):
#     id            = models.AutoField(primary_key=True)
#     product_id    = models.ForeignKey(Products, on_delete=models.CASCADE)
#     title         = models.CharField(max_length=255)
#     created_at    = models.DateTimeField(auto_now_add=True)  
#     is_active     = models.IntegerField(default=1)

# class ProductTags(models.Model):
#     id            = models.AutoField(primary_key=True)
#     product_id    = models.ForeignKey(Products, on_delete=models.CASCADE)
#     title         = models.CharField(max_length=255)
#     created_at    = models.DateTimeField(auto_now_add=True)  
#     is_active     = models.IntegerField(default=1)

# class ProductQuestions(models.Model):
#     id            = models.AutoField(primary_key=True)
#     product_id    = models.ForeignKey(Products, on_delete=models.CASCADE)
#     user_id       = models.ForeignKey(Account, on_delete=models.CASCADE)
#     question      = models.TextField(max_length=255)
#     answer        = models.TextField(max_length=255)
#     created_at    = models.DateTimeField(auto_now_add=True)  
#     is_active     = models.IntegerField(default=1)

# class ProductReviews(models.Model):
#     id            = models.AutoField(primary_key=True)
#     product_id    = models.ForeignKey(Products, on_delete=models.CASCADE)
#     user_id       = models.ForeignKey(Account, on_delete=models.CASCADE)
#     review_images = models.FileField()
#     rating        = models.CharField(default='5')
#     review        = models.TextField(default='')
#     created_at    = models.DateTimeField(auto_now_add=True)  
#     is_active     = models.IntegerField(default=1)

# class ProductReviewVoting(models.Model):
#     id            = models.AutoField(primary_key=True)
#     product_review_id    = models.ForeignKey(Products, on_delete=models.CASCADE)
#     user_id_voting      = models.ForeignKey(Account, on_delete=models.CASCADE)
#     created_at    = models.DateTimeField(auto_now_add=True)  
#     is_active     = models.IntegerField(default=1)  

# class ProductVarient(models.Model):
#     id      = models.AutoField(primary_key=True)
#     title   = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)

# class ProductVarientItems(models.Model):
#     id      = models.AutoField(primary_key=True)
#     product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
#     product_varient_id = models.ForeignKey(ProductVarient, on_delete=models.CASCADE)
#     title   = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)





    # def __str__(self):
    #     return self.category_name