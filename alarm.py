from sensor import Sensor


class Alarm:
    LOW_PRESSURE_THRESHOLD = 17
    HIGH_PRESSURE_THRESHOLD = 21

    def __init__(self):
        self._sensor = Sensor()
        self._is_alarm_on = False

    def check(self):
        psi_pressure_value = self._sensor.pop_next_pressure_psi_value()

        if (psi_pressure_value < self.LOW_PRESSURE_THRESHOLD
                or psi_pressure_value > self.HIGH_PRESSURE_THRESHOLD):
            self._is_alarm_on = True

    @property
    def is_alarm_on(self):
        return self._is_alarm_on
