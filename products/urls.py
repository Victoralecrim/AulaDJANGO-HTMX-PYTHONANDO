from django.urls import path
from . import views, htmx_views

urlpatterns = [
    path("list_products", views.list_products, name="list_product"),
    path("edit_product/<int:id>/", htmx_views.edit_product, name="edit_product"),
    path(
        "get_product_form/<int:id>/",
        htmx_views.get_product_form,
        name="get_product_form",
    ),
]

# URLS que vão receber a requisição do HTMX
htmx_urlpatterns = [
    path("check_product/", htmx_views.check_product, name="check_product"),
    path("save_product/", htmx_views.save_product, name="save_product"),
    path("delete_product/<int:id>/", htmx_views.delete_product, name="delete_product"),
    path(
        "edit_product_htmx/<int:id>/", htmx_views.edit_product, name="edit_product_htmx"
    ),  # Renomeada para evitar conflito
]


urlpatterns += htmx_urlpatterns
