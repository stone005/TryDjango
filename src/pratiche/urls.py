from django.urls import path

from pratiche.views import (
    pratica_detail_view, 
    # pratica_create_view,
    # pratica_delete_view,
    pratica_list_view,
    # pratica_update_view,    
    # dynamic_lookup_view,
    )

app_name='pratiche'
urlpatterns = [
    path('', pratica_list_view, name='pratica-list'), 
    # path('crea/', pratica_create_view, name='pratica-create'),
    path('<int:id>/', pratica_detail_view, name='pratica-detail'),
    # path('<int:id>/modifica/', pratica_update_view, name='pratica-update'),    
    # path('<int:id>/elimina/', pratica_delete_view, name='pratica-delete'),
]