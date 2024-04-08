import aiohttp
import requests


class AsyncClient(aiohttp.ClientSession):
    pass


class SyncClient(requests.Session):
    pass
