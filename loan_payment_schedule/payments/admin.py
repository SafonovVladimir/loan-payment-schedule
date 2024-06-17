from django.contrib import admin

from .models import Client, Loan


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Loan)
