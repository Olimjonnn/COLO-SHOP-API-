# Generated by Django 3.2.9 on 2022-04-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_aboutus_bestsellers_blog_cart_category_client_miniinfo_newsletter_product_production_shop_shopitem_s'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
