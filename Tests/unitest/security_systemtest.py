import unittest
from unittest.mock import patch, Mock
from AlertHandlers.doggo import Doggo
from AlertCreators.camera import Camera
from security_system import SecuritySystem


class SecuritySystemTest(unittest.TestCase):
    def setUp(self):
        self.security = SecuritySystem()

    def test_registerHandler_doggo_isInHandlers(self):
        doggo = Doggo("Jake")
        self.security.registerHandler(doggo)
        self.assertIn(doggo, self.security.handlers)

    def test_registerHandler_integer_raisesTypeError(self):
        with self.assertRaises(TypeError):
            self.security.registerHandler(5)

    @patch.object(Doggo, "handle_alert")
    def test_alertCreated_doggoRegistred_doggoHandleAlert(self, handle_alert_mock):
        doggo = Doggo("Jake")
        self.security.registerHandler(doggo)
        self.security.createAlert("outside", "human", 3)
        handle_alert_mock.assert_called_once()

    def test_registerCreator_camera_isInCreator(self):
        # setup
        camera_mock = Camera("Testcamera", ["outside"])

        # act
        self.security.registerCreator(camera_mock)

        # assert
        self.assertIn(camera_mock, self.security.creators)
        self.assertEqual(camera_mock.security_system, self.security)

    def test_registerCreator_integer_raisesTypeError(self):
        with self.assertRaises(TypeError):
            self.security.registerCreator(5)
