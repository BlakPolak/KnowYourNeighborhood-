
class Ui:
    """This class create user interface"""

    @staticmethod
    def main_menu():
        """Method display main menu"""
        print("""
               Welcome
               What would you like to do:
               (1) List statistics
               (2) Display 3 cities with longest names
               (3) Display county's name with the largest number of communities
               (4) Display locations, that belong to more than one category
               (5) Advanced search
               (0) Exit CcMS
            """)
        option = input("Your choice: ")
        return option


    @staticmethod
    def get_inputs(list_labels, title):
        """Method ask user for input"""
        inputs = []
        print(title)
        for item in list_labels:
            user_input = input(item + ' ').strip()
            inputs.append(user_input)
        return inputs


    @staticmethod
    def print_table(table, title_list):
        """Display data in formatted table"""
        table.insert(0, title_list)
        for row_index, row in enumerate(table):
            for col_index, col in enumerate(row):
                if (type(col) == float) or (type(col) == int):
                    table[row_index][col_index] = str("{0:,.2f}".format(col))
        widths = [max(map(len, col)) for col in zip(*table)]
        sum_of_widths = sum(widths) + len(table[0]) * 3 - 1 # len(table[0]) - number of |
        for row in table:
            print("-" * sum_of_widths)
            print("|" + "  ".join((val.rjust(width) + "|" for val, width in zip(row, widths))))
        print("-" * sum_of_widths)
