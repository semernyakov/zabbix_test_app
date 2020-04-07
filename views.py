import pprint
import sys

import aiohttp
from aiohttp import web
from aiozabbix import ZabbixAPI
from aiozabbix import ZabbixAPIException

from config import ip_url_list


async def fetch(session, url):
    zapi = ZabbixAPI(url, client_session=session)
    await zapi.login('Admin', 'zabbix')

    try:
        hosts = await zapi.host.get(
            monitored_hosts=1,
            output=['host', 'hostid', 'name']
        )
    except ZabbixAPIException as e:
        print(e)
        sys.exit()
    else:
        return hosts


async def index(request):
    doubles, data = [], []
    try:
        async with aiohttp.ClientSession() as session:
            for url in ip_url_list:
                res = await fetch(session, url)
                data += res
    except ZabbixAPIException as e:
        print(e)
        sys.exit()
    else:
        if data:

            # v1
            # for n, i in enumerate(data, 0):
            #     for x in data[n + 1:]:
            #         if x['host'] == i['host'] or x['name'] == i['name']:
            #             doubles.append(i)

            # v2
            doubles = [x for n, i in enumerate(data, 0) for x in data[n + 1:] if
                       x['host'] == i['host'] or x['name'] == i['name']]

            pprint.pprint(doubles)
            return web.json_response(doubles)
        else:
            return web.json_response([{"error": "data not found!"}])
