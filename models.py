from django.db import models

# -------- Category Model --------
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"   # Fix plural name

    def __str__(self):
        return self.name


# -------- Product Model --------
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/')  # Requires Pillow

    def __str__(self):
        return self.name

