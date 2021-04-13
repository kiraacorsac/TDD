import unittest
from unittest.mock import patch, Mock

from datetime import datetime
from AlertCreators.camera import Camera
from security_system import SecuritySystem


class CameraTest(unittest.TestCase):

    def setUp(self):
        self.camera = Camera("Camera1", ["backyard", "outside"])

        self.connectedCamera = Camera("Camera2", ["backyard", "outside"])
        self.system = Mock(name="SecuritySystem") 
        self.connectedCamera.security_system = self.system

        

    def test_isConnected_securitySystemNotNone_true(self):
        # setUp
        # set up everything you need to run the test

        self.camera.security_system = self.system

        self.assertTrue(self.camera.is_connected())

    # @patch.object(SecuritySystem, 'createAlert')
    def test_createAlert_humanOutside2_systemCreateAlert(self):
        #setup
        #act
        self.connectedCamera.create_alert("outside", "human", 2)
        #assert
        self.system.createAlert.assert_called_once()

    @patch.object(Camera, 'create_alert')
    def test_detectMovement_connected_createAlert(self, create_alert_mock):
        self.connectedCamera.detect_movement("human", "outside", datetime(2020, 11, 26, 13, 20))
        create_alert_mock.assert_called_once_with("outside", "human", 2)


    @patch.object(Camera, 'create_alert')
    def test_detectMovement_nightTimeNmodeon_createAlert(self, create_alert_mock):
        self.connectedCamera.night_mode = True
        self.connectedCamera.detect_movement("human", "outside", datetime(2020, 11, 26, 23, 20))
        create_alert_mock.assert_called_once_with("outside", "human", 3)

    #@patch.object(Camera, 'detect_movement')
    @patch('builtins.print')
    def test_detectMovement_dayTimeNmodeon_standby(self, print_mock):
        self.connectedCamera.night_mode = True
        self.connectedCamera.detect_movement("human", "outside", datetime(2020, 11, 26, 13, 20))
        print_mock.assert_called_once_with("standing by")

    def test_detectMovement_unknownLocation_raise(self):
        with self.assertRaises(Exception):
            self.connectedCamera.detect_movement("human", "inside",  datetime(2020, 11, 26, 13, 20))