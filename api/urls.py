
from django.urls import path, include
from api.views import FirstApiView, testView
from rest_framework.routers import DefaultRouter
from .views import ProductViewSets

router = DefaultRouter()

router.register('products', ProductViewSets)

app_name = "api"

# domain.com/products
urlpatterns = [
    path("welcome/", FirstApiView.as_view()),
    path("test/", testView),
    path('', include(router.urls))

]
