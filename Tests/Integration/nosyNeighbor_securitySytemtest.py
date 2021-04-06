import unittest
from datetime import datetime
from unittest.mock import patch
from AlertHandlers.sound_alarm import SoundAlarm
from AlertCreators.nosy_neighbor import NosyNeighbor
from AlertHandlers.doggo import Doggo
from security_system import SecuritySystem
from SecuritySystemStrategies.random_strategy import RandomStrategy
import random
import winsound


class NosyNeighbor_SecuritySystem(unittest.TestCase):
    @patch("builtins.print")
    @patch.object(winsound, "Beep")
    def test_nosyNeighbor_randomStrategy_alertHandled(self, print_mock, bip_mock):
        # set-up
        random.seed(0)
        bed_time = "23:30"
        wake_time = "05:30"
        neighbor = NosyNeighbor("Laco", bed_time, wake_time)
        doggo = Doggo("Jake")
        soundalarm = SoundAlarm()

        system = SecuritySystem()
        system.strategy = RandomStrategy()

        system.registerCreator(neighbor)
        system.registerHandler(doggo)
        system.registerHandler(soundalarm)

        # act
        neighbor.check_suspicious_activity(
            "infront of the door",
            "random visitors",
            datetime(2021, 1, 25, 22, 30, 20),
        )

        # assert
        print_mock.assert_called()
        bip_mock.assert_not_called()
