from class_League import League
from league_functions import *
import sys


#location of default epl league teams txt file
default_path_file = 'epl.txt'

#location of save file for list of objects
save_location = 'objList.pkl'

#try to load the save .pkl file and initialise it through the class: League
#if the file is not found then return an empty list
try:
    load_objects(save_location)
except FileNotFoundError:
    list_of_objects = []
else:
    list_of_objects = load_objects(save_location)
    League.initiated = True


def main_menu():
    """
    This serves as the main menu, it performs the following tasks
    1. Setup a league
    2. Manage existing league
    """
    main_menu_options = {'1': '1. Setup a league',
                         '2': '2. Manage existing league',
                         '0': '0. End program'}
    while True:
        print('\n''Main menu: ')
        print_menu_options(main_menu_options)
        option_select = input('\n''Choose a option: ')
        if option_in_dict(option_select, main_menu_options) is True:
            if option_select == '1':
                menu_setup_league()
            if option_select == '2':
                manage_league()
            if option_select == '0':
                sys.exit()
        elif option_in_dict(option_select, main_menu_options) is False:
            print('\n''Invalid option try again')


def menu_setup_league():
    """
    This is the setup league menu, it performs the following tasks
    firs it asks which league rules you want to set up e.g. EPL rules
    available league rules
    1. EPL

    Then you can select one of the options below.
    1. Use the default directory and file name - to setup the league
    2. Use custom directory and file name - to setup the league
    """
    # name of child (league) class.
    # Use the key as the name e.g. class EPL becomes key 'EPL' and value '1. EPL'
    child_league_class = {'EPL': '1. EPL',
                          '0': '0. Back to main menu'}

    setup_league_options = {'1': '1. Use the default directory and file name',
                            '2': '2. Use custom directory and file name',
                            '0': '0. Back to previous menu'}

    global list_of_objects
    while True:
        #prompt user to select a league scoring system (one of the child league classes)
        print('\n''Which league system do you want to use: ')
        print_menu_options(child_league_class)
        option_rule_select = input('\n''please type one of the options in the list or 0 to return back: ')
        #change to uppercase to allow for lowercase input
        option_rule_select = option_rule_select.upper()
        if option_in_dict(option_rule_select.upper(), child_league_class) is True:

            #prompt user to select default path or set a custom one
            while True:
                print('\n''Setup league menu: ')
                print_menu_options(setup_league_options)
                option_select = input('\n''Choose an option: ')
                if option_in_dict(option_select, setup_league_options) is True:

                    #use default path
                    if option_select == '1':
                        print('\n'f'Place your file into the python project directory '
                              f'with the file name: {default_path_file}')
                        input('\n''press the enter key once ready to load')
                        menu_setup_league_path(option_rule_select, default_path_file)

                    #use custom path
                    if option_select == '2':
                        custom_path = input_not_empty('\n''Enter the full path of the directory and file: ')
                        if os.path.exists(custom_path):
                            menu_setup_league_path(option_rule_select, custom_path)
                        else:
                            print('\n''File does not exist!')

                    if option_select == '0':
                        menu_setup_league()

                elif option_in_dict(option_select, setup_league_options) is False:
                    print('\n''Invalid option try again')

        elif option_in_dict(option_rule_select.upper(), child_league_class) is False:
            print('\n''Invalid option try again')

def menu_setup_league_path(child_class_league, path_file: str):
    """
    This function provides a user-friendly menu to setup the football league along
    with the benefit of error handling.
    ...
    :param child_class_league: name of the child league class e.g. EPL
    :type child_class_league: str
    :param path_file: path to the directory/file which contains the text file of teams
    :type path_file: str
    """
    global list_of_objects
    while True:
        #check if the file exists
        if os.path.exists(path_file):
            print('\n''file exists!')

            #check the file format
            try:
                check_file_format(path_file)
                print('correct file format!')
            #if file format issue - raise error and return to setup league menu
            except ValueError as format_issue:
                print(format_issue)
                print('Please check if the line stated is in the following format '
                      '"team: stadium - location"')
                menu_setup_league()

            #check if the class module exists
            try:
                str_to_class(child_class_league)
                print('module exists!')
            #if class module not found then raise error and return to the setup menu
            except ModuleNotFoundError as MNF:
                print(MNF)
                print('Please check if the class module exists')
                menu_setup_league()

            #if no error found then proceed to initialise objects into class
            else:
                league_name = input_not_empty('\n''What is the name of the league: ')
                list_of_objects.clear()
                list_of_objects = initialise_child_league(league_name, path_file, child_class_league)
                print('\n'f'Congratulations, the league {league_name} has now been created!')
                save_objects(list_of_objects, save_location)
                return_back('main')
                main_menu()
        #if the file does not exist then return to the setup league menu
        else:
            print('\n''File does not exist!')
            menu_setup_league()

