import typing as t
import msgspec


class User(msgspec.Struct):
    """
    Represents a Codeforces user.

    Attributes:
        handle (str, optional): Codeforces user handle.
        email (str, optional): Shown only if user allowed to share his contact
        info.
        vkId (str, optional): User id for VK social network. Shown only if user allowed to share his contact info.
        openId (str, optional): Shown only if user allowed to share his contact info.
        firstName (str, optional): Localized. First name of the user. Can be absent.
        lastName (str, optional): Localized. Last name of the user. Can be absent.
        country (str, optional): Localized. Country of the user. Can be absent.
        city (str, optional): Localized. City of the user. Can be absent.
        organization (str, optional): Localized. Organization of the user. Can be absent.
        contribution (int, optional): User's contribution to the Codeforces community.
        rank (str, optional): Localized. Rank of the user.
        rating (int, optional): User's rating in the Codeforces community.
        maxRank (str, optional): Localized. Maximum rank achieved by the user.
        maxRating (int, optional): Maximum rating achieved by the user.
        lastOnlineTimeSeconds (int, optional): Time when user was last seen online, in Unix format.
        registrationTimeSeconds (int, optional): Time when user was registered, in Unix format.
        friendOfCount (int, optional): Amount of users who have this user in friends.
        avatar (str, optional): URL of the user's avatar.
        titlePhoto (str, optional): URL of the user's title photo.

    Note:
        - If any field is absent or not provided, it is represented as `None`.
        - Some fields are localized, meaning they can vary depending on the user's language settings.
        - Time-related fields are represented in Unix format (seconds since epoch).
        - The `email`, `vkId`, and `openId` fields are shown only if the user allows sharing their contact information.
    """

    handle: t.Optional[str] = None
    """Codeforces user handle."""

    vkId: t.Optional[str] = None
    """User id for VK social network. Shown only if user allowed to share his contact info."""

    openId: t.Optional[str] = None
    """Shown only if user allowed to share his contact info."""

    firstName: t.Optional[str] = None
    """Localized. First name of the user. Can be absent."""

    lastName: t.Optional[str] = None
    """Localized. Last name of the user. Can be absent."""

    country: t.Optional[str] = None
    """Localized. Country of the user. Can be absent."""

    city: t.Optional[str] = None
    """Localized. City of the user. Can be absent."""

    organization: t.Optional[str] = None
    """Localized. Organization of the user. Can be absent."""

    contribution: t.Optional[int] = None
    """User's contribution to the Codeforces community."""

    rank: t.Optional[str] = None
    """Localized. Rank of the user."""

    rating: t.Optional[int] = None
    """User's rating in the Codeforces community."""

    maxRank: t.Optional[str] = None
    """Localized. Maximum rank achieved by the user."""

    maxRating: t.Optional[int] = None
    """Maximum rating achieved by the user."""

    lastOnlineTimeSeconds: t.Optional[int] = None
    """Time when user was last seen online, in Unix format."""

    registrationTimeSeconds: t.Optional[int] = None
    """Time when user was registered, in Unix format."""

    friendOfCount: t.Optional[int] = None
    """Amount of users who have this user in friends."""

    avatar: t.Optional[str] = None
    """URL of the user's avatar."""

    titlePhoto: t.Optional[str] = None
    """URL of the user's title photo."""

    email: t.Optional[str] = None
    """Shown only if user allowed to share his contact info."""


class Member(msgspec.Struct):
    """
    Represents a member of a party.

    Attributes:
        handle (str): Codeforces user handle.
        name (str, optional): User's name if available. Can be absent.
    """

    handle: str
    """Codeforces user handle."""

    name: t.Optional[str] = None
    """User's name if available. Can be absent."""


