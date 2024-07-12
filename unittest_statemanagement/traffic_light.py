# traffic_light.py

class TrafficLight:
    def __init__(self):
        self.state = 'red'

    def change_to_green(self):
        if self.state == 'red':
            self.state = 'green'

    def change_to_yellow(self):
        if self.state == 'green':
            self.state = 'yellow'

    def change_to_red(self):
        if self.state == 'yellow':
            self.state = 'red'

    def get_current_state(self):
        return self.state
