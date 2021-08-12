from django import forms
from products.models import Product

SERACH_CHOICES = [
    ("test1", "TEST 1"),
    ("test2", "TEST 2"),
    ("test3", "TEST 3"),
    ("test4", "TEST 4")
]

class TestForm(forms.Form):
    # text = forms.CharField(label="Search", widget=forms.CheckboxSelectMultiple(choices=SERACH_CHOICES))
    text = forms.CharField()
    # integer = forms.IntegerField(widget=forms.Textarea)
    integer = forms.IntegerField()
    boolean = forms.BooleanField()
    email = forms.EmailField()

    def clean_integer(self, *args, **kwargs):
        integer = self.cleaned_data.get("integer")
        if integer < 10:
            raise forms.ValidationError("The number should be greater than 10")
        return integer


class ProductModalForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'