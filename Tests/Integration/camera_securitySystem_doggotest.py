import unittest
from datetime import datetime
from unittest.mock import patch
from AlertHandlers.sound_alarm import SoundAlarm
from AlertCreators.camera import Camera
from AlertHandlers.doggo import Doggo
from security_system import SecuritySystem
from SecuritySystemStrategies.everybody_strategy import EverybodyStrategy
from SecuritySystemStrategies.oldest_first_strategy import OldestFirstStrategy
import winsound

class Camera_SecuritySystem_DoggoTest(unittest.TestCase):
  
  @patch('builtins.print')
  def test_cameraAlertCreated_doggoAlertHandled(self, print_mock):
    # setup

    camera = Camera("Camera1", ["outside", "garage"])
    doggo = Doggo("Jake")
    system = SecuritySystem()
    system.strategy = EverybodyStrategy()

    system.registerCreator(camera)
    system.registerHandler(doggo)


    # act
    camera.detect_movement("human", "outside", datetime(2020, 11, 26, 13, 20))


    # assert
    print_mock.assert_called_once_with("Jake: growl!")

  
  @patch('builtins.print')
  def test_cameraAlertCreated_doggoAlertIgnored(self, print_mock):
    # setup

    camera = Camera("Camera1", ["outside", "garage"])
    doggo = Doggo("Jake")
    system = SecuritySystem()
    system.strategy = EverybodyStrategy()


    system.registerCreator(camera)
    system.registerHandler(doggo)

    camera.detect_movement("lizzard", "outside", datetime(2020, 11, 26, 13, 20))

    print_mock.assert_not_called()

  @patch('builtins.print')
  def test_cameraAlertCreated_doggoAsFirstHandlerAlertHandled(self, print_mock):
    # setup

    camera = Camera("Camera1", ["outside", "garage"])
    doggo = Doggo("Jake")
    soundalarm = SoundAlarm()
    system = SecuritySystem()
    system.strategy = OldestFirstStrategy()

    system.registerCreator(camera)
    system.registerHandler(doggo)
    system.registerHandler(soundalarm)
    


    # act
    camera.detect_movement("human", "outside", datetime(2020, 11, 26, 23, 20))


    # assert
    print_mock.assert_called_once_with("Jake: growl!")

  @patch('builtins.print')
  def test_cameraAlertCreated_doggoAsSecondHandlerAlertIgnored(self, print_mock):
    # setup

    camera = Camera("Camera1", ["outside", "garage"])
    doggo = Doggo("Jake")
    soundalarm = SoundAlarm()
    system = SecuritySystem()
    system.strategy = OldestFirstStrategy()

    system.registerCreator(camera)
    system.registerHandler(soundalarm)
    system.registerHandler(doggo)


    # act
    camera.detect_movement("human", "outside", datetime(2020, 11, 26, 23, 20))


    # assert
    print_mock.assert_not_called()

  @patch.object(winsound, "Beep")
  def test_cameraAlertCreated_soundAsFirstHandlerAlertHandled(self, bip_mock):
    # setup

    camera = Camera("Camera1", ["outside", "garage"])
    camera.night_mode = True
    doggo = Doggo("Jake")
    soundalarm = SoundAlarm()
    system = SecuritySystem()
    system.strategy = OldestFirstStrategy()

    system.registerCreator(camera)
    system.registerHandler(soundalarm)
    system.registerHandler(doggo)
    


    # act
    camera.detect_movement("human", "outside", datetime(2020, 11, 26, 23, 20))


    # assert
    bip_mock.assert_called()