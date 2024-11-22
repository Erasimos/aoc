class SimulationState:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SimulationState, cls).__new__(cls, *args, **kwargs)
            cls._instance.state = {}
        return cls._instance

    def __init__(self):
        if not hasattr(self, "state"):
            self.state = {}