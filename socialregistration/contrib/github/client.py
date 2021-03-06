from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from socialregistration.clients.oauth import OAuth2
from socialregistration.settings import SESSION_KEY
import httplib2
import json

TIMEOUT = getattr(settings, 'SOCIALREGISTRATION_SOCKET_TIMEOUT', 5)


class Github(OAuth2):
    client_id = getattr(settings, 'GITHUB_CLIENT_ID', '')
    secret = getattr(settings, 'GITHUB_CLIENT_SECRET', '')
    scope = getattr(settings, 'GITHUB_REQUEST_PERMISSIONS', '')
    
    auth_url = 'https://github.com/login/oauth/authorize'
    access_token_url = 'https://github.com/login/oauth/access_token'
    
    _user_info = None
    
    def get_callback_url(self, **kwargs):
        if self.is_https():
            return 'https://%s%s' % (Site.objects.get_current().domain,
                reverse('socialregistration:github:callback'))
        return 'http://%s%s' % (Site.objects.get_current().domain,
            reverse('socialregistration:github:callback'))
        
    def get_user_info(self):
        if self._user_info is None:
            resp, content = self.request('https://api.github.com/user')
            self._user_info = json.loads(content)
        return self._user_info
    
    @staticmethod
    def get_session_key():
        return '%sgithub' % SESSION_KEY

    def client(self):
        ca_certs = getattr(settings, 'HTTPLIB2_CA_CERTS', None)
        return httplib2.Http(ca_certs=ca_certs, timeout=TIMEOUT, disable_ssl_certificate_validation=True)
