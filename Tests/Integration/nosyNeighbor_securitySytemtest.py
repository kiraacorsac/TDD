import unittest


class NosyNeighbor_SecuritySystem():

    def test_nosyNeighbor_randomStrategy_alertHanlded(self):
        #set-up
        bed_time = "23:30"
        wake_time = "05:30"
        neighbor = NosyNeighbor("Laco", bed_time, wake_time)
        doggo = Doggo("Jake")
        sound_alarm = SoundAlarm()

        system = SecuritySystem()
        system.strategy = RandomStrategy()

        system.registerCreator(neighbor)
        system.registerHandler(doggo)
        system.registerCreator(sound_alarm)


        #act
        neighbor.check_suspicious_activity(
            "infront of the door",
            "random visitors",
            datetime(2021, 1, 25, 2, 30, 20),
        )


