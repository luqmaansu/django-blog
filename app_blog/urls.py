from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home,), # blog home
    path('list/', views.blog_list, name="blog-list"),

    path('create/', views.blog_create,), # function based view to create a blog instance
    path('create2/', views.PostCreateView.as_view(), name="blog-create",),
    path('comment2/', views.CommmentAddView.as_view(), name="blog-comment"),
    path('<int:pk>/update2/', views.PostUpdateView.as_view(), name="blog-update",),
    path('<int:pk>/delete2/', views.PostDeleteView.as_view(), name="blog-delete",),
    


]
