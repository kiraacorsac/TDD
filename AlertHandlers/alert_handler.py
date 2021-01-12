from abc import ABC, abstractmethod

class AlertHandler(ABC):
  
  @abstractmethod
  def handle_alert(self, alert):
    pass