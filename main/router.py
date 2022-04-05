from rest_framework import routers
from main.views import *

router = routers.DefaultRouter()

router.register('logo', LogoView)
router.register('slider', SliderView)
router.register('category', CategoryView)
router.register('product', ProductView)
router.register('client', ClientView)
router.register('cart', CartView)
router.register('wishlist', WishlistView)
router.register('bestsellers', BestSellersView)
router.register('miniinfo', MiniInfoView)
router.register('blog', BlogView)
router.register('newsletter', NewsletterView)
router.register('aboutus', AboutUsView)