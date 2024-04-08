from pycodeforce.__clients__ import AsyncClient, SyncClient
from pycodeforce.abc.endpoints import CodeforcesAPI
from pycodeforce.abc.objects import User
import time
import aiohttp
import msgspec
import random
import typing as t
from hashlib import sha512


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

    def _generate_authorisation(
        self,
        method_name: t.Literal[
            "blogEntry.comments",
            "blogEntry.view",
            "contest.hacks",
            "contest.list",
            "contest.ratingChanges",
            "contest.standings",
            "contest.status",
            "problemset.problems",
            "problemset.recentStatus",
            "recentActions",
            "user.blogEntries",
            "user.friends",
            "user.info",
            "user.ratedList",
            "user.rating",
            "user.status",
        ],
    ) -> str:
        auth_url = ""
        auth_url += f"&apiKey={self._auth_key}"
        if self._time is None:
            self._time = int(time.time())
        auth_url += f"&time={self._time}"
        auth_url += f"&apiSig={random.randint(000000, 999999)}"
        auth_url += str(sha512(auth_url.encode("utf-8")))
        return auth_url

    async def _generate_response(self, url: str) -> aiohttp.ClientResponse:
        async with self._client as socket:
            response = await socket.get(url=url)
            return response

    async def get_user_inro(
        self, handles: str, check_historic_handles: t.Optional[bool] = True
    ) -> User:
        endpoint_url = self._url_generator.user_info(
            handles=handles, check_historic_handles=check_historic_handles
        )
        if self._auth_context is not "":
            endpoint_url += self._auth_context
        # generate_response = await self._generate_response(url=endpoint_url)
