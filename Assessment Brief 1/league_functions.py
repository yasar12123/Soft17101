import os
import pickle
import random
import re
import sys

# name of class modules that should be found by the str_to_class function
# they will be greyed out due to them not being directly used
from class_EPL import EPL

def check_file_format(path_file_name: str):
    """
    This functions checks the format of each line
    if a line from the txt file is not in the correct format "team: stadium - location"
    then an error is raised
    ...
    :param path_file_name: path\file name
    :type path_file_name: str
    ...
    :raises ValueError: Incorrect format
    ...
    """
    file = open(path_file_name, "r")
    line_format = re.compile('.*: .* - .*')
    #check each line fits with the format above
    for lineNumber, line in enumerate(file):
        if line_format.match(line) is None:
            raise ValueError(f'Error! Incorrect format, file: {path_file_name}'
                             f', line number: {lineNumber}, Line: {line}')
    file.close()


def txt_line_to_lists(path_file_name: str, delimiters):
    """
    This functions takes a txt file and turns each line into a list
    each line is then split into elements by the delimiters provided.
    ...
    :param path_file_name: path\file name
    :type path_file_name: str
    :param delimiters: delimiters can be put into a list or tuples
    :type delimiters: str
    ...
    :raises ValueError: The provided delimiters need to be in string format
    ...
    :return: returns a list with each line in a list containing elements split by the delimiters
    :rtype: list
    """
    #check if the delimiters are strings, if not then raise a value error
    for deli in delimiters:
        if not isinstance(deli, str):
            raise ValueError('The provided delimiters need to be in string format')

    file = open(path_file_name, "r")
    list_final = []
    #this loops around each line of data in the text file
    for line in file:
        line_to_deli = line
        #this loops around the delimiters provided and splits each occurrence into an element of a list
        for deli in delimiters:
            line_to_deli = line_to_deli.replace(deli, ',').strip()
        line_list = line_to_deli.split(',')
        #this loops each element and removes the leading and trailing empty space
        for stripPosition, strip in enumerate(line_list):
            line_list[stripPosition] = line_list[stripPosition].strip()
        list_final.insert(0, line_list)
    list_final.reverse()
    file.close()
    return list_final

def str_to_class(name_of_class):
    """
    This function converts a string and returns the class module if it is found.
    if not then a ModuleNotFoundError is raised.
    ...
    :param name_of_class: name of class to parse
    :type name_of_class: str
    ...
    :raises ModuleNotFoundError: if the class module can not be found
    ...
    :return: returns the class module
    :rtype: class
    """
    try:
        getattr(sys.modules[__name__], name_of_class)
    except AttributeError:
        raise ModuleNotFoundError(f'{name_of_class}: module can not be found')
    else:
        return getattr(sys.modules[__name__], name_of_class)


def initialise_child_league(league_name: str, file_path: str, class_league: str):
    """
    This function is used to set up a football league for the class specified
    It takes the list generated from the function txt_line_to_lists and initialises them
    through the class, each class object is then placed into a list.
    ...
    :param league_name: name of the football league e.g. EPL
    :type league_name: str
    :param file_path: path\file name
    :type file_path: str
    :param class_league: name of the class to initialise objects in
    :type class_league: str
    ...
    :raises FileNotFoundError: the provided path\file can not be found
    ...
    :return: returns a list of objects for the class
    :rtype: list
    """
    #change string to class if it exists
    child_class_league = str_to_class(class_league)

    #check if file exists
    if os.path.exists(file_path):
        team_info_list = [(txt_line_to_lists(file_path, [":", "-"]))]
        team_info_list = team_info_list[0]
        #initalise list into the class EPL
        list_of_objects = []
        for teamPosition, teamInfo in enumerate(team_info_list):
            list_of_objects.append(child_class_league(league_name, team_info_list[teamPosition][0],
                                   team_info_list[teamPosition][1], team_info_list[teamPosition][2]))
        return list_of_objects

    else:
        raise FileNotFoundError(f'the provided path/file: {file_path} can not be found')


def save_objects(object_list: list, file: str):
    """
    This function is used to save an object list to a .pkl file.
    ...
    :param object_list: a list of objects
    :type object_list: list
    :param file: path\file name to save into
    :type file: str
    """
    file_path = open(file, 'wb')
    pickle.dump(object_list, file_path)
    file_path.close()


