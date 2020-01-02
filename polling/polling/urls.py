from django.contrib import admin
from django.urls import include, path

# path () function is passed 2 required arguments - route (a string with a URL
# pattern) and view (HttpRequest object calls the specified view function),
# with kwargs and name being 2 more optional arguments.
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
