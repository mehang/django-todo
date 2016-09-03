from django.conf.urls import url
from . import views
app_name='myapp'

urlpatterns=[
        #For list
    url(r'^$',views.IndexView.as_view(),name='index'),
        url(r'add/$',views.AddTodo.as_view(),name='addtodo')

#url(r'^$',views.delete, name='delete')
#url(r'^/add/$',views.add, name='add')
]
