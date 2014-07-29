from django.contrib import admin
from .models import Health, UserPicture, ReceiptImage

# Register your models here.


class HealthAdmin(admin.ModelAdmin):
    class Meta:
        model = Health

admin.site.register(Health, HealthAdmin)


class UserPictureAdmin(admin.ModelAdmin):
    class Meta:
        model = UserPicture

admin.site.register(UserPicture, UserPictureAdmin)



class ReceiptImageAdmin(admin.ModelAdmin):
    class Meta:
        model = ReceiptImage

admin.site.register(ReceiptImage, ReceiptImageAdmin)