class BlogEntry(msgspec.Struct):
    """
    Represents a Codeforces blog entry. May be in either short or full version.

    Attributes:
        id (int): Unique identifier for the blog entry.
        originalLocale (str): Original locale of the blog entry.
        creationTimeSeconds (int): Time when blog entry was created, in Unix format.
        authorHandle (str): Author's user handle.
        title (str): Localized title of the blog entry.
        content (str, optional): Localized content of the blog entry. Not included in short version.
        locale (str): Locale of the blog entry.
        modificationTimeSeconds (int): Time when blog entry has been updated, in Unix format.
        allowViewHistory (bool): If true, you can view any specific revision of the blog entry.
        tags (List[str]): List of tags associated with the blog entry.
        rating (int): Rating of the blog entry.
    """

    id: t.Optional[int] = None
    """Unique identifier for the blog entry."""

    originalLocale: t.Optional[str] = None
    """Original locale of the blog entry."""

    creationTimeSeconds: t.Optional[int] = None
    """Time when blog entry was created, in Unix format."""

    authorHandle: t.Optional[str] = None
    """Author's user handle."""

    title: t.Optional[str] = None
    """Localized title of the blog entry."""

    content: t.Optional[str] = None
    """Localized content of the blog entry. Not included in short version."""

    locale: t.Optional[str] = None
    """Locale of the blog entry."""

    modificationTimeSeconds: t.Optional[int] = None
    """Time when blog entry has been updated, in Unix format."""

    allowViewHistory: t.Optional[bool] = None
    """If true, you can view any specific revision of the blog entry."""

    tags: t.Optional[t.List[str]] = None
    """List of tags associated with the blog entry."""

    rating: t.Optional[int] = None
    """Rating of the blog entry."""


class Comment(msgspec.Struct):
    """
    Represents a comment.

    Attributes:
        id (int, optional): Unique identifier for the comment.
        creationTimeSeconds (int, optional): Time when the comment was created, in Unix format.
        commentatorHandle (str, optional): Handle of the user who made the comment.
        locale (str, optional): Locale of the comment.
        text (str, optional): Text content of the comment.
        parentCommentId (int, optional): Identifier of the parent comment. Can be absent.
        rating (int, optional): Rating of the comment.
    """

    id: t.Optional[int] = None
    """Unique identifier for the comment."""

    creationTimeSeconds: t.Optional[int] = None
    """Time when the comment was created, in Unix format."""

    commentatorHandle: t.Optional[str] = None
    """Handle of the user who made the comment."""

    locale: t.Optional[str] = None
    """Locale of the comment."""

    text: t.Optional[str] = None
    """Text content of the comment."""

    parentCommentId: t.Optional[int] = None
    """Identifier of the parent comment. Can be absent."""

    rating: t.Optional[int] = None
    """Rating of the comment."""


class RecentAction(msgspec.Struct):
    """
    Represents a recent action.

    Attributes:
        timeSeconds (int): Action time, in Unix format.
        blogEntry (BlogEntry, optional): BlogEntry object in short form. Can be absent.
        comment (Comment, optional): Comment object. Can be absent.
    """

    timeSeconds: t.Optional[int] = None
    """Action time, in Unix format."""

    blogEntry: t.Optional[BlogEntry] = None
    """BlogEntry object in short form. Can be absent."""

    comment: t.Optional[Comment] = None
    """Comment object. Can be absent."""


class RatingChange(msgspec.Struct):
    """
    Represents a participation of a user in a rated contest.

    Attributes:
        contestId (int, optional): Contest ID.
        contestName (str, optional): Localized name of the contest.
        handle (str, optional): Codeforces user handle.
        rank (int, optional): Place of the user in the contest. This field contains user rank at the moment of rating update. If the rank changes afterward (e.g., someone gets disqualified), this field will not be updated and will contain the old rank.
        ratingUpdateTimeSeconds (int, optional): Time when the rating for the contest was updated, in Unix format.
        oldRating (int, optional): User rating before the contest.
        newRating (int, optional): User rating after the contest.
    """

    contestId: t.Optional[int] = None
    """Contest ID."""

    contestName: t.Optional[str] = None
    """Localized name of the contest."""

    handle: t.Optional[str] = None
    """Codeforces user handle."""

    rank: t.Optional[int] = None
    """Place of the user in the contest. This field contains user rank at the moment of rating update. If the rank changes afterward (e.g., someone gets disqualified), this field will not be updated and will contain the old rank."""

    ratingUpdateTimeSeconds: t.Optional[int] = None
    """Time when the rating for the contest was updated, in Unix format."""

    oldRating: t.Optional[int] = None
    """User rating before the contest."""

    newRating: t.Optional[int] = None
    """User rating after the contest."""


