urlpatterns = [
    path('', views.cars_list, name='cars_list'),
    path('new/', views.new_car, name='new_car'),
    path('edit/<int:pk>/', views.edit_car, name='edit_car'),
    path('delete/<int:pk>/', views.delete_car, name='delete_car'),
    path('report/', views.report_cars, name='report_cars'),  # Adicionando a URL do relatório
]