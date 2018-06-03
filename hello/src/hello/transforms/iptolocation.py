import json
from urllib import urlopen

from canari.maltego.entities import IPv4Address, Location
from canari.maltego.message import Bookmark
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
class IPToLocation(Transform):
    """TODO: Your transform description."""

    # The transform input entity type.
    input_type = IPv4Address

    def do_transform(self, request, response, config):
        # don't forget to add `from maltego.message import Bookmark`
        ip_address = request.entity.value

        url_template = config['hello.local.geo_ip_url']
        geoip_str = urlopen(url_template.format(ip=ip_address)).read()
        geoip_json = json.loads(geoip_str)
        country_code = geoip_json.get('country_code').lower()

        response += Location(
            country=geoip_json.get('country_name', 'Unknown'),
            city=geoip_json.get('city'),
            countrycode=geoip_json.get('country_code'),
            latitude=geoip_json.get('latitude'),
            longitude=geoip_json.get('longitude'),
            area=geoip_json.get('region_name'),
            link_label='From FreeGeoIP',
            bookmark=Bookmark.Orange,
            icon_url='http://www.geoips.com/assets/img/flag/256/%s.png' % country_code
        )

        return response

    def on_terminate(self):
        """This method gets called when transform execution is prematurely terminated. It is only applicable for local
        transforms. It can be excluded if you don't need it."""
        pass
