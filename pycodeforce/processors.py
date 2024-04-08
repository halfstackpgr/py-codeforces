from pycodeforce.clients import AsyncClient, SyncClient
from pycodeforce.abc.endpoints import CodeforcesAPI
from pycodeforce.abc.objects import (
    User
)
import time
import aiohttp
import msgspec
import typing as t



class AsyncMethod:
    def __init__(self, auth_key: t.Optional[str], time:t.Optional[int], api_signature:str ) -> None:
        self._url_generator = CodeforcesAPI()
        self._client = AsyncClient()
        self._auth_context = ""
        if auth_key:
            self._auth_context += f"&apiKey={auth_key}"
        if time:
            self._auth_context += f"&time={time}"
        


        pass
    
    async def _generate_response(self, url:str)->aiohttp.ClientResponse:
        async with self._client as socket:
            response = await socket.get(url=url)
            return response

    async def get_user_inro(self, handles: str, check_historic_handles: t.Optional[bool] = True)->User:
        endpoint_url = self._url_generator.user_info(handles=handles, check_historic_handles=check_historic_handles)
        if self._auth_context is not "":
            endpoint_url += self._auth_context
        #generate_response = await self._generate_response(url=endpoint_url)
        
        