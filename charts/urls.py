# from django . contrib import admin
from django . urls import path
from charts.views import simple_plot_png

urlpatterns = [
    path("plot.png", simple_plot_png, name="simple_plot_png"),
]



