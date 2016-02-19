
from django.conf.urls import patterns, include, url

# scout_group patterns.
urlpatterns = patterns("scout_group.views",
    url("^distrito/(?P<slug>[-\w]+)/$", "district", name="district"),
    url("^grupo-escoteiro/(?P<slug>[-\w]+)/$", "scout_group", name="scout_group"),

)
