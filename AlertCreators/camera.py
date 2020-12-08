from AlertCreators.alert_creator import AlertCreator

class Camera(AlertCreator):
    '''
    name: String
    security_system: SecuritySystem
      - securtiy system where the camera is registered 

    where: [String]
      - specifies where the camera could be pointnig

    night_mode: Bool
      - camera is able to create alerts during night but not during the day

    detect_movement(what, where): void
      - call create_alert(), with what, where, level 2
      - if where is not in self.where (camera is pointing in unknown location), raise Exception
      - if camera is in nightmode, and datetime hour is between 6-22 (day), do nothing
      - if camera is in nightmode, and datetime hour is between 22-6 (night), do create alert, level 3
      - if camera is NOT in nightmode, just create the alert as usual



    (recording)
    '''

    def __init__(self, name, where):
        super().__init__(name)
        self.where = where
        self.night_mode = False


    def detect_movement(self, what, where, datetime):
        self.create_alert(where, what, 2)
