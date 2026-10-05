# charts / views . py
import io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from django.http import HttpResponse

def simple_plot_png(request):
    # Data
    xs = [1 , 2 , 3 , 4 , 5]
    ys = [2 , 3 , 5 , 7 , 11]

    # Figuur
    fig , ax = plt.subplots(figsize=(5 , 3))
    ax.plot (xs, ys, marker="o")
    ax.set_title("Voorbeeldgrafiek" )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    fig.tight_layout()

    # Schrijf naar bytes - buffer als PNG
    buf = io.BytesIO()
    fig.savefig(buf , format = "png" , dpi =150)
    plt.close(fig)
    buf.seek(0)

    # Stuur als image / png
    return HttpResponse ( buf.read () , content_type = "image/png")


