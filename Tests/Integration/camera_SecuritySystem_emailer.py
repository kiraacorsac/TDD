import unittest
from datetime import datetime
from unittest.mock import patch
from AlertCreators.camera import Camera
from AlertHandlers.emailer import Emailer
from security_system import SecuritySystem

class Camera_SecuritySystem_EmailerTest(unittest.TestCase):

    @patch.object(Emailer, "_send_message")
    def test_cameraAlertCreated_emailerAlertHandled(self, sendMessage_mock):

    camera = Camera("Camera1", ["outside", "garage"])
    emailer = Emailer("anyone@example.com")
    system = SecuritySystem()

    system.registerCreator(camera)
    system.registerHandler(emailer)

    camera.detect_movement("human", "outside", datetime(2020, 11, 26, 13, 20))

    sendMessage_mock.assert_called_once()