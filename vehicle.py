# vehicle.py

class Vehicle:
    def __init__(self, vid):
        self.id = str(vid)

    def __repr__(self):
        return f"Vehicle({self.id})"
