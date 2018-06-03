from urllib import urlopen
import json

from canari.maltego.entities import IPv4Address, Location
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow

__author__ = 'shaddygarg'
__copyright__ = 'Copyright 2018, hello Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.1'
__maintainer__ = 'shaddygarg'
__email__ = 'shaddygarg1@gmail.com'
__status__ = 'Development'


@EnableDebugWindow
class Whatismyip(Transform):
    """TODO: Your transform description."""

    # The transform input entity type.
    input_type = Location

    def do_transform(self, request, response, config):
        ip_json = urlopen('https://api.ipify.org?format=json').read()
        ip_address = json.loads(ip_json)['ip']
        response += IPv4Address(ip_address)
        return response

    def on_terminate(self):
        """This method gets called when transform execution is prematurely terminated. It is only applicable for local
        transforms. It can be excluded if you don't need it."""
        pass
