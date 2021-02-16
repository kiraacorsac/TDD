from AlertCreators.alert_creator import AlertCreator
import datetime


class Neighbor(AlertCreator):
    def __init__(self, name, bed_time, wake_up_time):
        super().__init__(name)
        self.bed_time = bed_time.hour
        self.wake_up_time = wake_up_time.hour

    def checkSuspiciousActivity(self, where, what, time):
        currentHour = time.hour
        # print(self.wake_up_time)
        # print(self.bed_time)
        # print(currentHour)
        if self.bed_time >= currentHour >= self.wake_up_time:
            self.create_alert(where, what, 3)

        else:
            raise Exception("Neighbor asleep.")


# from datetimerange import DateTimeRange

# time_range = DateTimeRange("2015-03-22T10:00:00+0900", "2015-03-22T10:10:00+0900")
# print("2015-03-22T10:05:00+0900" in time_range)
# print("2015-03-22T10:15:00+0900" in time_range)

# time_range_smaller = DateTimeRange("2015-03-22T10:03:00+0900", "2015-03-22T10:07:00+0900")
# print(time_range_smaller in time_range)