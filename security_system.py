from alert import Alert
from AlertHandlers.alert_handler import AlertHandler
from AlertCreators.alert_creator import AlertCreator


class SecuritySystem:
    def __init__(self):
        self.handlers = []
        self.creators = []
        self.strategy = None
        # raise Exception()

    def registerHandler(self, handler):
        if not isinstance(handler, AlertHandler):
            raise TypeError("Alert handler needs to derive from 'AlertHandler' class")

        self.handlers.append(handler)

    def createAlert(self, where, what, level):
        alert = Alert(where, what, level)
        self.strategy.alert_dispatch(alert, self.handlers)

        # strategy.alert_dispatch()

    def registerCreator(self, creator):
        if not isinstance(creator, AlertCreator):
            raise TypeError("Alert creator needs to derive from 'AlertCreator' class")
        self.creators.append(creator)
        creator.security_system = self
