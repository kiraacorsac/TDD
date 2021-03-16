import unittest
from unittest.mock import patch, Mock
from AlertHandlers.doggo import Doggo
from AlertHandlers.sound_alarm import SoundAlarm
from alert import Alert
from SecuritySystemStrategies.everybody_strategy import EverybodyStrategy


class EverybodyStrategyTest(unittest.TestCase):
    @patch.object(Doggo, "handle_alert")
    @patch.object(SoundAlarm, "handle_alert")
    def test_alertDispatch_2handlers_handleAlertCalled2Times(
        self, handle_alert_Doggo_mock, handle_alert_SoundAlarm_mock
    ):
        # set up
        strategy = EverybodyStrategy()
        handlers = [Doggo("Jake"), SoundAlarm()]
        alert = Alert("outside", "human", 2)

        # act
        strategy.alert_dispatch(alert, handlers)

        # assert

        handle_alert_Doggo_mock.assert_called_once()
        handle_alert_SoundAlarm_mock.assert_called_once()
