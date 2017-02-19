import data
import location
import ui


def main():
    """Method starts program and allows user to choose an option"""
    malopolska = data.Data('malopolska.csv')
    list_from_malopolska = malopolska.malopolska_list
    choose = None
    while not choose:
        choose = ui.Ui.main_menu()
        if choose == "1":
            statistics = location.Location.statistics(list_from_malopolska)
            ui.Ui.print_table(statistics, ['Amount', 'Type'])
            choose = None
        if choose == "2":
            longest_name = location.Location.three_cities_with_longest_names(list_from_malopolska)
            ui.Ui.print_table(longest_name, ['Number', 'Name of city'])
            print ('zrobilem')
            choose = None
        if choose == "3":
            county = location.Location.county_with_largest_number_of_communities(list_from_malopolska)
            ui.Ui.print_table(county, ['County with the largest number of communities'])
            choose = None
        if choose == "4":
            locations = location.Location.locations_that_belong_to_more_than_one_category(list_from_malopolska)
            ui.Ui.print_table(locations, ['Name', 'Type'])
            choose = None
        if choose == "5":
            advanced_search_result = location.Location.advanced_search(list_from_malopolska)
            ui.Ui.print_table(advanced_search_result, ['Name', 'Type'])
            choose = None
        if choose == "0":
            print("Goodbye!")
            choose = True
if __name__ == "__main__":
    main()