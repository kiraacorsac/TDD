import unittest
from unittest.mock import patch, Mock
from AlertHandlers.doggo import Doggo
from AlertHandlers.sound_alarm import SoundAlarm
from alert import Alert
import random
from SecuritySystemStrategies.random_strategy import RandomStrategy

class RandomStrategyTest(unittest.TestCase):
  
  @patch.object(Doggo, "handle_alert")
  @patch.object(SoundAlarm, "handle_alert")
  def test_alertDispatch_random(self, handle_alert_SoundAlarm_mock, handle_alert_Doggo_mock):
        random.seed(0)
        strategy = RandomStrategy()
        alert = Alert("outside", "human", 2)   
        handlers = [Doggo("Jake"), SoundAlarm()]

        strategy.alert_dispatch(alert, handlers)

        handle_alert_SoundAlarm_mock.assert_called_once()
        handle_alert_Doggo_mock.assert_not_called()
