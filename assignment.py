class Match:
    def init(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing 
        class FlightTable:
            
            def init(self):
                self.matches = []

            def add_match(self, match):
                self.matches.append(match)

            def list_matches_by_team(self, team_name):
                matches = []
                for match in self.matches:
                    if team_name in [match.team1, match.team2]:
                        matches.append(match)
                return matches
            def list_matches_by_location(self, location):
                matches = []
                for match in self.matches:
                    if match.location == location:
                        matches.append(match)
                return matches

            def list_matches_by_timing(self, timing):
                matches = []
                for match in self.matches:
                    if match.timing == timing:
                        matches.append(match)
                return matches
def main():
    flight_table = FlightTable()

    flight_table.add_match(Match("Mumbai", "India", "Sri Lanka", "DAY"))
    flight_table.add_match(Match("Delhi", "England", "Australia", "DAY-NIGHT"))
    flight_table.add_match(Match("Chennai", "India", "South Africa", "DAY"))
    flight_table.add_match(Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    flight_table.add_match(Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    flight_table.add_match(Match("Delhi", "India", "Australia", "DAY"))

    while True:
        print("\nSearch Options:")
        print("1. List of all matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = input("Enter your choice: ")