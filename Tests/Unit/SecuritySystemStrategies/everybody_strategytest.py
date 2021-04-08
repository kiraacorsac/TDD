import unittest
from unittest.mock import patch, Mock
# from AlertHandlers.doggo import Doggo
# from AlertHandlers.sound_alarm import SoundAlarm
from alert import Alert
from SecuritySystemStrategies.everybody_strategy import EverybodyStrategy
# from SecuritySystemStrategies.random_strategy import RandomStrategy


class EverybodyStrategyTest(unittest.TestCase):
    def test_alertDispatch_2handlers_handleAlertCalled2Times(self):
        # set up
        strategy = EverybodyStrategy()
        handlers = [Mock(name="handler1"), Mock(name="handler2")]
        alert_mock = Mock(name="alert")
        alert_mock.where = "outside"
        alert_mock.what = "human"
        alert_mock.level = 2 
        
        # act
        strategy.alert_dispatch(alert_mock, handlers)

        # assert

        handlers[0].handle_alert.assert_called_once_with(alert_mock)
        handlers[1].handle_alert.assert_called_once_with(alert_mock)
