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

    def where_pointed(self, where):
      if self.where != where:
        self.create_alert()
      else:
        raise Exception("Camera pointed to unknown place")

  def nightmode(self):
    timeStart = "10:00 PM"
    timeEnd = "06:00 AM"
    now = datetime.now() 
    timeEnd = datetime.strptime(timeEnd, "%I:%M%p")
    timeStart = datetime.strptime(timeStart, "%I:%M%p")
    now = datetime.strptime(now, "%I:%M%p")

    if self.timeStart >= self.now <= self.timeEnd: 
      return True
    else:
      return False


  def detect_movement(self, where, what, level):
    if self.is_connected and self.nightmode() == True and self.timeStart <= self.now >= self.timeEnd:
      self.create_alert(where, what, 3)
    elif self.is_connected and self.nightmode() == False and self.timeStart >= self.now <= self.timeEnd: 
      self.create_alert()
