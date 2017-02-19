import location

class Data:
    """Class responsible for prepare data to use"""

    def __init__(self, malopolska_csv):
        self.malopolska_table = self.import_csv(malopolska_csv)
        self.malopolska_list = []
        self.initialize_objects()

    def import_csv(self, file_name):
        """
        Imports data from csv and  writes it to a list.
        Args: file_name: name of file
        Returns: table(list)
        """
        with open(file_name, "r") as file:
            lines = file.readlines()
        table = [element.replace("\n", "").split("\t") for element in lines]
        return table

    def write_csv(self, file_name, table):
        """
        Writes data from table to file.
        Args: file_name: name of file
              table: list with data
        Returns: None
        """
        with open(file_name, "w") as file:
            for record in table:
                row = ';'.join(record)
                file.write(row + "\n")

    def initialize_objects(self):
        """
        Initializes objects for classes.
        Returns: None
        """
        for row in self.malopolska_table:
            voivodeship = row[0]  # województwo
            county = row[1]  # powiat
            community = row[2]  # gmina
            rgmina = row[3]
            name = row[4]
            type = row[5]
            new_place = location.Location(voivodeship, county, community, rgmina, name, type)
            self.malopolska_list.append(new_place)