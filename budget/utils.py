# budget/utils.py

def bepaal_categorie(omschrijving):
    omschrijving = omschrijving.lower()

    if any(w in omschrijving for w in ['albert heijn', 'jumbo', 'lidl', 'aldi']):
        return 'Boodschappen'

    if any(w in omschrijving for w in ['salaris', 'werkgever', 'loon']):
        return 'Inkomen'

    if any(w in omschrijving for w in ['huur', 'verhuurder']):
        return 'Huur'

    if any(w in omschrijving for w in ['spotify', 'netflix', 'ziggo']):
        return 'Abonnementen'

    if any(w in omschrijving for w in ['ns reizigers', 'ovpay', 'gvb']):
        return 'Reizen'

    if any(w in omschrijving for w in ['pizza', 'burger', 'cafetaria', 'restaurant']):
        return 'Eten & Drinken'

    if any(w in omschrijving for w in ['hypotheek', 'abn amro bank']):
        return 'Vaste lasten'

    if 'geldmaat' in omschrijving:
        return 'Contant'

    return 'Overig'
