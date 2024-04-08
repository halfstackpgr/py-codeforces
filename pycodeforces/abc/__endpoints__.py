from typing import Optional


class CodeForcesAPI:
    """A class to generate URL endpoints for Codeforces API."""

    def __init__(self) -> None:
        self.base_url = "https://codeforces.com/api"

    def blog_entry_comments(self, blog_entry_id: int) -> str:
        """
        Generate URL endpoint to retrieve comments for a specific blog entry.

        Args:
            blog_entry_id (int): The ID of the blog entry.

        Returns:
            str: The generated URL endpoint.
        """
        return f"{self.base_url}/blogEntry.comments?blogEntryId={blog_entry_id}"

    def blog_entry_view(self, blog_entry_id: int) -> str:
        """
        Generate URL endpoint to retrieve a specific blog entry.

        Args:
            blog_entry_id (int): The ID of the blog entry.

        Returns:
            str: The generated URL endpoint.
        """
        return f"{self.base_url}/blogEntry.view?blogEntryId={blog_entry_id}"

    def contest_hacks(self, contest_id: int, as_manager: Optional[bool] = False) -> str:
        """
        Generate URL endpoint to retrieve hacks for a specific contest.

        Args:
            contest_id (int): The ID of the contest.
            as_manager (Optional[bool]): Boolean indicating if the user is a contest manager.

        Returns:
            str: The generated URL endpoint.
        """
        return f"{self.base_url}/contest.hacks?contestId={contest_id}&asManager={as_manager}"

    def contest_list(self, gym: Optional[bool] = False) -> str:
        """
        Generate URL endpoint to retrieve information about all available contests.

        Args:
            gym (Optional[bool]): Boolean indicating if gym contests should be returned.

        Returns:
            str: The generated URL endpoint.
        """
        return f"{self.base_url}/contest.list?gym={gym}"

    def contest_rating_changes(self, contest_id: int) -> str:
        """
        Generate URL endpoint to retrieve rating changes after a contest.

        Args:
            contest_id (int): The ID of the contest.

        Returns:
            str: The generated URL endpoint.
        """
        return f"{self.base_url}/contest.ratingChanges?contestId={contest_id}"

    def contest_standings(
        self,
        contest_id: int,
        as_manager: Optional[bool] = False,
        from_index: int = 1,
        count: int = 5,
        show_unofficial: Optional[bool] = True,
    ) -> str:
        """
        Generate URL endpoint to retrieve the description of a contest and the requested part of the standings.

        Args:
            contest_id (int): The ID of the contest.
            as_manager (Optional[bool]): Boolean indicating if the user is a contest manager.
            from_index (int): 1-based index of the standings row to start the ranklist.
            count (int): Number of standing rows to return.
            show_unofficial (Optional[bool]): Boolean indicating if unofficial contestants should be shown.

        Returns:
            str: The generated URL endpoint.
        """
        return (
            f"{self.base_url}/contest.standings?contestId={contest_id}&asManager={as_manager}"
            f"&from={from_index}&count={count}&showUnofficial={show_unofficial}"
        )

    def contest_status(
        self,
        contest_id: int,
        as_manager: Optional[bool] = False,
        handle: Optional[str] = None,
        from_index: int = 1,
        count: int = 10,
    ) -> str:
        """
        Generate URL endpoint to retrieve submissions for a specified contest.

        Args:
            contest_id (int): The ID of the contest.
            as_manager (Optional[bool]): Boolean indicating if the user is a contest manager.
            handle (Optional[str]): Codeforces user handle.
            from_index (int): 1-based index of the first submission to return.
            count (int): Number of returned submissions.

        Returns:
            str: The generated URL endpoint.
        """
        if handle:
            return (
                f"{self.base_url}/contest.status?contestId={contest_id}&asManager={as_manager}"
                f"&handle={handle}&from={from_index}&count={count}"
            )
        else:
            return f"{self.base_url}/contest.status?contestId={contest_id}&asManager={as_manager}&from={from_index}&count={count}"

    def problemset_problems(
        self, tags: Optional[str] = None, problemset_name: Optional[str] = None
    ) -> str:
        """
        Generate URL endpoint to retrieve all problems from the problemset.

        Args:
            tags (Optional[str]): Semicolon-separated list of tags.
            problemset_name (Optional[str]): Custom problemset's short name.

        Returns:
            str: The generated URL endpoint.
        """
        if tags:
            return f"{self.base_url}/problemset.problems?tags={tags}"
        elif problemset_name:
            return (
                f"{self.base_url}/problemset.problems?problemsetName={problemset_name}"
            )
        else:
            return f"{self.base_url}/problemset.problems"

    def problemset_recent_status(
        self, count: int, problemset_name: Optional[str] = None
    ) -> str:
        """
        Generate URL endpoint to retrieve recent submissions.

        Args:
            count (int): Number of submissions to return.
            problemset_name (Optional[str]): Custom problemset's short name.

        Returns:
            str: The generated URL endpoint.
        """
        if problemset_name:
            return f"{self.base_url}/problemset.recentStatus?count={count}&problemsetName={problemset_name}"
        else:
            return f"{self.base_url}/problemset.recentStatus?count={count}"

    def recent_actions(self, max_count: int) -> str:
        """
        Generate URL endpoint to retrieve recent actions.

        Args:
            max_count (int): Number of recent actions to return.

        Returns:
            str: The generated URL endpoint.
        """
        return f"{self.base_url}/recentActions?maxCount={max_count}"

    def user_blog_entries(self, handle: str) -> str:
        """
        Generate URL endpoint to retrieve a list of all user's blog entries.

        Args:
            handle (str): Codeforces user handle.

        Returns:
            str: The generated URL endpoint.
        """
        return f"{self.base_url}/user.blogEntries?handle={handle}"

    def user_friends(self, only_online: Optional[bool] = False) -> str:
        """
        Generate URL endpoint to retrieve authorized user's friends.

        Args:
            only_online (Optional[bool]): Boolean indicating if only online friends should be returned.

        Returns:
            str: The generated URL endpoint.
        """
        return f"{self.base_url}/user.friends?onlyOnline={only_online}"

    def user_info(
        self, handles: str, check_historic_handles: Optional[bool] = True
    ) -> str:
        """
        Generate URL endpoint to retrieve information about one or several users.

        Args:
            handles (str): Semicolon-separated list of handles.
            check_historic_handles (Optional[bool]): Boolean indicating if historical handles should be checked.

        Returns:
            str: The generated URL endpoint.
        """
        return f"{self.base_url}/user.info?handles={handles}&checkHistoricHandles={check_historic_handles}"

    def user_rated_list(
        self,
        active_only: Optional[bool] = True,
        include_retired: Optional[bool] = False,
        contest_id: Optional[int] = None,
    ) -> str:
        """
        Generate URL endpoint to retrieve the list of users who have participated in at least one rated contest.

        Args:
            active_only (Optional[bool]): Boolean indicating if only active users should be returned.
            include_retired (Optional[bool]): Boolean indicating if retired users should be included.
            contest_id (Optional[int]): ID of the contest.

        Returns:
            str: The generated URL endpoint.
        """
        if contest_id:
            return f"{self.base_url}/user.ratedList?activeOnly={active_only}&includeRetired={include_retired}&contestId={contest_id}"
        else:
            return f"{self.base_url}/user.ratedList?activeOnly={active_only}&includeRetired={include_retired}"

    def user_rating(self, handle: str) -> str:
        """
        Generate URL endpoint to retrieve rating history of the specified user.

        Args:
            handle (str): Codeforces user handle.

        Returns:
            str: The generated URL endpoint.
        """
        return f"{self.base_url}/user.rating?handle={handle}"

    def user_status(self, handle: str, from_index: int = 1, count: int = 10) -> str:
        """
        Generate URL endpoint to retrieve submissions of specified user.

        Args:
            handle (str): Codeforces user handle.
            from_index (int): 1-based index of the first submission to return.
            count (int): Number of returned submissions.

        Returns:
            str: The generated URL endpoint.
        """
        return f"{self.base_url}/user.status?handle={handle}&from={from_index}&count={count}"
