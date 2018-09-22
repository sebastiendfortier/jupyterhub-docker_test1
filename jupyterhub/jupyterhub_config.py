## Generic
c.JupyterHub.admin_access = True
c.Spawner.default_url = '/lab'

## Authenticator
from oauthenticator.oauth2 import OAuthLoginHandler
from oauthenticator.generic import GenericOAuthenticator
from tornado.auth import OAuth2Mixin

class UVSQMixin(OAuth2Mixin):
    _OAUTH_AUTHORIZE_URL = 'https://keats.prism.uvsq.fr/oauth2/login'
    _OAUTH_ACCESS_TOKEN_URL = 'https://keats.prism.uvsq.fr/oauth2/token'

class UVSQLoginHandler(OAuthLoginHandler, UVSQMixin):
    pass

class UVSQAuthenticator(GenericOAuthenticator):
    login_service = 'UVSQ'
    login_handler = UVSQLoginHandler
    client_id = '1'
    client_secret = ''
    userdata_url = 'https://keats.prism.uvsq.fr/oauth2/userdata'
    token_url = 'https://keats.prism.uvsq.fr/oauth2/token'
    oauth_callback_url = 'https://jupyter.ens.uvsq.fr/hub/oauth_callback'

c.JupyterHub.authenticator_class = UVSQAuthenticator

c.Authenticator.admin_users = { 'lucadefe' }


## Docker spawner
import os

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = 'jupyter/base-notebook:137a295ff71b'
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '10G'

# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = os.environ['HUB_IP']


## Services
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]