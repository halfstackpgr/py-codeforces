import msgspec
import typing as t
from pycodeforce.abc.objects import (
    User,
    Comment,
    BlogEntry,
    Hack,
    Contest, 
    RatingChange,
    Submission
)
from pycodeforce.abc.cobjects import (
    Standings,
    ProblemSetProblems
)

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
