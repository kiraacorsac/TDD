import unittest
from unittest.mock import patch, Mock
from AlertHandlers.doggo import Doggo
from AlertHandlers.sound_alarm import SoundAlarm
from alert import Alert


class EverybodyStrategyTest(unittest.TestCase):
  def test_alertDispatch_2handlers_handleAlertCalled2Times(self):
    # set up
    strategy = EverybodyStrategy()
    handlers = [Doggo("Jake"), SoundAlarm()]
    alert = Alert("outside","human", 2)

    # act
    strategy.alert_dispatch(alert, handlers)

    # assert
    