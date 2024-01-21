from random import uniform


class Sensor:
    OFFSET = 16

    def pop_next_pressure_psi_value(self):
        pressure_telemetry_value = self.sample_pressure()
        return self.OFFSET + pressure_telemetry_value

    @staticmethod
    def sample_pressure():
        # The reading of the pressure value from the sensor is simulated
        pressure_telemetry_value = uniform(0, 6)
        return pressure_telemetry_value