def load_objects(file: str):
    """
    This function is used to load a list of objects from a .pkl file
    ...
    :param file: path\file name to load from
    :type file: str
    ...
    :raises FileNotFoundError: the provided path\file can not be found
    ...
    :return: returns a list of objects
    :rtype: list
    """
    if os.path.exists(file) and os.stat(file).st_size > 0:
        file_path = open(file, 'rb')
        load_file = pickle.load(file_path)
        file_path.close()
        return load_file
    else:
        raise FileNotFoundError('the provided path/file can not be found')


def league_score_board(object_list: list):
    """
    This function takes a list of objects which have been initialised through the class: League
    and converts it to a league score board. The teams are then ordered
    by points, goal difference and goals scored in a descending manner
    ...
    :param object_list: list of objects
    :type object_list: list
    ...
    :return: returns a league table of teams ordered by points, goal difference and goals scored in a descending manner
    :rtype: dataframe
    """
    #sort teams by points, goal diff, goals scored in a descending manner
    sorted_list = sorted(object_list, key=lambda league: (-league.points,
                                                          -league.goal_difference,
                                                          -league.goals_scored))
    #table headers with padding
    print("\n\x1B[4m" + ("{:<2} {:<25} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4}".format
                       ('', 'Team', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts')) + "\x1B[0m")
    team_rank = 0
    for listPosition, listDict in enumerate(sorted_list):
        team_rank += 1
        print("{:<2} {:<25} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4}".format
              (team_rank,
               sorted_list[listPosition].team,
               sorted_list[listPosition].wins,
               sorted_list[listPosition].draws,
               sorted_list[listPosition].losses,
               sorted_list[listPosition].goals_scored,
               sorted_list[listPosition].goals_conceded,
               sorted_list[listPosition].goal_difference,
               sorted_list[listPosition].points))


def league_simulator(object_list):
    """
    This function simulates match scores by using random to determine if the match has been won, lost or drawn.
    Each team plays each other team twice. e.g. 20 teams in a league, each team plays 38 matches.
    The class: League is then updated with the results.
    ...
    :param object_list: list of objects
    :type object_list: list
    """
    #each team play each other team twice - ((number of teams * 2) - 2)
    number_of_matches = ((len(object_list) * 2) - 2)
    #iterate through each team
    for currentTeam in object_list:
        set_wins = 0
        set_draws = 0
        set_losses = 0
        set_gf = 0
        set_ga = 0
        #generate random goals scored and goals conceded
        for match in range(number_of_matches):
            goals_scored = random.randint(0, 5)
            goals_conceded = random.randint(0, 5)
            set_gf += goals_scored
            set_ga += goals_conceded
            currentTeam.goals_conceded = goals_conceded
            #if statements to check whether the team has won, lost or drawn a match
            if goals_scored > goals_conceded:
                set_wins += 1
            elif goals_scored == goals_conceded:
                set_draws += 1
            elif goals_scored < goals_conceded:
                set_losses += 1
        #update results to the league for team
        currentTeam.wins = set_wins
        currentTeam.draws = set_draws
        currentTeam.losses = set_losses
        currentTeam.goals_scored = set_gf
        currentTeam.goals_conceded = set_ga


def promote_team(object_list):
    """
    This function promotes the top team in the league (removes them from the League).
    The top team is the one with the most number of points, goal difference and then goals conceded
    ...
    :param object_list: list of objects
    :type object_list: list
    ...
    :return: returns the top team in the league with the most number of
             points, goal difference and then goals conceded
    :rtype: str
    """
    current_team = ''
    current_team_position = 0
    team_points = 0
    team_gd = 0
    team_gf = 0
    # iterate through the list of teams
    for position, teamName in enumerate(object_list):
        #if the next team in the list has a greater number of points, they get updated as the (current_team)
        if object_list[position].points > team_points:
            current_team = object_list[position].team
            team_points = object_list[position].points
            team_gd = object_list[position].goal_difference
            team_gf = object_list[position].goals_scored
            current_team_position = position
        #if the team has the same number of points then check to see if the goal difference is greater,
        # if so then update them as the (current_team)
        elif object_list[position].points == team_points and object_list[position].goal_difference > team_gd:
            current_team = object_list[position].team
            team_points = object_list[position].points
            team_gd = object_list[position].goal_difference
            team_gf = object_list[position].goals_scored
            current_team_position = position
        #if the team has the same number of points and goal difference then check to see if
        # the goals scored are greater, if so then update them as the (current_team)
        elif object_list[position].points == team_points and object_list[position].goal_difference == team_gd \
                and object_list[position].goals_scored > team_gf:
            current_team = object_list[position].team
            team_points = object_list[position].points
            team_gd = object_list[position].goal_difference
            team_gf = object_list[position].goals_scored
            current_team_position = position
    #remove the team from the list of objects
    del object_list[current_team_position]
    return current_team


def relegate_team(object_list):
    """
    This function relegates the bottom team in the league (removes them from the League)
    The bottom team is the one with the least number of points, goal difference and then goals conceded
    ...
    :param object_list: list of objects
    :type object_list: list
    ...
    :return: returns the bottom team in the league with the least number of
             points, goal difference and then goals conceded
    :rtype: str
    """
    #set the first team in the list as the starting point
    current_team = object_list[0].team
    current_team_position = 0
    team_points = object_list[0].points
    team_gd = object_list[0].goal_difference
    team_gf = object_list[0].goals_scored
    # iterate through the list of teams
    for position, teamName in enumerate(object_list):
        #if the next team in the list has lesser number of points, they get updated as the (current_team)
        if object_list[position].points < team_points:
            current_team = object_list[position].team
            team_points = object_list[position].points
            team_gd = object_list[position].goal_difference
            team_gf = object_list[position].goals_scored
            current_team_position = position
        #if the team has the same number of points then check to see if the goal difference is smaller,
        # if so then update them as the (current_team)
        elif object_list[position].points == team_points and object_list[position].goal_difference < team_gd:
            current_team = object_list[position].team
            team_points = object_list[position].points
            team_gd = object_list[position].goal_difference
            team_gf = object_list[position].goals_scored
            current_team_position = position
        #if the team has the same number of points and goal difference then check to see if
        # the goals scored are smaller, if so then update them as the (current_team)
        elif object_list[position].points == team_points and object_list[position].goal_difference == team_gd \
                and object_list[position].goals_scored < team_gf:
            current_team = object_list[position].team
            team_points = object_list[position].points
            team_gd = object_list[position].goal_difference
            team_gf = object_list[position].goals_scored
            current_team_position = position
    #remove the team from the list of objects
    del object_list[current_team_position]
    return current_team


def option_in_dict(option, dictionary: dict):
    """
    This function cross-checks if the input option is a key in the dictionary
    ...
    :param option: input to check against dictionary
    :type option: [str, int, float]
    :param dictionary: the dictionary to cross-check with the input
    :type dictionary: dict
    ...
    :return: returns true if the input option is a key in the dictionary otherwise false
    :rtype: bool
    """
    if option in dictionary.keys():
        return True
    else:
        return False


def find_team_from_object_list(team_name: str, object_list):
    """
    This function cross-checks if the input team name is in a list of objects
    ...
    :param team_name: team name to check
    :type team_name: str
    :param object_list: a list of objects from the class:League
    :type object_list: list
    ...
    :return: returns the teams info if they exist in the list otherwise prints team is not in the league
    :rtype: print
    """
    for position, teamList in enumerate(object_list):
        if str(object_list[position].team).upper() == str(team_name).upper():
            return print(teamList)
    else:
        return print(f'\n{team_name} is not in the league')


def team_object_position(team_name: str, object_list: list):
    """
    This function returns which index the specified team in located in a list
    ...
    :param team_name: team name to check
    :type team_name: str
    :param object_list: a list of objects from the class:League
    :type object_list: list
    ...
    :raises ValueError: team is not in the league
    ...
    :return: returns the teams index position in the list if they exist otherwise raises a exception
    :rtype: int
    """
    for position, teamList in enumerate(object_list):
        if str(object_list[position].team).upper() == str(team_name).upper():
            return position
    else:
        raise ValueError(f'{team_name} is not in the league')


def print_menu_options(menu_option: dict):
    """
    This function prints a dictionary
    ...
    :param menu_option: dictionary
    :type menu_option: dict
    ...
    :return: prints the dictionary
    :rtype: print
    """
    for option in menu_option.keys():
        print(menu_option[option])


def return_back(menu_name: str):
    """
    This function is used to prompt the user to return back
    ...
    :param menu_name: name of the menu which is being returned to
    :type menu_name: str
    ...
    :return: prompts the user to return back to a menu
    :rtype: any
    """
    input('\n'f'to return to the {menu_name} menu press the enter key')


def input_not_empty(question):
    """
    This function keeps prompting for a valid input to the question (the input is not blank/empty)
    ...
    :param question: the question which will be asked
    :type question: str
    ...
    :return: input answer
    :rtype: any
    """
    while True:
        question_answer = input(question)
        if question_answer.strip():
            return question_answer.strip()
        else:
            print("\ninvalid! the input is empty")

