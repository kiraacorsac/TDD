from AlertCreators.alert_creator import AlertCreator
import datetime


class Camera(AlertCreator):
    """
    name: String
    security_system: SecuritySystem
      - securtiy system where the camera is registered

    where: [String]
      - specifies where the camera could be pointnig

    night_mode: Bool
      - camera is able to create alerts during night but not during the day

    detect_movement(what, where): void
      - call create_alert(), with what, where, level 2
      - if where is not in self.possible_locations (camera is pointing in unknown location), raise Exception
      - if camera is in nightmode, and datetime hour is between 6-22 (day), do nothing
      - if camera is in nightmode, and datetime hour is between 22-6 (night), do create alert, level 3
      - if camera is NOT in nightmode, just create the alert as usual



    (recording)
    """

    def __init__(self, name, possible_locations):
        super().__init__(name)
        self.possible_locations = possible_locations
        self.night_mode = False

    # def detect_movement(self, what, where, datetime):
    #   currentHour = (datetime.hour)
    #   if 6 <= currentHour <= 22:
    #     self.create_alert(where, what, 2)
    #   else:
    #     self.night_mode = True
    #     self.create_alert(where, what, 3)

    def detect_movement(self, what, where, datetime):
        if where not in self.possible_locations:
            raise Exception("Camera location unknown.")

        currentHour = datetime.hour
        if self.night_mode is True:
            if 6 <= currentHour <= 22:
                print("standing by")
            else:
                self.create_alert(where, what, 3)
        else:
            self.create_alert(where, what, 2)