def manage_league():
    """
    This is the manage league menu, it allows you to perform the following tasks
    1. View League info - takes you to the view league info menu
    2. Update league - takes you to the update league menu
    3. Simulate League - simulates the league scores
    """
    manage_league_options = {'1': '1. View League info',
                             '2': '2. Update league',
                             '3': '3. Simulate League',
                             '0': '0. Back to main menu'}
    #check if any object exist in the class League
    if League.initiated is True:
        while True:
            print('\n''Manage league menu: ')
            print_menu_options(manage_league_options)
            option_select = input('\n''Choose a option: ')
            if option_in_dict(option_select, manage_league_options) is True:

                if option_select == '1':
                    view_league()

                if option_select == '2':
                    update_league()

                #simulate league
                if option_select == '3':
                    selection = input('Are you sure want to start simulation, this will overwrite the existing scores'
                                      '\nEnter ''yes'' to continue: ')
                    if selection.upper() == 'YES':
                        league_simulator(list_of_objects)
                        save_objects(list_of_objects, save_location)
                        print('\n''The league has now been simulated!')
                        league_score_board(list_of_objects)
                        return_back('manage league')
                        manage_league()
                    else:
                        print('\n''league simulation has been cancelled!')
                        manage_league()

                if option_select == '0':
                    main_menu()

            elif option_in_dict(option_select, manage_league_options) is False:
                print('\n''Invalid option try again')

    #if no objects have been initialised in the class League
    else:
        print('There is no league to manage')
        return_back('main')
        main_menu()


def view_league():
    """
    This is the view league info menu, it allows you to perform the following tasks
    1. View score board - view the leagues score board with all teams and stats
    2. View team info - view a teams information
    """
    view_league_options = {'1': '1. View score board',
                           '2': '2. View team info',
                           '0': '0. Back to manage league menu'}
    while True:
        print('\n''View league menu: ')
        print_menu_options(view_league_options)
        option_select = input('\n''Choose a option: ')
        if option_in_dict(option_select, view_league_options) is True:

            if option_select == '1':
                league_score_board(list_of_objects)
                return_back('view league info')
                view_league()

            if option_select == '2':
                team_name = input('\n''Which team would you like to view: ')
                find_team_from_object_list(team_name, list_of_objects)
                return_back('view league info')
                view_league()

            if option_select == '0':
                manage_league()

        elif option_in_dict(option_select, view_league_options) is False:
            print('\n''Invalid option try again')


def update_league():
    """
    This is the update league menu, it allows you to perform the following tasks
    1. Update team score - takes you to the update team score menu
    2. Update manager - allows you to update a teams manager
    3. Update top goal scorer - allows you to update a teams top goal scorer
    4. Promote teams from league - promotes the top 3 teams from the league
    5. Relegate teams from league - relegates the bottom 3 teams from the league
    """
    update_league_options = {'1': '1. Update team score',
                             '2': '2. Update manager',
                             '3': '3. Update top goal scorer',
                             '4': '4. Promote teams from league',
                             '5': '5. Relegate teams from league',
                             '0': '0. Back to manage league menu'}
    while True:
        print('\n''Update league menu: ')
        print_menu_options(update_league_options)
        option_select = input('\n''Choose a option: ')
        if option_in_dict(option_select, update_league_options) is True:

            if option_select == '1':
                update_score()

            #update manager
            if option_select == '2':
                team = input('Which team would you like to update: ')
                try:
                    team_position = team_object_position(team, list_of_objects)
                except ValueError:
                    print(f'{team} does not exist in the league')
                else:
                    set_manager = input_not_empty('What is the name of the manager: ')
                    list_of_objects[team_position].manager = set_manager
                    print(f'the manger for {team} has now been updated')
                    save_objects(list_of_objects, save_location)
                    print(list_of_objects[team_position])
                    return_back('update league')
                    update_league()

            #update top goal scorer
            if option_select == '3':
                team = input('Which team would you like to update: ')
                try:
                    team_position = team_object_position(team, list_of_objects)
                except ValueError:
                    print(f'{team} does not exist in the league')
                else:
                    set_TGS = input_not_empty('What is the name of the top goal scorer: ')
                    list_of_objects[team_position].top_goal_scorer = set_TGS
                    print(f'the top goal scorer for {team} has now been updated')
                    save_objects(list_of_objects, save_location)
                    print(list_of_objects[team_position])
                    return_back('update league')
                    update_league()

            #promote teams from the league
            if option_select == '4':
                selection = input('Are you sure want to promote teams from the league, '
                                  'this will remove the top 3 teams'
                                  '\nenter ''yes'' to continue: ')
                if selection.upper() == 'YES':
                    team1 = promote_team(list_of_objects)
                    team2 = promote_team(list_of_objects)
                    team3 = promote_team(list_of_objects)
                    save_objects(list_of_objects, save_location)
                    print(f'\n{team1}, {team2} and {team3} have now been promoted from the league')
                    league_score_board(list_of_objects)
                    return_back('update league')
                    update_league()
                else:
                    print('promote league has been cancelled')
                    update_league()

            #relegate teams from the league
            if option_select == '5':
                selection = input('Are you sure want to relegate teams from the league, '
                                  'this will remove the bottom 3 teams'
                                  '\nenter ''yes'' to continue: ')
                if selection.upper() == 'YES':
                    team1 = relegate_team(list_of_objects)
                    team2 = relegate_team(list_of_objects)
                    team3 = relegate_team(list_of_objects)
                    save_objects(list_of_objects, save_location)
                    print(f'\n{team1}, {team2} and {team3} have now been relegated from the league')
                    league_score_board(list_of_objects)
                    return_back('update league')
                    update_league()
                else:
                    print('relegate league has been cancelled')
                    update_league()

            if option_select == '0':
                manage_league()

        elif option_in_dict(option_select, update_league_options) is False:
            print('\n''Invalid option try again')


