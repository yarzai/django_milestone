
from django.urls import path


from .views import test, productForm
app_name = "exercise"

# domain.com/exercise
urlpatterns = [
    path("", productForm),
]
