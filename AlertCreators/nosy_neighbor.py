from AlertCreators.alert_creator import AlertCreator
from datetime import datetime, time
import re


class NosyNeighbor(AlertCreator):

    """
    It's an AlertCreator
    It has a constructor __init__(name, bed_time, wake_up_time) . I believe the name  is self-explenatory, and the rest of the properties are explained later.
    It has a method check_suspicious_activity(where, what, time) that takes the parameters where , what, time. Once again, similar to detect_movement, this is an 'endpoint' for our simulation, so the where  and what  are just strings we are going to be passing manually, nothing more.
    It has two properties bed_time and wake_up_time. Both of these properties are of type datetime.
    Calling check_suspicious_activity  with time  set to something wake_up_time  and bed_time results in creating level 3 alert, with the specified where  and what . Take a look in the camera implementation for inspiration.
    Calling check_suspicious_activity  with time  set to something  bed_time and wake_up_time  throws an exception saying 'Neighbor asleep'.
    datetime and datetime diffrence to be implemented for more robust feature"""

    def __init__(self, name, bed_time, wake_up_time):
        if name == "":
            raise ValueError("Should not be empty")
        if re.search("[^A-Za-z. ]", name):
            raise ValueError("Should be alphabetic")

        self.__name = name

        self.bed_time = bed_time
        self.wake_up_time = wake_up_time

    @property
    def name(self):
        return self.__name

    def check_suspicious_activity(self, where, what, datetime):
        self.currentHour = datetime
        if self.bed_time <= self.currentHour <= self.wake_up_time:
            raise Exception("Wellknown neighbor is sleeping")
        else:
            self.create_alert(where, what, 3)
