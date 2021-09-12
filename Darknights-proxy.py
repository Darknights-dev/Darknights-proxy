from mitmproxy.options import Options
from mitmproxy.tools.web.master import WebMaster
from mitmproxy.http import HTTPFlow

remote_server = "example.com"
proxy_enable = True
class ArkInterceptor():
    if not proxy_enable:
        Servers = {"ak-gs-localhost.hypergryph.com": ("ak-gs.hypergryph.com", 8443),
                   "ak-gs-b-localhost.hypergryph.com": ("ak-gs.hypergryph.com", 8443),
                   "ak-as-localhost.hypergryph.com": ("ak-as.hypergryph.com", 9443)
                }
    else:
        Servers = {"ak-gs-localhost.hypergryph.com": (remote_server, 9443),
                   "ak-gs-gf.hypergryph.com": (remote_server, 9443),
                   "ak-gs-b-localhost.hypergryph.com": (remote_server, 9443),
                   "ak-as-localhost.hypergryph.com": (remote_server, 9443),
                   "as.hypergryph.com" : (remote_server, 9443),
                   "bi-track.hypergryph.com" : (remote_server, 9443),
                   "gv1.xdrig.com": (remote_server, 9443),
                   "me.xdrig.com": (remote_server, 9443),
                   "ak-fs.hypergryph.com": (remote_server, 9443)
                }

    ServersList = [key for key in Servers.keys()] + [val[0] for val in Servers.values()]
    
    def __init__(self):
        print("Proxy Loaded.")
        
    def http_connect(self, flow: HTTPFlow):
        if (flow.request.host in self.Servers.keys()):
            flow.request.host, flow.request.port = self.Servers.get(flow.request.host)

addons=[
    ArkInterceptor()
]

# run directly for localhost only
if __name__ == "__main__":
    ops = Options(
    listen_host='0.0.0.0', 
    listen_port=8080,   
    ssl_insecure=True
    )
    master = WebMaster(ops)
    master.addons.add(ArkInterceptor())
    master.run()
