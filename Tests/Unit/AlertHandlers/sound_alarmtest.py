import unittest
import winsound
from alert import Alert
from AlertHandlers.doggo import Doggo
from AlertHandlers.sound_alarm import SoundAlarm
from unittest.mock import patch


class SoundAlarmTest(unittest.TestCase):
    def setUp(self):
        self.doggo = Doggo("Jake")
        self.alert3 = Alert("outside", "human", 3)
        self.alert2 = Alert("outside", "human", 2)
        self.alert1 = Alert("outside", "human", 1)

    @patch.object(winsound, "Beep")
    def test_handleAlert_level3_bipsOnce(self, bip_mock):
        bippin = SoundAlarm()
        bippin.handle_alert(self.alert3)
        bip_mock.assert_called()

    @patch.object(winsound, "Beep")
    def test_handleAlert_level2_noBips(self, bip_mock):
        bippin = SoundAlarm()
        bippin.handle_alert(self.alert2)
        bip_mock.assert_not_called()


if __name__ == "__main__":
    unittest.main()