# from django . contrib import admin
from django . urls import path
from budget.views import transacties

urlpatterns = [
    # path ('admin/', admin.site.urls),
    path("transacties/", transacties, name="transacties"),
]

