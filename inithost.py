import asyncio
import sys

import aiohttp
from aiozabbix import ZabbixAPI, ZabbixAPIException

from config import ip_url_list


async def init_hosts(session, url, num, add_visible_name):
    zapi = ZabbixAPI(url, client_session=session)
    await zapi.login('Admin', 'zabbix')

    try:
        hosts = await zapi.host.get(monitored_hosts=1, output=['host', 'hostid', 'name'])
    except ZabbixAPIException as e:
        print(e)
        sys.exit()
        print(f'Zabbix hosts not found!')
    else:
        try:
            instance = await zapi.do_request(
                method="host.create",
                params={
                    "host": f"Linux-Server-{num}",
                    "name": f"Linux-Server-Name-{num}" if add_visible_name else f"Linux-Server-{num}",
                    "interfaces": [
                        {
                            "type": 1,
                            "main": 1,
                            "useip": 1,
                            "ip": "127.0.0.1",
                            "dns": "",
                            "port": "10050"
                        }
                    ],
                    "groups": [
                        {
                            "groupid": "2"
                        }
                    ],
                    "tags": [
                        {
                            "tag": f"Linux-Server-{num}",
                            "value": f"Linux-Server-{num}"
                        }
                    ]
                }
            )
        except Exception as e:
            print(e)
            sys.exit()
        else:
            print(f"Added instance {instance}")
            return instance


async def main():
    async with aiohttp.ClientSession() as session:
        for url in ip_url_list:
            res1 = await init_hosts(session, url, 1, add_visible_name=True)
            res2 = await init_hosts(session, url, 2, add_visible_name=True)
            res3 = await init_hosts(session, url, 3, add_visible_name=False)
            print(res1, res2, res3)


asyncio.run(main())
