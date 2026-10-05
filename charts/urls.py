# from django . contrib import admin
from django . urls import path
from charts.views import plaatje

urlpatterns = [
    # path ('admin/', admin.site.urls),
    path("plaatje/", plaatje, name="plaatje"),
]