class Contest(msgspec.Struct):
    """
    Represents a contest on Codeforces.

    Attributes:
        id (int, optional): Contest ID.
        name (str, optional): Localized name of the contest.
        type (str, optional): Enum: CF, IOI, ICPC. Scoring system used for the contest.
        phase (str, optional): Enum: BEFORE, CODING, PENDING_SYSTEM_TEST, SYSTEM_TEST, FINISHED.
        frozen (bool, optional): If true, then the ranklist for the contest is frozen and shows only submissions created before freeze.
        durationSeconds (int, optional): Duration of the contest in seconds.
        startTimeSeconds (int, optional): Contest start time in Unix format. Can be absent.
        relativeTimeSeconds (int, optional): Number of seconds passed after the start of the contest. Can be negative. Can be absent.
        preparedBy (str, optional): Handle of the user who created the contest. Can be absent.
        websiteUrl (str, optional): URL for contest-related website. Can be absent.
        description (str, optional): Localized description of the contest. Can be absent.
        difficulty (int, optional): From 1 to 5. Larger number means more difficult problems. Can be absent.
        kind (str, optional): Localized human-readable type of the contest. Can be absent. Categories may include: Official ICPC Contest, Official School Contest, Opencup Contest, School/University/City/Region Championship, Training Camp Contest, Official International Personal Contest, Training Contest.
        icpcRegion (str, optional): Localized name of the Region for official ICPC contests. Can be absent.
        country (str, optional): Localized name of the country. Can be absent.
        city (str, optional): Localized name of the city. Can be absent.
        season (str, optional): Can be absent.
    """

    id: t.Optional[int] = None
    """Contest ID."""

    name: t.Optional[str] = None
    """Localized name of the contest."""

    type: t.Optional[str] = None
    """Enum: CF, IOI, ICPC. Scoring system used for the contest."""

    phase: t.Optional[str] = None
    """Enum: BEFORE, CODING, PENDING_SYSTEM_TEST, SYSTEM_TEST, FINISHED."""

    frozen: t.Optional[bool] = None
    """If true, then the ranklist for the contest is frozen and shows only submissions created before freeze."""

    durationSeconds: t.Optional[int] = None
    """Duration of the contest in seconds."""

    startTimeSeconds: t.Optional[int] = None
    """Contest start time in Unix format. Can be absent."""

    relativeTimeSeconds: t.Optional[int] = None
    """Number of seconds passed after the start of the contest. Can be negative. Can be absent."""

    preparedBy: t.Optional[str] = None
    """Handle of the user who created the contest. Can be absent."""

    websiteUrl: t.Optional[str] = None
    """URL for contest-related website. Can be absent."""

    description: t.Optional[str] = None
    """Localized description of the contest. Can be absent."""

    difficulty: t.Optional[int] = None
    """From 1 to 5. Larger number means more difficult problems. Can be absent."""

    kind: t.Optional[str] = None
    """Localized human-readable type of the contest. Can be absent. Categories may include: Official ICPC Contest, Official School Contest, Opencup Contest, School/University/City/Region Championship, Training Camp Contest, Official International Personal Contest, Training Contest."""

    icpcRegion: t.Optional[str] = None
    """Localized name of the Region for official ICPC contests. Can be absent."""

    country: t.Optional[str] = None
    """Localized name of the country. Can be absent."""

    city: t.Optional[str] = None
    """Localized name of the city. Can be absent."""

    season: t.Optional[str] = None
    """Can be absent."""


