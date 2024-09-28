class MyCalendarTwo:

    def __init__(self):
        self.nonoverlap = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:

        for s, e in self.overlap:
            if end > s and e > start:
                return False

        for s, e in self.nonoverlap:
            if end > s and e > start:
                self.overlap.append((max(start, s), min(end, e)))

        self.nonoverlap.append((start, end))
        return True
