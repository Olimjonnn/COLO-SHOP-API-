from django.shortcuts import render
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import viewsets
from main.models import *
from main.serializer import *

class LogoView(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']

    def list(self, request):
        logo = Logo.objects.last()
        log = LogoSerializer(logo)
        return Response(log.data)


class SliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']

    def list(self, request):
        slider = Slider.objects.last()
        sl = SliderSerializer(slider)
        return Response(sl)


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            user = request.user
            if user.type == 1:
                name = request.data['name']
                Category.objects.create(name=name)
                return Response({"Created"})
            else:
                return Response({"Sorry :("})
        except Exception as arr:
            data = {
                "error": f"{arr}"
            }
            return Response(data)


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            user = request.user
            if user.type == 1:
                category_id = request.POST.get('category')
                name = request.POST.get('name')
                image = request.FILES['image']
                price = request.POST.get('price')
                sale_price = request.POST.get('sale_price')
                sale = request.POST.get('sale')
                is_new = request.POST.get('is_new')
                best_sellers = request.POST.get('best_sellers')
                Product.objects.create(category_id=category_id, name=name, image=image, price=price, sale_price=sale_price, sale=sale, is_new=is_new, best_sellers=best_sellers)
                return Response({"Alhamdullilah"})
            else:
                return Response({"Sorry :("})
        except Exception as arr:
            data = {
                "error": f"{arr}"
            }
            return Response(data)

    @action(['GET'], detail=False)
    def filter(self, request):
        try:
            category = request.GET.get('category')
            cat = Product.objects.filter(category_id=category)
            ca = ProductSerializer(cat, many=True)
            return Response(ca.data)
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)

    @action(['GET'], detail=False)
    def isnew(self, request):
        proda = Product.objects.filter(is_new=True)
        pr = ProductSerializer(proda, many=True)
        return Response(pr.data)

class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    http_method_names = ['post']

class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    @action(['GET'], detail=False)
    def car(self, request):
        client = request.GET.get("client")
        clie = Cart.objects.filter(client_id=client)
        cl = CartSerializer(clie, many=True)
        return Response(cl.data)

class WishlistView(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    @action(['GET'], detail=False)
    def car(self, request):
        client = request.GET.get("client")
        clie = Wishlist.objects.filter(client_id=client)
        cl = WishlistSerializer(clie, many=True)
        return Response(cl.data)

class BestSellersView(viewsets.ModelViewSet):
    queryset = BestSellers.objects.all()
    serializer_class = BestSellersSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']

    @action(['GET'], detail=False)
    def sss(self, request):
        # product = request.GET.get('product')
        prod = BestSellers.objects.filter(product__best_sellers=True)
        produ = BestSellersSerializer(prod, many=True)
        return Response(produ.data)

class MiniInfoView(viewsets.ModelViewSet):
    queryset = MiniInfo.objects.all()
    serializer_class = MiniInfoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']

class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def create(self, request):
        user = request.user
        if user.type == 1:
            image = request.FILES.get('image')
            text = request.data['text']
            Blog.objects.create(image=image, text=text)
            return Response({"Created"})
        else:
            return Response({"Sorry :("})


class NewsletterView(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    http_method_names = ['post']
    def create(self, request):
        user = request.user
        if user.type == 2:
            email = request.data['email']
            Newsletter.objects.create(email=email)
            return Response({"Added"})
        else:
            return Response({"Sorry :("})


class AboutUsView(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']