class Party(msgspec.Struct):
    """
    Represents a party, participating in a contest.

    Attributes:
        contestId (int, optional): Id of the contest in which the party is participating. Can be absent.
        members (List[Member], optional): Members of the party.
        participantType (str, optional): Enum: CONTESTANT, PRACTICE, VIRTUAL, MANAGER, OUT_OF_COMPETITION.
        teamId (int, optional): If the party is a team, then it is a unique team id. Otherwise, this field is absent.
        teamName (str, optional): Localized name of the team if the party is a team or ghost. Otherwise, it is absent.
        ghost (bool, optional): If true then this party is a ghost. It participated in the contest, but not on Codeforces.
        room (int, optional): Room of the party. If absent, then the party has no room.
        startTimeSeconds (int, optional): Time when this party started a contest. Can be absent.
    """

    contestId: t.Optional[int] = None
    """Id of the contest in which the party is participating. Can be absent."""

    members: t.Optional[t.List[Member]] = None
    """Members of the party. Can be absent."""

    participantType: t.Optional[str] = None
    """Enum: CONTESTANT, PRACTICE, VIRTUAL, MANAGER, OUT_OF_COMPETITION."""

    teamId: t.Optional[int] = None
    """If the party is a team, then it is a unique team id. Otherwise, this field is absent."""

    teamName: t.Optional[str] = None
    """Localized name of the team if the party is a team or ghost. Otherwise, it is absent."""

    ghost: t.Optional[bool] = None
    """If true then this party is a ghost. It participated in the contest, but not on Codeforces."""

    room: t.Optional[int] = None
    """Room of the party. If absent, then the party has no room."""

    startTimeSeconds: t.Optional[int] = None
    """Time when this party started a contest. Can be absent."""


class Problem(msgspec.Struct):
    """
    Represents a problem.

    Attributes:
        contestId (int, optional): Id of the contest containing the problem. Can be absent.
        problemsetName (str, optional): Short name of the problemset the problem belongs to. Can be absent.
        index (str, optional): Usually, a letter or letter with digit(s) indicating the problem index in a contest.
        name (str, optional): Localized name of the problem.
        type (str, optional): Enum: PROGRAMMING, QUESTION.
        points (float, optional): Maximum amount of points for the problem. Can be absent.
        rating (int, optional): Problem rating (difficulty). Can be absent.
        tags (List[str], optional): Problem tags.
    """

    contestId: t.Optional[int] = None
    """Id of the contest containing the problem. Can be absent."""

    problemsetName: t.Optional[str] = None
    """Short name of the problemset the problem belongs to. Can be absent."""

    index: t.Optional[str] = None
    """Usually, a letter or letter with digit(s) indicating the problem index in a contest."""

    name: t.Optional[str] = None
    """Localized name of the problem."""

    type: t.Optional[str] = None
    """Enum: PROGRAMMING, QUESTION."""

    points: t.Optional[float] = None
    """Maximum amount of points for the problem. Can be absent."""

    rating: t.Optional[int] = None
    """Problem rating (difficulty). Can be absent."""

    tags: t.Optional[t.List[str]] = None
    """Problem tags."""


class ProblemStatistics(msgspec.Struct):
    """
    Represents statistic data about a problem.

    Attributes:
        contestId (int, optional): Id of the contest containing the problem. Can be absent.
        index (str, optional): Usually, a letter or letter with digit(s) indicating the problem index in a contest.
        solvedCount (int, optional): Number of users who solved the problem.
    """

    contestId: t.Optional[int] = None
    """Id of the contest containing the problem. Can be absent."""

    index: t.Optional[str] = None
    """Usually, a letter or letter with digit(s) indicating the problem index in a contest."""

    solvedCount: t.Optional[int] = None
    """Number of users who solved the problem."""


