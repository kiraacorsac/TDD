import unittest
from AlertCreators.nosy_neighbor import NosyNeighbor
from alert import Alert
from unittest.mock import patch
from datetime import datetime, time
from security_system import SecuritySystem


class NosyNeighborTest(unittest.TestCase):
    def setUp(self):
        self.bedtime = "23:30"
        self.waketime = "05:30"
        self.wellknown_neighbor = NosyNeighbor("Felix", self.bedtime, self.waketime)

        system = SecuritySystem()
        self.wellknown_neighbor.security_system = system

    def test_isConnected_securitySystemNotNone_true(self):
        system = SecuritySystem()
        self.wellknown_neighbor.security_system = system
        self.assertTrue(self.wellknown_neighbor.is_connected())

    def test_neighbourName_nameSet_returnsName(self):
        self.assertEqual(self.wellknown_neighbor.name, "Felix")

    def test_neighbourName_complexNameSet_returnsName(self):
        wellknown_neighbor = NosyNeighbor("Mr. Grumble", self.bedtime, self.waketime)
        self.assertEqual(wellknown_neighbor.name, "Mr. Grumble")

    def test_neighborName_nameSetEmptyString_raisesError(self):
        with self.assertRaises(ValueError):
            wellknown_neighbor = NosyNeighbor("", self.bedtime, self.waketime)

    def test_neighborName_nameSetNotAlphabetic_raisesError(self):
        with self.assertRaises(ValueError):
            wellknown_neighbor = NosyNeighbor("@", self.bedtime, self.waketime)

    @patch.object(SecuritySystem, "createAlert")
    def test_createAlert_visitorInFrontOfTheDoor_systemCreateAlert(
        self, system_create_alert_mock
    ):
        self.wellknown_neighbor.create_alert(
            "infront of the door", "random visitors", 2
        )
        system_create_alert_mock.assert_called_once()

    @patch.object(NosyNeighbor, "create_alert")
    def test_checkSuspiciousActivity_WakeUpHour_createAlert(self, create_alert_mock):
        self.wellknown_neighbor.check_suspicious_activity(
            "infront of the door", "random visitors", datetime(2021, 1, 25, 13, 30, 10)
        )
        create_alert_mock.assert_called_once_with(
            "infront of the door", "random visitors", 3
        )

    def test_checkSuspiciousActivity_SleepHour_raiseException(self):
        with self.assertRaises(Exception):
            self.wellknown_neighbor.check_suspicious_activity(
                "infront of the door",
                "random visitors",
                datetime(2021, 1, 25, 2, 30, 20),
            )


if __name__ == "__main__":
    unittest.main()
