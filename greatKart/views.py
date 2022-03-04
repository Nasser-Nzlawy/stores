
from django.shortcuts import render
from store.models import Product, ReviewRating
from sliderimages.models import slideimage

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    slide_imgs = slideimage.objects.all()
    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'slide_imgs' : slide_imgs,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)
