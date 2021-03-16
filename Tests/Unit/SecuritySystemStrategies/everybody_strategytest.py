import unittest
from unittest.mock import patch, Mock
from AlertHandlers.doggo import Doggo
from AlertHandlers.sound_alarm import SoundAlarm
from alert import Alert


class EverybodyStrategyTest(unittest.TestCase):
    def test_alertDispatch_2handlers_handleAlertCalled2Times(self):
        # set up
        self.strategy = EverybodyStrategy()
        self.handlers = [Doggo("Jake"), SoundAlarm()]
        self.alert = Alert("outside", "human", 2)

        # act
        self.strategy.alert_dispatch(self.alert, self.handlers)

        # assert

    @patch.object(EverybodyStrategy, "alert_dispatch")
    def test_strategy_alertDispatched(self, alert_disptach_mock):

        self.strategy.alert_dispatch(self.alert)
        alert_dispatch_mock.assert_called_once()
