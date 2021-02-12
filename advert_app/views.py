from django.shortcuts import render
from .models import Advert

# Create your views here.
def advert(request):
    ads = Advert.objects.all().order_by('?')[:10]
    for advert in ads:
        current_parent_views = advert.parent_page_visit+1
        advert.parent_page_visit = current_parent_views
        advert.impression_percentage = (advert.page_visit/current_parent_views) * 100
        advert.save()

    context = {
        'adverts': ads
    }
    return render(request, 'advert.html', context)

def place_ads(request):
    message = ''
    if request.method == "POST":
        if request.FILES:
            banner = request.FILES.get('banner')
            Advert.objects.create(
                banner=banner
            )
            message = 'Upload was successful!'
    context = {
        "message": message
    }
    return render(request, 'place_ads.html', context)

def view_ad(request, id):
    advert = Advert.objects.get(id=id)

    current_page_visit = advert.page_visit+1
    advert.page_visit = current_page_visit
    advert.impression_percentage = (advert.page_visit/advert.parent_page_visit) * 100
    advert.save()

    context = {
        'banner': advert.banner.url,
        'impression': round(advert.impression_percentage, 1)
    }
    return render(request, 'view_ad.html', context)