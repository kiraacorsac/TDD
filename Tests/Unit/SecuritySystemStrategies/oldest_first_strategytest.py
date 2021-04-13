import unittest
from unittest.mock import patch, Mock
from AlertHandlers.doggo import Doggo
from AlertHandlers.sound_alarm import SoundAlarm
from alert import Alert
from SecuritySystemStrategies.oldest_first_strategy import OldestFirstStrategy


class OldestFirstStrategyTest(unittest.TestCase):

    def test_alertDispatch_oldestFirst(self):
        # set up
        strategy = OldestFirstStrategy()


        handlers = [
            Mock(name="Doggo"),
            Mock(name="SoundAlarm"),
        ]

        alert_mock = Mock(name="alert")
        alert_mock.where = "outside"
        alert_mock.what = "human"
        alert_mock.level = 2

        # act
        strategy.alert_dispatch(alert_mock, handlers)

        # assert

        handlers[0].handle_alert.assert_called_once_with(alert_mock)
