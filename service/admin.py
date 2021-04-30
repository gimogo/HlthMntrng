from django.contrib import admin
from service.models import Prescription,Hospital,Location,Appointment,HealthRecord
# Register your models here.
admin.site.register(Prescription)
admin.site.register(Hospital)
admin.site.register(Location)
admin.site.register(Appointment)
admin.site.register(HealthRecord)

