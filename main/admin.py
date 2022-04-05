from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from main.models import  *
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'type', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name','last_name', 'email' )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('type', 'phone')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')})
    )

admin.site.register(Logo)
admin.site.register(Slider)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(BestSellers)
admin.site.register(MiniInfo)
admin.site.register(Blog)
admin.site.register(Newsletter)
admin.site.register(AboutUs)