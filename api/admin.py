from django.contrib import admin
from .models import *


# Register your models here.
model = [Project, BoardColumn, Task, TaskFile]
admin.site.register(model)
