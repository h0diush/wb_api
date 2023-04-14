from django.contrib import admin

from goods.models import Good, Review


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'user', 'get_url_reviews')
    list_filter = ('user', 'reviews')
    readonly_fields = ('date', 'goods_id', 'root_id')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'country', 'rating', 'good')
    list_filter = ('good', 'country', 'rating')
