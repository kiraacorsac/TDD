import unittest
from AlertCreators.camera import Camera
from AlertHandlers.doggo import Doggo
from security_system import SecuritySystem


class Camera_SecuritySystem_DoggoTest(unittest.TestCase):
    def test_cameraAlertCreated_doggoAlertHandled(self):
        # setup

        camera = Camera("Camera2", ["outside", "garage"])
        doggo = Doggo("Tom")
        system = SecuritySystem()

        system.registerCreator(camera)
        system.registerHandler(doggo)

        # act

        # assert
