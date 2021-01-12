class AlertCreator:
    '''
    name: String
    security_system: SecuritySystem

    is_connected(): Bool
      - retrurns true if security_system is not none
    
    create_alert(): void
      - pass alert to security system, if connected
      - raise Exception, if not connected
    '''

    def __init__(self, name):
        self.name = name
        self.security_system = None

    def is_connected(self):
        if self.security_system is not None:
            return True
        else:
            return False

    def create_alert(self, where, what, level):
        self.security_system.createAlert(where, what, level)
