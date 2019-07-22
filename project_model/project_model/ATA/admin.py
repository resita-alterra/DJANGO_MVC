from django.contrib import admin
from .models import Direksi, Mentee, MataPelajaran, Mentor, Challenge, LiveCode 

class DireksiAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'nama_lengkap', 'jabatan']
    search_fields = ['id', 'nama_lengkap', 'jabatan']

class MenteeAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'nama_lengkap', 'no_absen']
    search_fields = ['id', 'nama_lengkap', 'no_absen']

class MataPelajaranAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'nama_pelajaran', 'jadwal_dimulai']
    search_fields = ['id', 'nama_pelajaran', 'jadwal_dimulai']

class MentorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama_lengkap', 'no_telepon']
    search_fields = ['id', 'nama_lengkap', 'no_telepon']

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['id','banyak_soal','bobot_nilai']
    search_fields = ['id','banyak_soal','bobot_nilai']

class LiveCodeAdmin(admin.ModelAdmin):
    list_display = ['id','banyak_soal','bobot_nilai']
    search_fields = ['id','banyak_soal','bobot_nilai']




# Register your models here.
admin.site.register(Direksi, DireksiAdmin)
admin.site.register(Mentee, MenteeAdmin)
admin.site.register(MataPelajaran, MataPelajaranAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(LiveCode, LiveCodeAdmin)
