import unittest
from unittest.mock import patch, Mock
from AlertHandlers.doggo import Doggo
from AlertHandlers.sound_alarm import SoundAlarm
from alert import Alert


class EverybodyStrategyTest(unittest.TestCase):
    @patch.object(Doggo, "handle_alert")
    @patch.object(SoundAlarm, "handle_alert")
    def test_alertDispatch_2handlers_handleAlertCalled2Times(
        self, handle_alert_Doggo_mock, handle_alert_SoundAlarm_mock
    ):
        # set up
        self.strategy = EverybodyStrategy()
        self.handlers = [Doggo("Jake"), SoundAlarm()]
        self.alert = Alert("outside", "human", 2)

        # act
        self.strategy.alert_dispatch(self.alert, self.handlers)

        # assert

        handle_alert_Doggo_mock.assert_called_once()
        handle_alert_SoundAlarm_mock.assert_called_once()