class Submission(msgspec.Struct):
    """
    Represents a submission.

    Attributes:
        id (int): Unique identifier for the submission.
        contestId (int, optional): Id of the contest, can be absent.
        creationTimeSeconds (int): Time when submission was created, in Unix format.
        relativeTimeSeconds (int): Number of seconds passed after the start of the contest (or a virtual start for virtual parties), before the submission.
        problem (Problem, optional): Problem object.
        author (Party, optional): Party object.
        programmingLanguage (str): Programming language used for the submission.
        verdict (str, optional): Enum: FAILED, OK, PARTIAL, COMPILATION_ERROR, RUNTIME_ERROR, WRONG_ANSWER, PRESENTATION_ERROR, TIME_LIMIT_EXCEEDED, MEMORY_LIMIT_EXCEEDED, IDLENESS_LIMIT_EXCEEDED, SECURITY_VIOLATED, CRASHED, INPUT_PREPARATION_CRASHED, CHALLENGED, SKIPPED, TESTING, REJECTED. Can be absent.
        testset (str, optional): Enum: SAMPLES, PRETESTS, TESTS, CHALLENGES, TESTS1, ..., TESTS10. Testset used for judging the submission.
        passedTestCount (int, optional): Number of passed tests.
        timeConsumedMillis (int, optional): Maximum time in milliseconds, consumed by solution for one test.
        memoryConsumedBytes (int, optional): Maximum memory in bytes, consumed by solution for one test.
        points (float, optional): Number of scored points for IOI-like contests. Can be absent.
    """

    id: int
    """Unique identifier for the submission."""

    contestId: t.Optional[int] = None
    """Id of the contest, can be absent."""

    creationTimeSeconds: t.Optional[int] = None
    """Time when submission was created, in Unix format."""

    relativeTimeSeconds: t.Optional[int] = None
    """Number of seconds passed after the start of the contest (or a virtual start for virtual parties), before the submission."""

    problem: t.Optional[Problem] = None
    """Problem object."""

    author: t.Optional[Party] = None
    """Party object."""

    programmingLanguage: t.Optional[str] = None
    """Programming language used for the submission."""

    verdict: t.Optional[str] = None
    """Enum: FAILED, OK, PARTIAL, COMPILATION_ERROR, RUNTIME_ERROR, WRONG_ANSWER, PRESENTATION_ERROR, TIME_LIMIT_EXCEEDED, MEMORY_LIMIT_EXCEEDED, IDLENESS_LIMIT_EXCEEDED, SECURITY_VIOLATED, CRASHED, INPUT_PREPARATION_CRASHED, CHALLENGED, SKIPPED, TESTING, REJECTED. Can be absent."""

    testset: t.Optional[str] = None
    """Enum: SAMPLES, PRETESTS, TESTS, CHALLENGES, TESTS1, ..., TESTS10. Testset used for judging the submission."""

    passedTestCount: t.Optional[int] = None
    """Number of passed tests."""

    timeConsumedMillis: t.Optional[int] = None
    """Maximum time in milliseconds, consumed by solution for one test."""

    memoryConsumedBytes: t.Optional[int] = None
    """Maximum memory in bytes, consumed by solution for one test."""

    points: t.Optional[float] = None
    """Number of scored points for IOI-like contests. Can be absent."""


class Hack(msgspec.Struct):
    """
    Represents a hack, made during a Codeforces Round.

    Attributes:
        id (int): Unique identifier for the hack.
        creationTimeSeconds (int): Hack creation time in Unix format.
        hacker (Party, optional): Party object representing the hacker.
        defender (Party, optional): Party object representing the defender.
        verdict (str, optional): Enum: HACK_SUCCESSFUL, HACK_UNSUCCESSFUL, INVALID_INPUT, GENERATOR_INCOMPILABLE, GENERATOR_CRASHED, IGNORED, TESTING, OTHER. Can be absent.
        problem (Problem, optional): Problem object representing the hacked problem.
        test (str, optional): Can be absent.
        judgeProtocol (object, optional): Object with three fields: "manual", "protocol" and "verdict". Field manual can have values "true" and "false". If manual is "true" then test for the hack was entered manually. Fields "protocol" and "verdict" contain human-readable description of judge protocol and hack verdict. Localized. Can be absent.
    """

    id: int
    """Unique identifier for the hack."""

    creationTimeSeconds: int
    """Hack creation time in Unix format."""

    hacker: t.Optional[Party] = None
    """Party object representing the hacker."""

    defender: t.Optional[Party] = None
    """Party object representing the defender."""

    verdict: t.Optional[str] = None
    """Enum: HACK_SUCCESSFUL, HACK_UNSUCCESSFUL, INVALID_INPUT, GENERATOR_INCOMPILABLE, GENERATOR_CRASHED, IGNORED, TESTING, OTHER. Can be absent."""

    problem: t.Optional[Problem] = None
    """Problem object representing the hacked problem."""

    test: t.Optional[str] = None
    """Can be absent."""

    judgeProtocol: t.Optional[t.Dict[str, str]] = None
    """
    Object with three fields: "manual", "protocol" and "verdict".
    Field manual can have values "true" and "false". If manual is "true" then test for the hack was entered manually.
    Fields "protocol" and "verdict" contain human-readable description of judge protocol and hack verdict. Localized.
    Can be absent.
    """


