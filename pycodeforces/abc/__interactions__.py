import msgspec
import typing as t
from pycodeforces.abc.__objects__ import (
    User,
    Comment,
    BlogEntry,
    Hack,
    Contest,
    RatingChange,
    Submission,
    RecentAction,
)
from pycodeforces.abc.__cobjects__ import Standings, ProblemSetProblems


class InteractionResponse(msgspec.Struct):
    status: str
    comment: t.Optional[str] = None


class UserInteractionResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[User], User]] = None


class BlogEntryCommentResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[Comment], Comment]] = None


class BlogEntryViewResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[BlogEntry], BlogEntry]] = None


class ContestHacksResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[Hack], Hack]] = None


class ContestListResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[Contest], Contest]] = None


class ContestRatingChangeResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[RatingChange], RatingChange]] = None


class ContestStandingResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[Standings], Standings]] = None


class ContestStatusResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[Submission], Submission]] = None


class ProblemSetProblemsResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[ProblemSetProblems], ProblemSetProblems]] = None


class ProblemSetRecentStatusResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[Submission], Submission]] = None


class RecentActionsResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[RecentAction], RecentAction]] = None


class UserBlogEntryResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[BlogEntry], BlogEntry]] = None


class UserFriendResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[str], str]] = None


class UserRatedListResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[User], User]] = None


class UserRatingResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[RatingChange], RatingChange]] = None


class UserStatusResponse(InteractionResponse):
    result: t.Optional[t.Union[t.List[Submission], Submission]] = None
