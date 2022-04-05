from rest_framework import serializers
from main.models import  *

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = "__all__"


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Cart
        fields = "__all__"


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        # depth = 2
        model = Wishlist
        fields = "__all__"




class BestSellersSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = BestSellers
        fields = "__all__"


class MiniInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniInfo
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = "__all__"


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"