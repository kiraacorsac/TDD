import unittest
from datetime import datetime
from unittest.mock import patch
from AlertCreators.camera import Camera
from AlertHandlers.emailer import Emailer
from security_system import SecuritySystem
from unittest.mock import patch
from SecuritySystemStrategies.everybody_strategy import EverybodyStrategy

class Camera_EmailerTest(unittest.TestCase):
  
  @patch.object(Emailer, "_send_message")
  def test_cameraEmailer(self, sendMessage_mock):
    # setup

    camera = Camera("Camera1", ["outside", "garage"])
    emailer = Emailer("filip@example.com")
    emailer.alert_recipient = "quentin@example.com"
    system = SecuritySystem()
    system.strategy = EverybodyStrategy()


    system.registerCreator(camera)
    system.registerHandler(emailer)

    # act
    camera.detect_movement("human", "outside", datetime(2020, 11, 26, 13, 20))


    # assert
    sendMessage_mock.assert_called_once_with(
            "quentin@example.com",
            "Alert",
            '''You've got an Alert!
What: human; Where: outside; Level: 2''')

if __name__ == "__main__":
    unittest.main()