import ui


class Location:
    def __init__(self, voivodeship, county, community, rgmina, name, type):
        self.voivodeship = voivodeship #wojewodztwo
        self.county = county #powiat
        self.community = community #gmina
        self.rgmina = rgmina #region gminy
        self.name = name
        self.type = type


    @staticmethod
    def statistics(malopolska_list):
        statistics = {}
        stats_list = []
        for item in malopolska_list[1:]:
            if item.type not in statistics:
                statistics[item.type] = 1
            else:
                statistics[item.type] += 1
            if item.type == "miasto na prawach powiatu":
                statistics["powiat"] += 1
        print (statistics)
        for key, value in statistics.items():
            stats_list.append([str(value), key])
        stats_list.sort()
        return stats_list

    @staticmethod
    def three_cities_with_longest_names(malopolska_list):
        longest = []
        for element in malopolska_list:
            if element.type == 'miasto':
                longest.append(element.name)
        longest.sort(key=len, reverse=True)
        longest_3 = longest[:3]
        longest_3.sort()
        list_to_print = []
        n = 1
        for city in longest_3:
            list_to_print.append([str(n) + ".", city])
            n += 1
        return list_to_print

    @staticmethod
    def county_with_largest_number_of_communities(malopolska_list):
        counties = {}
        for element in malopolska_list:
            if element.type == 'powiat':
                counties[element.name] = [element.county, 0]
        for key, values in counties.items():
            for element in malopolska_list:
                if element.county == values[0]:
                    counties[key][1] = element.community

        county = ['city', 0]
        for key, values in counties.items():
            if int(values[1]) > county[1]:
                county[0] = key
                county[1] = int(values[1])
        list_to_print = [[str(county[0])+' ---> it has '+str(county[1]) + ' communities']]
        list_to_print.sort()
        return list_to_print

    @staticmethod
    def locations_that_belong_to_more_than_one_category(malopolska_list):
        location = {}
        for element in malopolska_list:
            if element.community:
                location[element.name] = []
        for key, value in location.items():
            for element in malopolska_list:
                if key == element.name:
                    value.append(element.type)
        list_to_print = []
        for key, value in location.items():
            if len(value) > 1:
                list_to_print.append([str(key), ", ".join(str(x) for x in value)])
        list_to_print.sort()
        print (list_to_print)
        return list_to_print

    @staticmethod
    def advanced_search(malopolska_list):
        results = []
        search = ui.Ui.get_inputs([''], 'Type location:')
        search = search[0].lower()
        for item in malopolska_list:
            if search in item.name.lower():
                results.append([item.name, item.type])

        results = sorted(results)
        return results