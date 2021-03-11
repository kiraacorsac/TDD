from abc import ABC, abstractmethod

class SecuritySystemStrategy(ABC):
  @abstractmethod
  def alert_dispatch(self, alert, handlers):
    pass
