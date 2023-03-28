from class_League import League


class EPL(League):
    """
    A child class of class League to store EPL rules and additional attributes
    --------------------------------------------------------------------------

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
    points:
        returns the number of points (wins*3 + draws)

    """
    def __init__(self, league: str, team: str, stadium: str, location: str):
        """
        Constructor method for the class: EPL
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
        super().__init__(league, team, stadium, location)

    @property
    def points(self):
        """
        Returns the number of points in accordance to the EPL rules
        a win equals 3 points
        a draw equals 1 point
        ...
        :return: returns the number points (wins*3 + draws)
        :rtype: int
        """
        self._points = ((self._wins * 3) + self._draws)
        return self._points

