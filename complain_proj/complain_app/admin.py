from django.contrib import admin
from .models import *

admin.site.register(Category)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'home_adress', 'first_name', 'last_name']
    
@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    list_display = ['written_by', 'content', 'category']
    
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_to_compl', 'answer_content', 'is_accepted']

# Register your models here.
