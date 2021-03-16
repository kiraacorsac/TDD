from SecuritySystemStrategies.security_system_strategy import SecuritySystemStrategy

class EverybodyStrategy(SecuritySystemStrategy):
  def alert_dispatch(self, alert, handlers):
    for handler in handlers:
      handler.handle_alert(alert)