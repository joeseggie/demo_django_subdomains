from django_hosts import patterns
from django_hosts import host
from django.conf import settings


host_patterns = patterns(
    '',
    host(r'admin', settings.ROOT_URLCONF, name='admin'),
    host(r'api', 'subdomainsdemo.api_urls', name='api'),
)
