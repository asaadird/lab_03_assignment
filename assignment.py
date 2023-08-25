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
