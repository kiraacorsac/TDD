import unittest
from unittest.mock import patch, Mock
from AlertHandlers.doggo import Doggo
from AlertHandlers.alert_handler import AlertHandler
from AlertCreators.camera import Camera
from security_system import SecuritySystem


class SecuritySystemTest(unittest.TestCase):
  def setUp(self):
    self.security = SecuritySystem()

  def test_registerHandler_handler_isInHandlers(self):
    handler_mock = Mock(name="handler", spec=AlertHandler)
    self.security.registerHandler(handler_mock)
    self.assertIn(handler_mock, self.security.handlers)
  
  def test_registerHandler_integer_raisesTypeError(self):
    with self.assertRaises(TypeError):
      self.security.registerHandler(5)



  # @patch.object(Doggo, "handle_alert")
  # def test_alertCreated_doggoRegistred_doggoHandleAlert(self, handle_alert_mock):
  #   doggo = Doggo("Jake")
  #   self.security.registerHandler(doggo)
  #   self.security.createAlert("outside", "human", 3)
  #   handle_alert_mock.assert_called_once()

  # TODO test wheter security system calls strategy using manually made mocks


  def test_registerCreator_camera_isInCreator(self):
    #setup
    camera_mock = Camera("Testcamera", ["outside"])
    
    #act
    self.security.registerCreator(camera_mock)

    #assert
    self.assertIn(camera_mock, self.security.creators)
    self.assertEqual(camera_mock.security_system, self.security)

  def test_registerCreator_integer_raisesTypeError(self):
    with self.assertRaises(TypeError):
      self.security.registerCreator(5)