# coding=utf-8
from .models import Category

def catefories(request):
    return {
        'categories':Category.objects.all()

    }