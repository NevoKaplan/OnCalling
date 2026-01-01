class NoAvailablePersonOnDate(Exception):

    def __init__(self, message: str, *, date=None):
        super().__init__(message)
        self.date = date