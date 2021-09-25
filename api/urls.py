
from django.urls import path
from api.views import FirstApiView, testView
app_name = "api"

# domain.com/products
urlpatterns = [
    path("welcome/", FirstApiView.as_view()),
    path("test/", testView),

]
