
class Vehicle:
    def __init__(self, speed, weight):
        self.speed = speed
        self.weight = weight


    def check_speed_limit_obec(self, speed):
        if speed > 50:
            return "Dostanes pokutu"
        else:
            return "Jedes v limitu"

    def check_speed_limit_dalnice(self, speed):
        if speed > 130:
            return "Dostanes pokutu"
        else:
            return "Jedes v limitu"


class Kamion(Vehicle):
    def __init__(self, speed, weight, load):
        super().__init__(speed, weight)
        self.load = load

    def check_speed_limit_dalnice(self):
        if self.speed > 80:
            return "Dostanes pokutu"
        else:
            return "Jedes v limitu"


kamion1 = Kamion(55, 1500, 18000)

print(kamion1.check_speed_limit_dalnice())
