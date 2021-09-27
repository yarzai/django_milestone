from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils.timesince import timesince
from django.urls import reverse
from accounts.models import Account


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


class ProductQuerySet(models.query.QuerySet):
    # def count(self):
    #     return super().count() + 5

    def is_availible(self):
        return self.filter(is_availible=True)


class ProductModelManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    # def all(self):
    #     print("ALL")
    #     return super().all().filter(is_availible=True)


class Product(models.Model):
    # name = models.CharField(max_length=150, validators=[validate_name])
    name = models.CharField(max_length=150)
    price = models.IntegerField(verbose_name="Product Price")
    code = models.IntegerField(unique=True, error_messages={
        "unique": "please enter another code.",
        "blank": "please fill the field."
    },
        help_text="enter a unique value")
    quantity = models.IntegerField()
    is_availible = models.BooleanField(default=True)
    image = models.ImageField(upload_to="products", null=True, blank=True)
    category = models.CharField(max_length=150, choices=CATEGORIES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # email = models.EmailField()
    slug = models.SlugField(null=True, blank=True)
    user = models.ForeignKey(
        Account, on_delete=models.DO_NOTHING, related_name='product', null=True, blank=True)

    author = models.ManyToManyField('Author')

    objects = ProductModelManager()
    # products = ProductModelManager()

    @property
    def added_on(self):
        return timesince(self.created) + " ago"

    def __str__(self):
        return self.name + " - " + str(self.code)

    def get_absolute_url(self):
        return reverse("products:detail-product", kwargs={"product_slug": self.slug})

    def save(self, *args, **kwargs):

        # if not self.slug:
        #     self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        print("save method was called")

    class Meta:
        db_table = 'products'
        ordering = ["created", '-price']
        # verbose_name = 'product1'
        # verbose_name_plural = "product2"
        # unique_together = ["name" ,"price"]


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    print("pre save")
    # print("sender:", sender)
    # if not instance.slug:
    #     instance.slug = slugify(instance.name)


pre_save.connect(product_pre_save_receiver, sender=Product)


def product_post_save_receiver(sender, instance, created, *args, **kwargs):
    print("post save")
    if created:
        if not instance.slug:
            instance.slug = slugify(instance.name)
            instance.save()


post_save.connect(product_post_save_receiver, sender=Product)


class Author(models.Model):
    name = models.CharField(max_length=150)
    eduction = models.CharField(max_length=150)

    class Meta:
        db_table = 'author'
