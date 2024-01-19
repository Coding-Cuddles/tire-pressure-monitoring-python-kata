from tire_pressure_monitoring import Alarm


class TestAlarm:

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        assert not alarm.is_alarm_on
