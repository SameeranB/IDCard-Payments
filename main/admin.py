from django.contrib import admin
from .models import Student
from .models import Driver
from .models import Cab
from .models import Travel_History
from .models import Payment_History
from .models import Cab_History
# Register your models here.


admin.site.register(Student)
admin.site.register(Driver)
admin.site.register(Cab)
admin.site.register(Travel_History)
admin.site.register(Payment_History)
admin.site.register(Cab_History)

