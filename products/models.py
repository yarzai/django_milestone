from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify

# Create your models here.

CATEGORIES = [
    ("computers", "Computers"),
    ("phones", "Phones")
]


def validate_name(value):
    # print("Name validator")
    # print("value", value)
    if 'n' in value:
        return value
    # print("Hi")
    raise ValidationError("name does not have @.")


class Product(models.Model):
    # name = models.CharField(max_length=150, validators=[validate_name])
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    code = models.IntegerField(unique=True)
    quantity = models.IntegerField()
    is_availible = models.BooleanField(default=True)
    image = models.ImageField(upload_to="products", null=True, blank=True)
    category = models.CharField(max_length=150, choices=CATEGORIES)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    # email = models.EmailField()
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name + " - " + str(self.code)

    def save(self, *args, **kwargs):
        print("save method was called")
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'products'
        ordering = ["created", '-price']
        # verbose_name = 'product1'
        # verbose_name_plural = "product2"
        # unique_together = ["name" ,"price"]
