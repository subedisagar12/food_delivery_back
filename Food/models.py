from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    image=models.ImageField(upload_to="images/category_img",blank=True)

    class Meta:
        verbose_name_plural="Categories"
    def __str__(self):
        return self.name

class Food(models.Model):
    CHOICES=(
    ('Plate','Plate'),
    ('Piece','Piece'),
    ('Dozens','Dozens'),
    )
    name=models.CharField(max_length=250)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    primary_image=models.ImageField(upload_to="images/food_image")
    price=models.IntegerField(default=100)
    unit_serving=models.CharField(max_length=50,choices=CHOICES,default="Plate")
    secondary_image_1=models.ImageField(upload_to="images/food_image",blank=True)
    secondary_image_2=models.ImageField(upload_to="images/food_image",blank=True)
    secondary_image_3=models.ImageField(upload_to="images/food_image",blank=True)
    isPopular=models.BooleanField(default=False)

    def __str__(self):
        return self.name
