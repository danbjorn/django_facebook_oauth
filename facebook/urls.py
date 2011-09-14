from django.conf.urls.defaults import patterns

urlpatterns = patterns('facebook.views',
  (r'^authentication_callback$', 'authentication_callback', {}, 'authentication_callback'),
)
