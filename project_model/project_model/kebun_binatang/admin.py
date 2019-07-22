from django.contrib import admin
from .models import Hewan, Kandang, Penjaga, Pengunjung

class HewanAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'spesies']
    search_fields = ['id', 'nama', 'spesies']
    ordering = ['id']

class KandangAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'isi_kandang']
    search_fields = ['id', 'nama', 'isi_kandang']
    ordering = ['id']

class PenjagaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon']
    search_fields = ['id', 'nama', 'nomor_telepon']
    ordering = ['id']


class PengunjungAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon']
    search_fields = ['id', 'nama', 'nomor_telepon']
    ordering = ['id']
    

# Register your models here.
admin.site.register(Hewan, HewanAdmin)
admin.site.register(Kandang, KandangAdmin)
admin.site.register(Penjaga, PenjagaAdmin)
admin.site.register(Pengunjung, PengunjungAdmin)
