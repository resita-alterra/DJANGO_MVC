from django.contrib import admin
from .models import Dokter, Pasien, Resep, Obat
# Register your models here.
class DokterAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon']
    search_fields = ['id', 'nama', 'nomor_telepon']
    ordering = ['id']

class PasienAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon']
    search_fields = ['id', 'nama', 'nomor_telepon']
    ordering = ['id']

class ResepAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'total_harga']
    search_fields = ['id', 'nama', 'total_harga']
    ordering = ['id']

class ObatAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'kandungan']
    search_fields = ['id', 'nama', 'kandungan']
    ordering = ['id']


admin.site.register(Dokter, DokterAdmin)
admin.site.register(Pasien, PasienAdmin)
admin.site.register(Resep, ResepAdmin)
admin.site.register(Obat, ObatAdmin)
