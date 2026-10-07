import unittest
import os
import csv

class HorseRaces:
    def __init__(self, filename):
        self.race_dict = self.load_results(self.process_csv(filename))

    def process_csv(self, f):
        '''
        Parameters: 
            f, name or path or CSV file: string

        Returns:
            list of lists
        '''
        table = []

        # Do not modify this code
        # This opens the CSV and saves it as a list of lists
        base_path = os.path.abspath(os.path.dirname(__file__))
        full_path = os.path.join(base_path, f)
        # Open the file to be read by Python
        with open(full_path) as file:
            # Get each of the rows in this file
            rows = file.readlines()
            for row in rows:
                # Because this is a CSV, we SPLIT the row by commas
                # We go through each line and build a list of cells
                table_row = []
                for cell in row.strip().split(','):
                    table_row.append(cell)
                # Append the list of cells to the table
                table.append(table_row)
        # print(table)
        return table

###############################################################################
##### TASK 1
###############################################################################
    def load_results(self, table):
        '''
        Given the processed CSV (as a list of lists), populate a nested dictionary with the horse information.

        NOTE: You will need to use float() to convert the race time from str to float.

        Parameters: 
            table, a list of lists
                inner lists are individual rows in the CSV
                inner elements are the cells of each row
                EXAMPLE: [["Horse", "Tenno Sho Fall", "Tenno Sho Spring", "Teio Sho"],
                          ["Special Week", "16.5", "16.3", "17.0"]]

        Returns:
            nested dict structure from csv
            outer keys are (str) horses, outer values are dicts
            inner keys are (str) races, inner values are (int) race times
            EXAMPLE: {'Special Week': {'Tenno Sho Fall': 16.5, 'Tenno Sho Spring': 16.3, 'Teio Sho': 17.0}}
        '''
        #first row 
        header = table[0]

        race_dict = {}
        for row in table[1:]:
            horse_name = row[0]
            race_dict[horse_name] = {}
            for i in range(1, len(row)):
                race_name = header[i]
                race_time = float(row[i])
                race_dict[horse_name][race_name] = race_time
        return race_dict

###############################################################################
##### TASK 2
###############################################################################

    def horse_fastest_race(self, horse):
        '''
        Given the name of a horse, return its fastest race and time.
        If the horse does not exist, return (None, 999.9)

        Parameters:
            horse, name of a race: str

        Returns:
            tuple of fastest race name and the time
            EXAMPLE: ('Teio Sho', 14.8)
        '''

        fastest_race = None
        fastest_time = 999.9

        if horse in self.race_dict:
            return fastest_race, fastest_time

        horse_races = self.race_dict[horse]
        for race, time in horse_races.items():
            if time < fastest_time:
                fastest_time = time
                fastest_race = race
        return fastest_race, fastest_time

###############################################################################
##### TASK 3
###############################################################################
        
    def horse_personal_best(self):
        '''
        Calculate the fastest race and time for each horse.

        Returns:
            A dictionary of tuples of each horse, with their fastest race and time.
            EXAMPLE: {"Oguri Cap": ("Tenno Sho Fall", 16.6), "Mejiro McQueen": ("Tenno Sho Fall", 16.1)}
        '''
        horses_fastest = {}

        for horse_name in self.race_dict.keys():
            horses_fastest[horse_name] = self.horse_fastest_race(horse_name)
        return horses_fastest

###############################################################################
##### TASK 4
###############################################################################

    def get_average_time(self):
        '''
        Calculate the average race time for each horse.

        Returns:
            A dictionary with each horse and their average time.
            EXAMPLE: {'Gold Ship': 16.5, 'Daiwa Scarlet': 17.2}
        '''
        horses_average = {}

        for horse_name, races in self.race_dict.items():
            sum = 0.0
            for race_name, race_time in races.items():
                sum += race_time
            average_time = sum / len(races)
            horses_average[horse_name] = average_time

###############################################################################
##### DO NOT MODIFY THE UNIT TESTS BELOW!
###############################################################################
class dis7_test(unittest.TestCase):
    '''
    Unit tests to check that our functions were implemented correctly.
    '''
    def setUp(self):
        self.horse_races = HorseRaces('race_results.csv')

    def test_load_results(self):
        # Check that outer values are dictionaries
        self.assertIsInstance(self.horse_races.race_dict['Special Week'], dict)
        # Check one horse's time
        self.assertAlmostEqual(self.horse_races.race_dict['Special Week']['Tenno Sho Spring'], 16.3)

    def test_horse_fastest_race(self):
        nonexistent_horse = self.horse_races.horse_fastest_race('Bob')
        self.assertEqual(nonexistent_horse[0], None)
        fastest_horse = self.horse_races.horse_fastest_race('Symboli Rudolf')
        self.assertEqual(fastest_horse[0], 'Teio Sho')
        self.assertAlmostEqual(fastest_horse[1], 14.8)

    def test_horse_personal_best(self):
        self.assertEqual(self.horse_races.horse_personal_best()['Oguri Cap'][0], 'Tenno Sho Fall')
        self.assertAlmostEqual(self.horse_races.horse_personal_best()['Oguri Cap'][1], 16.6)

    def test_get_average_time(self):
        self.assertAlmostEqual(self.horse_races.get_average_time()['Gold Ship'], 16.5)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
