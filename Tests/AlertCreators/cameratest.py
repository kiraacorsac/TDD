import unittest
from unittest.mock import patch

from datetime import datetime
from AlertCreators.camera import Camera
from security_system import SecuritySystem


class CameraTest(unittest.TestCase):

    def setUp(self):
        self.camera = Camera("Camera1", ["backyard", "outside"])

        self.connectedCamera = Camera("Camera2", ["backyard", "outside"])
        system = SecuritySystem()  
        self.connectedCamera.security_system = system

        

    def test_isConnected_securitySystemNotNone_true(self):
        # setUp
        # set up everything you need to run the test

        system = SecuritySystem()  
        self.camera.security_system = system

        self.assertTrue(self.camera.is_connected())

    @patch.object(SecuritySystem, 'createAlert')
    def test_createAlert_humanOutside2_systemCreateAlert(self, system_create_alert_mock):
        self.connectedCamera.create_alert("outside", "human", 2)
        system_create_alert_mock.assert_called_once()

    @patch.object(Camera, 'create_alert')
    def test_detectMovement_connected_createAlert(self, create_alert_mock):
        self.connectedCamera.detect_movement("human", "outside", datetime(2020, 11, 26, 13, 20))
        create_alert_mock.assert_called_once_with("outside", "human", 2)

    @patch.object(Camera, 'create_alert')
    def test_createAlert_nightmode_systemCreateAlert(self, create_alert_mock):
        self.connectedCamera.nightmode("outside", "human", 2)
        create_alert_mock.assert_called_once()

    @patch.object(Camera, 'create_alert')
    def test_createAlert_nightmodeIsTrue_create_alert(self, create_alert_mock):
        self.connectedCamera.detect_movement("outside", "human", "11:00 PM")
        create_alert_mock.assert_called_once()

    @patch.object(Camera, 'create_alert')
    def test_createAlert_nightmodeIsFalse_create_alertNotCalled(self, create_alert_mock):
        self.connectedCamera.detect_movement("outside", "human", "08:00 AM")
        create_alert_mock.assert_not_called()

    def test_detectMovement_nightTimeNightMode_createsAlert(self):
        pass