import logging
from collections import Counter

from ..space import Space
from ..room import Room

log = logging.getLogger()


class FloorPlan(Space):
    def __init__(self, rooms=None, **kwargs):
        # Only allow Room objects as rooms
        if rooms:
            room_class_types = [type(room) for room in rooms]

            for room_class_type in room_class_types:
                if room_class_type != Room:
                    raise Exception
            # TODO Can all() or any() be used here?
            # if any(room_class_types) != Room:
            #     raise Exception

        super().__init__(contents=rooms, **kwargs)

        # self.rooms = self.contents

    def __str__(self):
        return f'FloorPlan: {self.name}, Rooms: {self.rooms}'

    def __repr__(self):
        return self.__str__()

    @property
    def rooms(self):
        return self.contents

    def add_room(self, room, x_offset=0, y_offset=0):
        """

        return False if room can not be located at coordinates
        """
        self.place_content_at(room, x_offset, y_offset)

    def room_count(self):
        room_list = [r.room_type for r in self.plan.values()]
        return Counter(room_list)

    def plan_summary(self):
        summary = {}

        for r in self.plan.values():
            if r.room_type in summary:
                summary[r.room_type] += r.area
            else:
                summary[r.room_type] = r.area

        return summary