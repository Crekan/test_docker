from django.contrib import admin
from django.urls import path

from test_api.views import BooksView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', BooksView.as_view()),
]
