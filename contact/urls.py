from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'), 
    path("",views.ListTodoAPIView.as_view(),name="todo_list"),
    path("create/", views.CreateTodoAPIView.as_view(),name="todo_create"),
    path("update/<int:pk>/",views.UpdateTodoAPIView.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.DeleteTodoAPIView.as_view(),name="delete_todo"),
    # user signup
    path("signup",views.ListcustomerUsersAPIView.as_view(),name="todo_list"),
    path("createsignup/", views.CreatecustomerUsersAPIView.as_view(),name="todo_create"),
    path("updatesignup/<int:pk>/",views.UpdatecustomerUsersAPIView.as_view(),name="update_todo"),
    path("deletesignup/<int:pk>/",views.DeletecustomerUsersAPIView.as_view(),name="delete_todo")

]