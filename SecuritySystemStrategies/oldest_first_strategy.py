# Implement
# - unit test
# - integration test (you can put it in camera_securitySystem_doggotest)
# - this class
# Strategy that always picks the first handler in the list when alert_dispatched is called

from SecuritySystemStrategies.security_system_strategy import SecuritySystemStrategy


class OldestFirstStrategy(SecuritySystemStrategy):
    def alert_dispatch(self, alert, handlers):
        print(handlers[0], handlers[1])
        handlers[0].handle_alert(alert)
