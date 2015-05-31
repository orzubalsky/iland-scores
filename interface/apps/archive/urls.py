from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    'archive.views',
    url(r'p-01$', TemplateView.as_view(template_name='p_columns.html'), name='p-columns'),
    url(r'p-02$', TemplateView.as_view(template_name='p_scroll.html'), name='p-scroll'),
    url(r'p-03$', TemplateView.as_view(template_name='p_words.html'), name='p-words'),
    url(r'$', TemplateView.as_view(template_name='prototype_list.html'), name='home'),
)
