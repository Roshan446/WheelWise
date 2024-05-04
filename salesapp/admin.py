from django.contrib import admin
from salesapp.models import BikeBrand, City, State
# Register your models here.


admin.site.register(BikeBrand)
admin.site.register(State)
admin.site.register(City)
