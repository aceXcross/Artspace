from django.shortcuts import render


def index(request):
    return render(request, 'artist/index.html', {'title': 'all information'})


def portfolio(request):
    return render(request, 'artist/index.html', {'title': 'portfolio'})


def brushes(request):

    return render(request, 'artist/index.html', {
        'title': 'brushes',
        'brushes':  ['Механические карандаши', 'Кисти для акварели', 'IPad Pro 2021 with Apple Pencil']
    })


def reviews(request):
    return render(request, 'artist/index.html', {'title': 'reviews'})
