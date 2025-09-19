class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def calculate_year(self, days_in_year):
        minute = self.seconds/60
        hour = minute/60
        days = hour/24
        years = days/ days_in_year
        return round(years,2)

    def on_mercury(self):
        days = 365.256 * 0.24084
        return self.calculate_year(days)

    def on_venus(self):
        days = 365.256 * 0.61519726
        return self.calculate_year(days)
        
    def on_earth(self):
        days = 365.256 * 1.0
        return self.calculate_year(days)

    def on_mars(self):
        days = 365.256 * 1.8808158
        return self.calculate_year(days)

    def on_jupiter(self):
        days = 365.256 * 11.862615
        return self.calculate_year(days)

    def on_saturn(self):
        days = 365.256 * 29.447498
        return self.calculate_year(days)

    def on_uranus(self):
        days = 365.256 * 84.016846
        return self.calculate_year(days)

    def on_neptune(self):
        days = 365.256 * 164.79132
        return self.calculate_year(days)