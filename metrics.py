# metrics.py

class Metrics:
    def __init__(self):
        self.total = 0
        self.valid = 0
        self.invalid = 0
        self.failures = {}

    def record(self, success, reason=None):
        self.total += 1
        if success:
            self.valid += 1
        else:
            self.invalid += 1
            if reason:
                self.failures[reason] = self.failures.get(reason, 0) + 1

    def report(self):
        print("Total messages processed:", self.total)
        print("  Valid:  ", self.valid)
        print("  Invalid:", self.invalid)
        for reason, count in self.failures.items():
            print(f"    {reason} failures: {count}")
