from ...opening import Opening

# NOTE: Factory design pattern?


class Door(Opening):
    """Abstract class for doors"""
    def __init__(self, width=32, height=80, thickness=1.375, jamb_width=4.5625,
                 unit_price=0):

        self.thickness = thickness
        self.jamb_width = jamb_width
        self.unit_price = unit_price

        super().__init__(width, height)

    def plot(self):
        """
        - [ ] Plot plan view
        - [ ] Plot elevation view
        """
        pass  # pragma: no cover



