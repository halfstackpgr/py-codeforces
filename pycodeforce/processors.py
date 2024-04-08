from pycodeforce.clients import AsyncClient
from pycodeforce.abc.endpoints import CodeforcesAPI
from pycodeforce.abc.objects import (
    UserInteractionResponse, 
    BlogEntryResponse,
    User,
    BlogEntry
    
)
import time
import msgspec
import random
import typing as t
import hashlib


class AsyncMethod:
    def __init__(
        self,
        auth_key: t.Optional[str],
        unix_time: t.Optional[int],
        secret: t.Optional[str],
    ) -> None:
        self._url_generator = CodeforcesAPI()
        self._client = AsyncClient()
        self._auth_key = auth_key
        self._secret = secret
        self._time = unix_time

    def _generate_authorisation(self, end_point_url: str) -> str:
        methodial = end_point_url.removeprefix("https://codeforces.com/api/")
        print(methodial)
        auth_url = f"{methodial}?"
        if self._time is None:
            self._time = int(time.time())
        rand_num = str(random.randint(100000, 999999))
        auth_url += f"apiKey={self._auth_key}&time={self._time}&apiSig={rand_num}/"
        auth_url += methodial
        auth_url += f"?apiKey={self._auth_key}&time={self._time}#{self._secret}"
        print(auth_url.encode("utf-8"))
        hash_object = hashlib.sha512(auth_url.encode("utf-8"), usedforsecurity=False)
        
        hex_dig = hash_object.hexdigest()

        auth_url = f"https://codeforces.com/api/{methodial}?apiKey={self._auth_key}&time={self._time}&apiSig={rand_num}{hex_dig}"
        return auth_url

    async def _generate_response(self, url: str) -> bytes:
        async with self._client as socket:
            response = await socket.get(url=url)
            return await response.read()

    async def get_user(
        self, handles: str, check_historic_handles: t.Optional[bool] = True
    ) -> t.Optional[t.List[User]]:
        list_of_users: t.List[User] = []
        endpoint_url = self._url_generator.user_info(
            handles=handles, check_historic_handles=check_historic_handles
        )
        final_url = self._generate_authorisation(end_point_url=endpoint_url)
        try:
            base = msgspec.json.decode(
                await self._generate_response(url=final_url),
                strict=False,
                type=UserInteractionResponse,
            )
            if base.status != "FAILED":
                if isinstance(base.result, t.List):
                    list_of_users = base.result
                if isinstance(base.result, User):
                    list_of_users.append(base.result)
            else:
                raise Exception(base.comment)
        except Exception as e:
            raise e

        return list_of_users

    
    async def get_blog_entry_comments(
        self, blog_entry_id: int
        ) -> t.Optional[t.List[BlogEntry]]:
        list_of_blog_entry_comments: t.List[BlogEntry] = []
        endpoint_url = self._url_generator.blog_entry_comments(blog_entry_id=blog_entry_id)
        print(endpoint_url)
        final_url = self._generate_authorisation(end_point_url=endpoint_url)
        print(final_url)
        try:
            base = msgspec.json.decode(
                await self._generate_response(url=final_url),
                strict=False,
                type=BlogEntryResponse,
            )
            if base.status != "FAILED":
                if isinstance(base.result, t.List):
                    list_of_blog_entry_comments = base.result
                if isinstance(base.result, BlogEntry):
                    list_of_blog_entry_comments.append(base.result)
            else:
                raise Exception(base.comment)
        except Exception as e:
            raise e

        return list_of_blog_entry_comments
    
    async def close(self):
        await self._client.close()


