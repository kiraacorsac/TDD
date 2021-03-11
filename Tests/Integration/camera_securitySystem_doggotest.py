import unittest
from datetime import datetime
from unittest.mock import patch
from AlertCreators.camera import Camera
from AlertHandlers.doggo import Doggo
from security_system import SecuritySystem

class Camera_SecuritySystem_DoggoTest(unittest.TestCase):
  
  @patch('builtins.print')
  def test_cameraAlertCreated_doggoAlertHandled(self, print_mock):
    # setup

    camera = Camera("Camera1", ["outside", "garage"])
    doggo = Doggo("Jake")
    system = SecuritySystem()

    system.registerCreator(camera)
    system.registerHandler(doggo)


    # act
    camera.detect_movement("human", "outside", datetime(2020, 11, 26, 13, 20))


    # assert
    print_mock.assert_called_once_with("Jake: growl!")


  @patch('builtins.print')
  def test_cameraAlertCreated_doggoAlert_not_activated(self, print_mock):
    # setup

    camera = Camera("Camera1", ["outside", "garage"])
    doggo = Doggo("Jake")
    system = SecuritySystem()

    system.registerCreator(camera)
    system.registerHandler(doggo)

    #act
    camera.detect_movement("eagle", "outside", datetime(2020, 11, 26, 13, 20))
    
    # assert   
    print_mock.assert_not_called()
