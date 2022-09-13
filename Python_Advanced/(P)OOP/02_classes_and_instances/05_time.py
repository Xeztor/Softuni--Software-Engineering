class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def get_time(self):
        h = self.format_unit(self.hours)
        m = self.format_unit(self.minutes)
        s = self.format_unit(self.seconds)

        return f"{h}:{m}:{s}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1

        if self.minutes > Time.max_minutes:
            self.minutes = 0
            self.hours += 1
        if self.hours > Time.max_hours:
            self.hours = 0

        return self.get_time()

    @staticmethod
    def format_unit(unit):
        if unit < 10:
            return f"0{unit}"

        return f"{unit}"


# time = Time(9, 30, 59)
# print(time.next_second())
#
# time1 = Time(10, 59, 59)
# print(time1.next_second())
#
# time2 = Time(23, 59, 59)
# print(time2.next_second())
