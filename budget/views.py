from datetime import datetime
from decimal import Decimal, InvalidOperation

from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import Transactie
from .utils import bepaal_categorie

def transacties(request):
    alle = Transactie.objects.order_by('-transactiedatum')
    return render(request, "budget/transacties.html", { "transacties": alle } )

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            bestand = request.FILES['bestand']
            inhoud = bestand.read().decode('utf-8')
            regels = inhoud.strip().splitlines()

            Transactie.objects.all().delete()  # bestaande data wissen

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