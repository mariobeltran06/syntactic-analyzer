class ErrorManager:
    def __init__(self):
        self.errors = []

    def add(self, msg):
        self.errors.append(msg)

    def has_errors(self):
        return len(self.errors) > 0

    def save_to_file(self, filename='errors.err'):
        with open(filename, 'w') as f:
            for err in self.errors:
                f.write(err + '\n')