import unittest
from unittest.mock import patch, Mock
from AlertHandlers.doggo import Doggo
from AlertHandlers.sound_alarm import SoundAlarm
from alert import Alert
import random
from SecuritySystemStrategies.random_strategy import RandomStrategy

class RandomStrategyTest(unittest.TestCase):
  
  def test_alertDispatch_random(self):
        random.seed(0)
        strategy = RandomStrategy()
        handlers = [
          Mock(name="Doggo"),
          Mock(name="SoundAlarm")
        ]

        alert_mock = Mock(name="alert")
        alert_mock.where = "outside"
        alert_mock.what = "human"
        alert_mock.level = 2

        strategy.alert_dispatch(alert_mock, handlers)

        handlers[0].handle_alert.assert_not_called()
        handlers[1].handle_alert.assert_called_once_with(alert_mock)

