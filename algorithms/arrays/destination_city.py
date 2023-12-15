class Solution:
    def destCity(self,paths):
        """
        :type paths: List[List[str]]
        :rtype : str
        """
        source_cities = set(city[0] for city in paths)
        for path in paths:
            destination_city = path[1]

            if destination_city not in source_cities:
                return destination_city
        return ""
