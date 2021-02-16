import unittest
from AlertHandlers.doggo import Doggo
from alert import Alert
from unittest.mock import patch

class DoggoTest(unittest.TestCase):

  def setUp(self):
    self.simple_doggo = Doggo("Jake")
    

  def test_doggoName_nameSet_returnsName(self):
    self.assertEqual(self.simple_doggo.name, "Jake")

  def test_doggoName_complexNameSet_returnsName(self):
    doggo = Doggo("Mr. Puppet")
    self.assertEqual(doggo.name, "Mr. Puppet")

  def test_doggoName_nameSetEmptyString_raisesError(self):
    with self.assertRaises(ValueError):
      doggo = Doggo("")

  def test_doggoName_nameSetNotAlphabetic_raisesError(self):
    with self.assertRaises(ValueError):
      doggo = Doggo("!!!")

  def test_doggoName_nameChanged_raisesError(self):
    doggo = Doggo("Something in line")
    with self.assertRaises(Exception):
      doggo.name = "Something new"

  def test_sound_soundSet_returnSound(self):
    self.simple_doggo.sound = "bark"
    self.assertEqual(self.simple_doggo.sound, "bark")

  def test_sound_default_exist(self):
    self.assertEqual(self.simple_doggo.sound, "Bark!")

  def test_sound_empty_raisesError(self):
    with self.assertRaises(ValueError):
      self.simple_doggo.sound = ""

  def test_doggoNumLegs_default_greaterThanOrEqual0(self):
    self.assertGreaterEqual(self.simple_doggo.num_legs, 0)

  def test_doggoNumLegs_setLessThan0_raisesError(self):
    with self.assertRaises(ValueError):
      self.simple_doggo.num_legs = -1
      
  @patch('builtins.print')
  def test_bark_default_prints(self, print_mock):
    self.simple_doggo.bark()
    print_mock.assert_called_once_with("Jake barks: Bark!")

  @patch('builtins.print')
  def test_growl_default_prints(self, print_mock):
    self.simple_doggo.growl()
    print_mock.assert_called_once_with("Jake: growl!")

  @patch.object(Doggo, 'bark')
  def test_handleAlert_insideCat1_bark10times(self, bark_mock):
    alert = Alert("inside", "cat", 1)
    self.simple_doggo.handle_alert(alert)
    self.assertEqual(bark_mock.call_count, 10)

  @patch.object(Doggo, 'bark')
  def test_handleAlert_outsideCat1_bark10times(self, bark_mock):
    alert = Alert("outside", "cat", 1)
    self.simple_doggo.handle_alert(alert)
    self.assertEqual(bark_mock.call_count, 10)

  @patch.object(Doggo, 'growl')
  def test_handleAlert_outsideHuman1_growl(self, growl_mock):
    alert = Alert("outside", "human", 1)
    self.simple_doggo.handle_alert(alert)
    growl_mock.assert_called_once()

  @patch.object(Doggo, "bark")
  def test_handleAlert_insideHuman1_bark(self, bark_mock):
    alert = Alert("inside", "human", 1)
    self.simple_doggo.handle_alert(alert)
    bark_mock.assert_called_once()


  def test_getSpeed_threeLegs_15(self):
    self.simple_doggo.num_legs = 3
    self.assertEqual(self.simple_doggo.get_speed(), 15)

  @patch('builtins.print')
  @patch.object(Doggo, "get_speed")
  def test_getSpeed_threeLegs_15_alternative(self, print_mock, getSpeed_mock):
    getSpeed_mock.return_value = 10
    self.simple_doggo.run()
    print_mock.assert_called_once()



  
  # @patch.object(Doggo, 'growl')
  # @unittest.skip("broken")
  # def test_playingAround_handleAlert_outsideCat1_bark10times(self, growl_mock):
  #   alert = Alert("outside", "cat", 1)
  #   self.simple_doggo.handle_alert(alert)
  #   self.assertEqual(growl_mock.call_count, 10)

if __name__ == "__main__":
  unittest.main()