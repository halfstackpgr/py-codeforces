from pycodeforce.clients import AsyncClient
from pycodeforce.abc.endpoints import CodeforcesAPI
from pycodeforce.abc.objects import InteractionResponse, User
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
        auth_url = f"{methodial}?"
        if self._time is None:
            self._time = int(time.time())
        rand_num = str(random.randint(100000, 999999))
        auth_url += f"apiKey={self._auth_key}&time={self._time}&apiSig={rand_num}/"
        auth_url += methodial
        auth_url += f"?apiKey={self._auth_key}&time={self._time}#{self._secret}"
        hash_object = hashlib.sha512(auth_url.encode("utf-8"))
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
                type=InteractionResponse,
            )
            if base.status is not "FAILED":
                if isinstance(base.result, t.Dict):
                    list_of_users.append(
                        msgspec.json.decode(
                            (str(base.result)).encode("utf-8"), type=User
                        )
                    )
                if isinstance(base.result, t.List):
                    for user in base.result:
                        list_of_users.append(
                            msgspec.json.decode((str(user)).encode("utf-8"), type=User)
                        )
            else:
                raise Exception(base.comment)
        except Exception as e:
            raise e

        return list_of_users

    async def close(self):
        await self.close()
