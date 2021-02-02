import unittest
from unittest.mock import patch

from datetime import datetime
from AlertCreators.nosyneighbor import NosyNeighbor
from security_system import SecuritySystem

class nosyneighbortest(unittest.TestCase):

    def setUp(self):
        self.nosyneighbor = NosyNeighbor("Neighbor1", 1, 8)
        system = SecuritySystem()  
        self.nosyneighbor.security_system = system

    @patch.object(SecuritySystem, 'createAlert')
    def test_createAlert_humanOutside2_systemCreateAlert(self, system_create_alert_mock):
        self.nosyneighbor.create_alert("outside", "human", 3)
        system_create_alert_mock.assert_called_once()

    @patch.object(NosyNeighbor, 'create_alert')
    def test_checksuspiciousactivity_awake_createAlert(self, create_alert_mock):
        self.nosyneighbor.check_suspicious_activity("outside", "human", datetime(2020, 11, 26, 10, 20))
        create_alert_mock.assert_called_once_with("outside", "human", 3)

    @patch('builtins.print')
    def test_check_suspicious_activity_asleep_noaction(self, print_mock):
        self.nosyneighbor.check_suspicious_activity("outside", "human", datetime(2020, 11, 26, 2, 20))
        print_mock.assert_called_once_with("Neighbor asleep")

    