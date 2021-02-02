from AlertCreators.alert_creator import AlertCreator
import datetime

class NosyNeighbor(AlertCreator):

    def __init__(self, name, bed_time, wake_up_time):
        super().__init__(name)
        self.bed_time = bed_time
        self.wake_up_time = wake_up_time

    def check_suspicious_activity(self, where, what, datetime):
        currentHour = (datetime.hour)
        if self.bed_time <= currentHour <= self.wake_up_time:
            print("Neighbor asleep")
        else:
            self.create_alert(where, what, 3)
        