def update_score():
    """
    This is the update score menu, it allows you to perform the following tasks
    1. Update wins
    2. Update losses
    3. Update draws
    4. Update goals scored
    5. Update goals conceded
    """
    update_score_options = {'1': '1. Update wins',
                            '2': '2. Update losses',
                            '3': '3. Update draws',
                            '4': '4. Update goals scored',
                            '5': '5. Update goals conceded',
                            '0': '0. Back to update league menu'}
    global team_position

    #establish the team to be updated
    team = ''
    if not team:
        set_team = input('\n''Which team would you like to update: ')
        try:
            team_position = team_object_position(set_team, list_of_objects)
            team = set_team
        except ValueError:
            print('\n'f'{set_team} does not exist in the league')
            update_league()

    while True:
        print('\n''Update score menu: ')
        print_menu_options(update_score_options)
        option_select = input('\n''Choose a option: ')
        if option_in_dict(option_select, update_score_options) is True:

            #update wins
            if option_select == '1':
                print(f'Current wins for {team}: {list_of_objects[team_position].wins}')
                set_win = input('Number of wins to set: ')
                try:
                    set_win = int(set_win)
                    list_of_objects[team_position].wins = set_win
                except ValueError:
                    if isinstance(set_win, int) and set_win < 0:
                        print('\n'f'invalid!! The input ({set_win}) is a negative number')
                    else:
                        print('\n'f'invalid!! The input ({set_win}) is not a integer')
                else:
                    print('\n'f'{set_win} wins have now been set for {team}')
                    save_objects(list_of_objects, save_location)
                    return_back('update team score')

            #update losses
            if option_select == '2':
                print(f'Current losses for {team}: {list_of_objects[team_position].losses}')
                set_losses = input('Number of losses to set: ')
                try:
                    set_losses = int(set_losses)
                    list_of_objects[team_position].losses = set_losses
                except ValueError:
                    if isinstance(set_losses, int) and set_losses < 0:
                        print('\n'f'invalid!! The input ({set_losses}) is a negative number')
                    else:
                        print('\n'f'invalid!! The input ({set_losses}) is not a integer')
                else:
                    print('\n'f'{set_losses} losses have now been set for {team}')
                    save_objects(list_of_objects, save_location)
                    return_back('update team score')

            #update draws
            if option_select == '3':
                print(f'Current draws for {team}: {list_of_objects[team_position].draws}')
                set_draws = input('Number of draws to set: ')
                try:
                    set_draws = int(set_draws)
                    list_of_objects[team_position].draws = set_draws
                except ValueError:
                    if isinstance(set_draws, int) and set_draws < 0:
                        print('\n'f'invalid!! The input ({set_draws}) is a negative number')
                    else:
                        print('\n'f'invalid!! The input ({set_draws}) is not a integer')
                else:
                    print('\n'f'{set_draws} draws have now been set for {team}')
                    save_objects(list_of_objects, save_location)
                    return_back('update team score')

            #update goals scored
            if option_select == '4':
                print(f'Current goals scored for {team}: {list_of_objects[team_position].goals_scored}')
                set_gf = input('Number of goals scored to set: ')
                try:
                    set_gf = int(set_gf)
                    list_of_objects[team_position].goals_scored = set_gf
                except ValueError:
                    if isinstance(set_gf, int) and set_gf < 0:
                        print('\n'f'invalid!! The input ({set_gf}) is a negative number')
                    else:
                        print('\n'f'invalid!! The input ({set_gf}) is not a integer')
                else:
                    print('\n'f'{set_gf} goals scored have now been set for {team}')
                    save_objects(list_of_objects, save_location)
                    return_back('update team score')

            #update goals conceded
            if option_select == '5':
                print(f'Current goals conceded for {team}: {list_of_objects[team_position].goals_conceded}')
                set_ga = input('Number of goals conceded to set: ')
                try:
                    set_ga = int(set_ga)
                    list_of_objects[team_position].goals_conceded = set_ga
                except ValueError:
                    if isinstance(set_ga, int) and set_ga < 0:
                        print('\n'f'invalid!! The input ({set_ga}) is a negative number')
                    else:
                        print('\n'f'invalid!! The input ({set_ga}) is not a integer')
                else:
                    print('\n'f'{set_ga} goals conceded have now been set for {team}')
                    save_objects(list_of_objects, save_location)
                    return_back('update team score')

            if option_select == '0':
                update_league()

        elif option_in_dict(option_select, update_score_options) is False:
            print('\n''Invalid option try again')