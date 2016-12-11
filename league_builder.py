import csv
import random

# read and copy details of players from the supplied CSV file
def load_players(filename, all_players):
    with open(filename, 'r') as csvfile:
        players = csv.DictReader(csvfile, delimiter=',')
        for player in players:
            # put each player's details in a dictionary
            player_details = {'Name': player['Name'],
               'Height (inches)': player['Height (inches)'],
               'Soccer Experience': player['Soccer Experience'],
               'Guardian Name(s)': player['Guardian Name(s)']}
            # append each player's details the players list
            all_players.append(player_details)

# group players in two - experienced = yes and experienced = no
def group_by_experience(players):
    experienced_players_yes = []
    experienced_players_no = []
    for player in players:
      if player['Soccer Experience'] == 'YES':
          experienced_players_yes.append(player)
      if player['Soccer Experience'] == 'NO':
          experienced_players_no.append(player)

    return experienced_players_yes, experienced_players_no


# select players to respective teams
def players_to_teams(players):

    experienced, not_experienced = group_by_experience(players)

    # selection of experienced players
    while True:
        pick = random.choice(experienced)
        if pick not in Dragons:
            Dragons.append(pick)
            if len(Dragons) == 3:
                break

    while True:
        pick = random.choice(experienced)
        if (pick not in Dragons) and (pick not in Sharks):
            Sharks.append(pick)
            if len(Sharks) == 3:
                break

    while True:
        pick = random.choice(experienced)
        if (pick not in Dragons) and (pick not in Sharks) and (pick not in Raptors):
            Raptors.append(pick)
            if len(Raptors) == 3:
                break


    # select non experienced players for the Dragons
    while True:
        # select player randomly
        pick = random.choice(not_experienced)
        if pick not in Dragons:
            Dragons.append(pick)
            if len(Dragons) == 6:
                break


    # select non experienced players for the Sharks
    while True:
        pick = random.choice(not_experienced)
        # check to see if the selected player isn't neither Dragons
        # also check if the selected player isn't already in Sharks
        if (pick not in Dragons) and (pick not in Sharks):
            Sharks.append(pick)
            if len(Sharks) == 6:
                break


    # select non experienced players for the Raptors
    while True:
        # select player randomly
        pick = random.choice(not_experienced)
        # check to see if the selected player isn't neither Dragons nor Sharks
        # also check if the selected player isn't already in Raptors
        if (pick not in Dragons) and (pick not in Sharks) and (pick not in Raptors):
            Raptors.append(pick)
            if len(Raptors) == 6:
                break


# function that produces the league roster
# listing the team name, and each player on the team
# including the player's information

def make_roster():
    filename = 'teams.txt'
    with open(filename, 'a') as file:
        file.write("Raptors\n")
        for player in Raptors:
            name = player['Name']
            experience = player['Soccer Experience']
            guardian = player['Guardian Name(s)']
            detials = ('{}, {}, {}\n').format(name, experience, guardian)
            file.write(detials)

        file.write("Sharks\n")
        for player in Sharks:
            name = player['Name']
            experience = player['Soccer Experience']
            guardian = player['Guardian Name(s)']
            detials = ('{}, {}, {}\n').format(name, experience, guardian)
            file.write(detials)

        file.write("Dragons\n")
        for player in Dragons:
            name = player['Name']
            experience = player['Soccer Experience']
            guardian = player['Guardian Name(s)']
            detials = ('{}, {}, {}\n').format(name, experience, guardian)
            file.write(detials)


# function that creates file name from a given name string
def make_filename(player_name):
    # fetch player name for filename
    file_holder = player_name
    # make name all lower case,
    # replace the space between the name with an underscore
    # then append the result string with file format .txt
    prepared_name = file_holder.lower().replace (" ", "_") + '.txt'
    return prepared_name

# letters to players' guardians
def generate_letters():
    message_structure = ("Dear {}, I'm pleased to inform you that {} is " +
          "now a player of the Raptors soccer team.\nThe first practice " +
          "towards the upcoming soccer league will be on 7th Jan, 2017. " +
          "\nThank you.\nEnock,\nCoordinator, Soccer League\n")

    # letters for those in team Raptors
    for player in Raptors:
        message = message_structure.format(player['Guardian Name(s)'], player['Name'])

        # call the function that makes the filename for each message
        filename = make_filename(player['Name'])

        # filename is a returned string from the function make_filename
        with open(filename, 'a') as file:
            file.write(message)

    # letters for those in team Sharks
    for player in Sharks:
        message = message_structure.format(player['Guardian Name(s)'], player['Name'])

        # call the function that makes the filename for each message
        filename = make_filename(player['Name'])

        # filename is a returned string from the function make_filename
        with open(filename, 'a') as file:
            file.write(message)

    # letters for those in team Dragons
    for player in Dragons:
        message = message_structure.format(player['Guardian Name(s)'], player['Name'])

        # call the function that makes the filename for each message
        filename = make_filename(player['Name'])

        # filename is a returned string from the function make_filename
        with open(filename, 'a') as file:
            file.write(message)




if __name__ == "__main__":

    # list of all provided players
    soccer_players = []

    # list of players by teams
    Raptors = []
    Sharks = []
    Dragons = []

    load_players('soccer_players.csv', soccer_players)
    group_by_experience(soccer_players)
    players_to_teams(soccer_players)
    make_roster()
    generate_letters()