class ProblemResult(msgspec.Struct):
    """
    Represents a submissions results of a party for a problem.

    Attributes:
        points (float, optional): Floating point number.
        penalty (int, optional): Penalty (in ICPC meaning) of the party for this problem. Can be absent.
        rejectedAttemptCount (int, optional): Number of incorrect submissions.
        type (str, optional): Enum: PRELIMINARY, FINAL. If type is PRELIMINARY then points can decrease (if, for example, solution will fail during system test). Otherwise, party can only increase points for this problem by submitting better solutions.
        bestSubmissionTimeSeconds (int, optional): Number of seconds after the start of the contest before the submission, that brought maximal amount of points for this problem. Can be absent.
    """

    points: t.Optional[float] = None
    """Floating point number."""

    penalty: t.Optional[int] = None
    """Penalty (in ICPC meaning) of the party for this problem. Can be absent."""

    rejectedAttemptCount: t.Optional[int] = None
    """Number of incorrect submissions."""

    type: t.Optional[str] = None
    """Enum: PRELIMINARY, FINAL. If type is PRELIMINARY then points can decrease (if, for example, solution will fail during system test). Otherwise, party can only increase points for this problem by submitting better solutions."""

    bestSubmissionTimeSeconds: t.Optional[int] = None
    """Number of seconds after the start of the contest before the submission, that brought maximal amount of points for this problem. Can be absent."""


class RankListRow(msgspec.Struct):
    """
    Represents a ranklist row.

    Attributes:
        party (Party, optional): Party object representing the party that took a corresponding place in the contest.
        rank (int, optional): Party place in the contest.
        points (float, optional): Total amount of points scored by the party.
        penalty (int, optional): Total penalty (in ICPC meaning) of the party.
        successfulHackCount (int, optional): Number of successful hacks performed by the party.
        unsuccessfulHackCount (int, optional): Number of unsuccessful hacks performed by the party.
        problemResults (List[ProblemResult], optional): Party results for each problem. Order of the problems is the same as in the "problems" field of the returned object.
        lastSubmissionTimeSeconds (int, optional): For IOI contests only. Time in seconds from the start of the contest to the last submission that added some points to the total score of the party. Can be absent.
    """

    party: t.Optional[Party] = None
    """Party object representing the party that took a corresponding place in the contest."""

    rank: t.Optional[int] = None
    """Party place in the contest."""

    points: t.Optional[float] = None
    """Total amount of points scored by the party."""

    penalty: t.Optional[int] = None
    """Total penalty (in ICPC meaning) of the party."""

    successfulHackCount: t.Optional[int] = None
    """Number of successful hacks performed by the party."""

    unsuccessfulHackCount: t.Optional[int] = None
    """Number of unsuccessful hacks performed by the party."""

    problemResults: t.Optional[t.List[ProblemResult]] = None
    """Party results for each problem. Order of the problems is the same as in the "problems" field of the returned object."""

    lastSubmissionTimeSeconds: t.Optional[int] = None
    """
    For IOI contests only. Time in seconds from the start of the contest to the last submission that added some points to the total score of the party.
    Can be absent.
    """
