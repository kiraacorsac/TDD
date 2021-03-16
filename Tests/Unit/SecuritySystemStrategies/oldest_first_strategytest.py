import unittest
from unittest.mock import patch, Mock
from AlertHandlers.doggo import Doggo
from AlertHandlers.sound_alarm import SoundAlarm
from alert import Alert
from SecuritySystemStrategies.oldest_first_strategy import OldestFirstStrategy


class OldestFirstStrategyTest(unittest.TestCase):
    @patch.object(Doggo, "handle_alert")
    # @patch.object(SoundAlarm, "handle_alert")
    def test_alertDispatch_2handlers_firstHandlerCalledOnly(
        self, handle_alert_Doggo_mock
    ):
        # set up
        strategy = OldestFirstStrategy()
        handlers = [Doggo("Jake"), SoundAlarm()]
        alert = Alert("outside", "human", 2)

        # act
        strategy.alert_dispatch(alert, handlers)

        # assert

        handle_alert_Doggo_mock.assert_called()
        # handle_alert_SoundAlarm_mock.assert_not_called()
