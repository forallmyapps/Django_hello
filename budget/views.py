import io
import base64
from datetime import datetime
from decimal import Decimal, InvalidOperation
# from urllib import request

from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import Transactie
from .utils import bepaal_categorie
import matplotlib.pyplot as plt
from django.db.models import Sum


def transacties(request):
    alle = Transactie.objects.order_by('-transactiedatum')
    return render(request, "budget/transacties.html", { "transacties": alle } )


def verwijderen(request):
    if Transactie.objects.all().count() > 0:
        Transactie.objects.all().delete()  # bestaande data wissen


def grafiek(request):
    # Alleen uitgaven (negatieve bedragen)
    data = (
        Transactie.objects
        .filter(bedrag__lt=0)
        .values('categorie')
        .annotate(totaal=Sum('bedrag'))
        .order_by('totaal')
    )

    categorieen = [d['categorie'] for d in data]
    bedragen = [abs(d['totaal']) for d in data]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(categorieen, bedragen, color='steelblue')
    ax.set_xlabel('Totaal uitgegeven (EUR)')
    ax.set_title('Uitgaven per categorie')
    plt.tight_layout()

    # Omzetten naar base64-string voor de template
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    afbeelding = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return render(request, 'budget/grafiek.html', {'afbeelding': afbeelding} )


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            bestand = request.FILES['bestand']
            inhoud = bestand.read().decode('utf-8')
            regels = inhoud.strip().splitlines()

            verwijderen(request)  # bestaande data wissen

            for regel in regels:
                velden = regel.split('\t')
                if len(velden) < 8:
                    continue  # ongeldige regel overslaan

                try:
                    datum = datetime.strptime(velden[2], '%Y%m%d').date()
                    bedrag = Decimal(velden[6].replace(',', '.'))
                    omschrijving = velden[7].strip()

                    Transactie.objects.create(
                        rekeningnummer=velden[0],
                        transactiedatum=datum,
                        bedrag=bedrag,
                        omschrijving=omschrijving,
                        categorie=bepaal_categorie(omschrijving),
                    )

                except (ValueError, InvalidOperation):
                    continue

            return redirect('transacties')
    else:
        form = UploadForm()

    return render(request, 'budget/upload.html', {'form': form})


