from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactFrom
from .models import News,Category

def yangiliklar_list_view(request):
    yangiliklar_list_slide = News.published.all()
    latest_news_5 = News.published.all()[:5]
    iqtisodiy_news_one = News.published.filter(category__nomi='Iqtisodiyot')[0]
    iqtisodiy_news_4 = News.published.filter(category__nomi='Iqtisodiyot')[1:5]
    sport_news_one = News.published.filter(category__nomi='Sport')[0]
    sport_news_4 = News.published.filter(category__nomi='Sport')[1:5]
    texnologiy_news_one = News.published.filter(category__nomi='Texnologiy')[0]
    texnologiy_news_4 = News.published.filter(category__nomi='Texnologiy')[1:5]
    jamiyat_news_one = News.published.filter(category__nomi='Jamiyat')[0]
    jamiyat_news_4 = News.published.filter(category__nomi='Jamiyat')[1:5]



    context = {
        'yangiliklar_list': yangiliklar_list_slide,
        'latest_news_5': latest_news_5,
        'iqtisodiy_news_one':iqtisodiy_news_one,
        'iqtisodiy_news_4':iqtisodiy_news_4,
        'sport_news_one':sport_news_one,
        'sport_news_4':sport_news_4,
        'texnologiy_news_one':texnologiy_news_one,
        'texnologiy_news_4':texnologiy_news_4,
        'jamiyat_news_one':jamiyat_news_one,
        'jamiyat_news_4':jamiyat_news_4

    }

    return render(request=request, template_name='index.html', context=context)




def yangiliklar_detail_view(request, slug):

    yangiliklar_detail = News.object.get(slug = slug)
    yaqin_news = News.object.filter(category__nomi=yangiliklar_detail.category)[0:3]


    context = {
        'yangiliklar_detail': yangiliklar_detail,
        'yaqin_news': yaqin_news
    }

    return render(request=request, template_name='single_page.html', context=context)

def texno_news_view(request):

    news_list = News.published.filter(category__nomi='Texnologiy')


    context = {
        'news_list' : news_list,
    }

    return render(request, template_name='texno.html', context=context)



def mahalliy_news_view(request):

    news_list = News.published.filter(category__nomi='Mahalliy')

    context = {
        'news_list' : news_list,
    }

    return render(request, template_name='mahalliy.html', context=context)


def sport_news_view(request):

    news_list = News.published.filter(category__nomi='Sport')


    context = {

    'news_list' : news_list,

    }

    return render(request, template_name='sport.html', context=context)




def iqtisodiy_news_view(request):

    news_list = News.published.filter(category__nomi='Iqtisodiyot')


    context = {

    'news_list' : news_list,

    }

    return render(request, template_name='iqtisodi.html', context=context)


def jamiyat_news_view(request):

    news_list = News.published.filter(category__nomi='Jamiyat')


    context = {

    'news_list' : news_list,

    }

    return render(request, template_name='jamiyat.html', context=context)


def contact_view(request):
    form = ContactFrom(request.POST)
    if form.is_valid() and request.method =='POST':
        form.save()
        return HttpResponse('Xabaringiz yuborildi')
    context = {
        'form' : form
    }

    return render(request, template_name='contact.html', context=context)


def about_us_view(request):
    context = {

    }

    return render(request, template_name='about-us.html', context=context)

