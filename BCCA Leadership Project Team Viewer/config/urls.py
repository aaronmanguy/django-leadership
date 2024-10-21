from django.urls import path


from app.views import team


urlpatterns = [
    path("", team),
    path("<name>", team),
]
