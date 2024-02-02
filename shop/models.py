from django.db import models


class Product(models.Model):
    title = models.CharField('Product Name', max_length=100)
    description = models.TextField('Product description', max_length=1000)
    img = models.ImageField('Product image', upload_to='images/shop')
    link = models.CharField('Affiliate link', max_length=200)

    def __str__(self):
        return f'{self.title}, {self.description}'

    class Meta:
        verbose_name = 'Product'