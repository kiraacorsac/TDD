from SecuritySystemStrategies.security_system_strategy import SecuritySystemStrategy
import random

class RandomStrategy(SecuritySystemStrategy):
    def alert_dispatch(self, alert, handlers):
      random_int = random.randint(0, len(handlers)-1)
      handlers[random_int].handle_alert(alert)

