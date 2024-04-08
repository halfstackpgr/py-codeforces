from pycodeforce.clients import AsyncClient
from pycodeforce.abc.endpoints import CodeforcesAPI
from pycodeforce.abc.objects import (
    UserInteractionResponse,
    BlogEntryCommentResponse,
    BlogEntryViewResponse,
    ContestHacksResponse,
    ContestListResponse,
    ContestRatingChangeResponse,
    User,
    Comment,
    BlogEntry,
    Hack,
    Contest,
    RatingChange
)
import time
import msgspec
import random
import typing as t
import hashlib


class AsyncMethod:
    def __init__(
        self,
        enable_auth: t.Optional[bool] = False,
        auth_key: t.Optional[str] = None,
        unix_time: t.Optional[int] = None,
        secret: t.Optional[str] = None,
    ) -> None:
        self._url_generator = CodeforcesAPI()
        self._client = AsyncClient()
        self._auth_key = auth_key
        self._secret = secret
        self._time = unix_time
        self._auth_enabled = enable_auth

    def _generate_authorisation(
        self,
        end_point_url: str,
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
        if self._auth_enabled is True:
            if not self._time:
                self._time = int(time.time())
            randon_six_digit_num = random.randint(111111, 999999)
            head = end_point_url.removeprefix(
                f"https://codeforces.com/api/{method_name}?"
            )
            to_hash = f"{randon_six_digit_num}/{method_name}?apiKey={self._auth_key}&{head}&time={self._time}#{self._secret}"
            hashed_string = (hashlib.sha512(to_hash.encode("utf8"))).hexdigest()
            final_url = f"https://codeforces.com/api/{method_name}?{head}&apiKey={self._auth_key}&time={self._time}&apiSig={randon_six_digit_num}{hashed_string}"
            return final_url
        else:
            return end_point_url

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
        final_url = self._generate_authorisation(
            method_name="user.info", end_point_url=endpoint_url
        )
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
    ) -> t.Optional[t.List[Comment]]:
        list_of_blog_entry_comments: t.List[Comment] = []
        endpoint_url = self._url_generator.blog_entry_comments(
            blog_entry_id=blog_entry_id
        )
        final_url = self._generate_authorisation(
            method_name="blogEntry.comments", end_point_url=endpoint_url
        )
        try:
            base = msgspec.json.decode(
                await self._generate_response(url=final_url),
                strict=False,
                type=BlogEntryCommentResponse,
            )
            if base.status != "FAILED":
                if isinstance(base.result, t.List):
                    list_of_blog_entry_comments = base.result
                if isinstance(base.result, Comment):
                    list_of_blog_entry_comments.append(base.result)
            else:
                raise Exception(base.comment)
        except Exception as e:
            raise e

        return list_of_blog_entry_comments

    async def get_blog_entry_view(
        self, blog_entry_id: int
    ) -> t.Optional[t.List[BlogEntry]]:
        list_of_blog_entry: t.List[BlogEntry] = []
        endpoint_url = self._url_generator.blog_entry_view(blog_entry_id=blog_entry_id)
        final_url = self._generate_authorisation(
            method_name="blogEntry.view", end_point_url=endpoint_url
        )
        try:
            base = msgspec.json.decode(
                await self._generate_response(url=final_url),
                strict=False,
                type=BlogEntryViewResponse,
            )
            if base.status != "FAILED":
                if isinstance(base.result, t.List):
                    list_of_blog_entry = base.result
                if isinstance(base.result, BlogEntry):
                    list_of_blog_entry.append(base.result)
            else:
                raise Exception(base.comment)
        except Exception as e:
            raise e

        return list_of_blog_entry

    async def get_contest_hacks(
        self, contest_id: int, as_manager: t.Optional[bool] = False
    ) -> t.Optional[t.List[Hack]]:
        list_of_contest_hacks: t.List[Hack] = []
        endpoint_url = self._url_generator.contest_hacks(
            contest_id=contest_id, as_manager=as_manager
        )
        final_url = self._generate_authorisation(
            method_name="contest.hacks", end_point_url=endpoint_url
        )
        try:
            base = msgspec.json.decode(
                await self._generate_response(url=final_url),
                strict=False,
                type=ContestHacksResponse,
            )
            if base.status != "FAILED":
                if isinstance(base.result, t.List):
                    list_of_contest_hacks = base.result
                if isinstance(base.result, Hack):
                    list_of_contest_hacks.append(base.result)
            else:
                raise Exception(base.comment)
        except Exception as e:
            raise e

        return list_of_contest_hacks

    async def get_contest_list(
        self, of_gym: t.Optional[bool] = False
    ) ->t.Optional[t.List[Contest]]:
        list_of_contest: t.List[Contest] = []
        endpoint_url = self._url_generator.contest_list(gym=of_gym)
        final_url = self._generate_authorisation(
            method_name="contest.list", end_point_url=endpoint_url
        )
        try:
            base = msgspec.json.decode(
                await self._generate_response(url=final_url),
                strict=False,
                type=ContestListResponse,
            )
            if base.status != "FAILED":
                if isinstance(base.result, t.List):
                    list_of_contest = base.result
                if isinstance(base.result, Contest):
                    list_of_contest.append(base.result)
            else:
                raise Exception(base.comment)
        except Exception as e:
            raise e

        return list_of_contest

    async def get_contest_rating_changes(self, contest_id: int)->t.Optional[t.List[RatingChange]]:
        list_of_contest_rating_change: t.List[RatingChange] = []
        endpoint_url = self._url_generator.contest_rating_changes(contest_id=contest_id)
        final_url = self._generate_authorisation(
            method_name="contest.list", end_point_url=endpoint_url
        )
        try:
            base = msgspec.json.decode(
                await self._generate_response(url=final_url),
                strict=False,
                type=ContestRatingChangeResponse,
            )
            if base.status != "FAILED":
                if isinstance(base.result, t.List):
                    list_of_contest_rating_change = base.result
                if isinstance(base.result, RatingChange):
                    list_of_contest_rating_change.append(base.result)
            else:
                raise Exception(base.comment)
        except Exception as e:
            raise e

        return list_of_contest_rating_change

    async def close(self):
        await self._client.close()
