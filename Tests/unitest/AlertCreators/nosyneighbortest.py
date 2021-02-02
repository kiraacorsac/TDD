import unittest
from unittest.mock import patch

from datetime import datetime
from AlertCreators.neighbor import Neighbor
from security_system import SecuritySystem


class NosyNeighborTest(unittest.TestCase):
    def setUp(self):
        self.neighbor = Neighbor(
            "Corine", datetime(2020, 11, 26, 23, 00), datetime(2020, 11, 26, 7, 00)
        )

        system = SecuritySystem()
        self.neighbor.security_system = system

    def test_isConnected_securitySystemNotNone_true(self):
        # setUp
        # set up everything you need to run the test

        system = SecuritySystem()
        self.neighbor.security_system = system

        self.assertTrue(self.neighbor.is_connected())

    @patch.object(SecuritySystem, "createAlert")
    def test_checkSuspiciousActivity_upTime_systemCreateAlert(
        self, system_create_alert_mock
    ):
        self.neighbor.checkSuspiciousActivity(
            "outside", "human", datetime(2020, 11, 26, 10, 20)
        )
        system_create_alert_mock.assert_called_once()

    # @patch("builtins.print")
    # def test_checkSuspiciousActivity_downTime_createNoAlert(self, print_mock):
    #     self.neighbor.checkSuspiciousActivity(
    #         "outside", "human", datetime(2020, 11, 26, 3, 20)
    #     )
    #     print_mock.assert_called_once_with("Neighbor asleep.")

    def test_checkSuspiciousActivity_downTime_raise(self):
        with self.assertRaises(Exception):
            self.neighbor.checkSuspiciousActivity(
                "outside", "human", datetime(2020, 11, 26, 3, 20)
            )
