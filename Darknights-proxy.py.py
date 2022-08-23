from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.web.master import WebMaster
from mitmproxy.http import HTTPFlow

network_config = """{"sign":"N+TjgIU1VP85wUeRVcmU6k9w3x3oTlKDXM9oK2TllRtryxTH2S9zMCAgUKIBvhinssBE7Dkll34G0llfUYdlnJTWar+OydnkEN0DA9ecWuoNdQRJ3fIAyYMDRsrTjcrkfUqDJ6GdB9MivqYBm5MKhFxzdI1UtY2kJxC9TZJR5m0=","content":"{\\"configVer\\":\\"5\\",\\"funcVer\\":\\"V030\\",\\"configs\\":{\\"V030\\":{\\"override\\":true,\\"network\\":{\\"gs\\":\\"placeholder\\",\\"as\\":\\"placeholder\\",\\"u8\\":\\"placeholder\\",\\"hu\\":\\"https://ak.hycdn.cn/assetbundle/official\\",\\"hv\\":\\"https://ak-conf.hypergryph.com/config/prod/official/{0}/version\\",\\"rc\\":\\"https://ak-conf.hypergryph.com/config/prod/official/remote_config\\",\\"an\\":\\"https://ak-conf.hypergryph.com/config/prod/announce_meta/{0}/announcement.meta.json\\",\\"prean\\":\\"https://ak-conf.hypergryph.com/config/prod/announce_meta/{0}/preannouncement.meta.json\\",\\"sl\\":\\"https://ak.hypergryph.com/protocol/service\\",\\"of\\":\\"placeholder/index.html\\",\\"pkgAd\\":\\"https://ak.hypergryph.com/download\\",\\"pkgIOS\\":\\"https://apps.apple.com/cn/app/id1454663939\\",\\"secure\\":false}}}}"}"""

dist = "https://example.com"

class ArkInterceptor():

    def __init__(self):
        print("Proxy Loaded.")

    def response(self, flow: HTTPFlow):
        if not flow.request.path.find("network_config") == -1:
            flow.response.set_text(str(network_config).replace("placeholder",dist))

# run directly for localhost only
if __name__ == "__main__":
    ops = Options(
        listen_host='0.0.0.0',
        listen_port=8080,
        ssl_insecure=True
    )
    master = WebMaster(ops)
    master.server = ProxyServer(ProxyConfig(ops))
    master.addons.add(ArkInterceptor())
    master.run()

addons = [
    ArkInterceptor()
]