from django.shortcuts import render
from django.conf.urls import url
from django.views.generic import View
from my_app.models import GroupModel


class GroupView(View):
    def get(self, request):
        group = GroupModel.objects.all()
        return render(request, 'group.html', {'group':group})




