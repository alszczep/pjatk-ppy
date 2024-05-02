class InvalidStateChangeError(Exception):
    # message = from_state
    def __init__(self, message: str, to_state: str):
        super().__init__("Invalid state change from " + message + " to " + to_state)
