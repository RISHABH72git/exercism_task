class Clock:
    def __init__(self, hour, minute):
        self.total_minutes = (hour * 60 + minute) % (24 * 60)
        self.hour = self.total_minutes // 60
        self.minute = self.total_minutes % 60

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return (self.hour, self.minute) == (other.hour, other.minute)

    def __add__(self, minutes):
        self.total_minutes = self.total_minutes + minutes
        self.hour = (self.total_minutes // 60) % 24
        self.minute = self.total_minutes % 60
        return self

    def __sub__(self, minutes):
        self.total_minutes = self.total_minutes - minutes
        self.hour = (self.total_minutes // 60) % 24
        self.minute = self.total_minutes % 60
        return self