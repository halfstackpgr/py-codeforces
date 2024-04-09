import msgspec
import typing as t
from pycodeforces.abc.__objects__ import Problem, Contest, RankListRow, ProblemStatistics


class Standings(msgspec.Struct):
    contest: t.Optional[t.Union[t.List[Contest], Contest]] = None
    problems: t.Optional[t.Union[t.List[Problem], Problem]] = None
    rows: t.Optional[t.Union[t.List[RankListRow], RankListRow]] = None


class ProblemSetProblems(msgspec.Struct):
    problems: t.Optional[t.Union[t.List[Problem], Problem]]
    problemStatistics: t.Optional[t.Union[t.List[ProblemStatistics], ProblemStatistics]]
