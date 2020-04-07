import os
import aiohttp_cors

# -----------------------------------------------------------------------------
# CONFIG
# -----------------------------------------------------------------------------

enable_logging = True  # Enable logging with mode for

scheme = 'http://'  # Or 'https://' !?

ip_server_list = ['172.17.0.3', '172.17.0.4']  # Available Server IP Addresses

ip_url_list = [(scheme + x) for x in ip_server_list]  # With scheme

os.environ["PYTHONASYNCIODEBUG"] = "1"  # Enable debug mode for asyncio

defaults_cors = {
    "http://localhost:8081": aiohttp_cors.ResourceOptions()
}
