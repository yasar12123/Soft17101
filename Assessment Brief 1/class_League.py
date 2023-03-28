
class League:
    """
    A class to store football league statistics
    -------------------------------------------

    Attributes
    ----------
    _league : str
        The name of the league
    _team : str
        The name of the team
    _stadium : str
         The home stadium of the team
    _location : str
         The location where the team is based

    Methods
    -------
    goals_scored:
        returns the number of goals scored
        sets the number of goals scored
    goals_conceded:
        returns the number of goals conceded
        sets the number of goals conceded
    wins:
        returns the number of wins
        sets the number of wins
    losses:
        returns the number of losses
        sets the number of losses
    draws:
        returns the number of draws
        sets the number of draws
    top_goal_scorer:
        returns the teams top goal scorer
        sets the teams top goal scorer
    manager:
        returns the teams manager
        sets the teams manager
    goal_difference:
        returns goal difference (goals scored - goals conceded)
    points:
        returns the number of points (default 0)
    team:
        returns the name of the team
    """

    """
    This flag indicates if the class has been initialised with objects.
    initiated:
        True if object has been initialised otherwise False.
    """
    initiated = False

    def __init__(self, league: str, team: str, stadium: str, location: str):
        """
        Constructor method for the class: League
        ...
        :param league : The name of the league
        :type league: str
        :param team : The name of the team
        :type team: str
        :param stadium : The home stadium of the team
        :type stadium: str
        :param location : The location where the team is based
        :type location: str
        """
        self._league = league
        self._team = team
        self._stadium = stadium
        self._location = location
        self._manager = 'Unassigned'
        self._top_goal_scorer = 'Unassigned'
        self._wins = 0
        self._draws = 0
        self._losses = 0
        self._goals_scored = 0
        self._goals_conceded = 0
        self._points = 0
        League.initiated = True

    @property
    def goals_scored(self):
        """
        Get or set the number of goals scored
        ...
        :raises ValueError: The new value needs to be an integer or a positive number
        ...
        :return: returns the number of goals scored
        :rtype: int
        """
        return self._goals_scored

    @goals_scored.setter
    def goals_scored(self, goals_scored):
        if type(goals_scored) != int:
            raise ValueError("The input {} needs to be an integer".format(goals_scored))
        if goals_scored < 0:
            raise ValueError("The input {} is a negative number".format(goals_scored))
        else:
            self._goals_scored = goals_scored

    @property
    def goals_conceded(self):
        """
        Get or set the number of goals conceded
        ...
        :raises ValueError: The new value needs to be an integer or a positive number
        ...
        :return: returns the number of goals conceded
        :rtype: int
        """
        return self._goals_conceded

    @goals_conceded.setter
    def goals_conceded(self, goals_conceded):
        if type(goals_conceded) != int:
            raise ValueError("The input {} needs to be an integer".format(goals_conceded))
        if goals_conceded < 0:
            raise ValueError("The input {} is a negative number".format(goals_conceded))
        else:
            self._goals_conceded = goals_conceded

    @property
    def wins(self):
        """
        Get or set the number of matches won
        ...
        :raises ValueError: The new value needs to be an integer or a positive number
        ...
        :return: returns the number of matches won
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        if type(wins) != int:
            raise ValueError("The input {} needs to be an integer".format(wins))
        if wins < 0:
            raise ValueError("The input {} is a negative number".format(wins))
        else:
            self._wins = wins

    @property
    def losses(self):
        """
        Get or set the number of matches lost
        ...
        :raises ValueError: The new value needs to be an integer or a positive number
        ...
        :return: returns the number of matches lost
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        if type(losses) != int:
            raise ValueError("The input {} needs to be an integer".format(losses))
        if losses < 0:
            raise ValueError("The input {} is a negative number".format(losses))
        else:
            self._losses = losses

    @property
    def draws(self):
        """
        Get or set the number of matches drawn
        ...
        :raises ValueError: The new value needs to be an integer or a positive number
        ...
        :return: returns the number of matches drawn
        :rtype: int
        """
        return self._draws

    @draws.setter
    def draws(self, draws):
        if type(draws) != int:
            raise ValueError("The input {} needs to be an integer".format(draws))
        if draws < 0:
            raise ValueError("The input {} is a negative number".format(draws))
        else:
            self._draws = draws

    @property
    def goal_difference(self):
        """
        Returns the goal difference.
        The number of goals scored minus the number of goals conceded
        ...
        :return: returns the goal difference (goals scored - goals conceded)
        :rtype: int
        """
        goal_difference = self._goals_scored - self._goals_conceded
        return goal_difference

    @property
    def top_goal_scorer(self):
        """
        Get or set the teams top goal-scorer
        ...
        :raises ValueError: The new value needs to be a string
        ...
        :return: returns teams top goal-scorer
        :rtype: str
        """
        return self._top_goal_scorer

    @top_goal_scorer.setter
    def top_goal_scorer(self, new_top_goal_scorer: str):
        if type(new_top_goal_scorer) != str:
            raise ValueError("The input {} needs to be a string".format(new_top_goal_scorer))
        else:
            self._top_goal_scorer = new_top_goal_scorer

    @property
    def manager(self):
        """
        Get or set the teams manager
        ...
        :raises ValueError: The new value needs to be a string
        ...
        :return: returns teams manager
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, new_manager: str):
        if type(new_manager) != str:
            raise ValueError("The input {} needs to be a string".format(new_manager))
        else:
            self._manager = new_manager

    @property
    def team(self):
        """
        returns the name of the team
        ...
        :return: returns the name of the team
        :rtype: str
        """
        return self._team

    def __str__(self):
        """
        Returns the stats and info of a team.
        ...
        :return: The league, team name, stadium, location, manager, top goal scorer,
                 wins, draws, losses, goals scored, goals conceded and goal difference
        :rtype: str
        """
        return ('\n' "League: " + str(self._league) +
                '\n' "Team: " + str(self._team) +
                '\n' "Stadium: " + str(self._stadium) +
                '\n' "Location: " + str(self._location) +
                '\n' "Manager: " + str(self._manager) +
                '\n' "Top goal scorer: " + str(self._top_goal_scorer) +
                '\n' "Wins: " + str(self._wins) +
                '\n' "Draws: " + str(self._draws) +
                '\n' "Losses: " + str(self._losses) +
                '\n' "Goals scored: " + str(self._goals_scored) +
                '\n' "Goals conceded: " + str(self._goals_conceded) +
                '\n' "Goal difference: " + str(self.goal_difference))

