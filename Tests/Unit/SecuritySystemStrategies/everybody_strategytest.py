import unittest
from unittest.mock import patch, Mock
# from AlertHandlers.doggo import Doggo
# from AlertHandlers.sound_alarm import SoundAlarm
from alert import Alert
from SecuritySystemStrategies.everybody_strategy import EverybodyStrategy
# from SecuritySystemStrategies.random_strategy import RandomStrategy


class EverybodyStrategyTest(unittest.TestCase):
    def test_alertDispatch_multipleHandlers_handleAlertCalledForEveryHandler(self):
        # set up
        strategy = EverybodyStrategy()
        handlers = [
            Mock(name="handler1"),
            Mock(name="handler2"),
            Mock(name="handler3"),
            Mock(name="handler4"),
            Mock(name="handler5"),
            Mock(name="handler6"),
        ]

        alert_mock = Mock(name="alert")
        alert_mock.where = "outside"
        alert_mock.what = "human"
        alert_mock.level = 2

        # act
        strategy.alert_dispatch(alert_mock, handlers)

        # assert
        for handler in handlers:
            handler.handle_alert.assert_called_once_with(alert_mock)
