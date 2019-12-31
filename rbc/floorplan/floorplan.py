import logging

from ..space import Space
from ..room import Room

log = logging.getLogger()


class FloorPlan(Space):
    def __init__(self, rooms=None, **kwargs):
        if rooms:
            room_class_types = [type(room) for room in rooms]
            log.info(f'room classes: {room_class_types}')
            # TODO Can all() or any() be used here?
            for room_class_type in room_class_types:
                if room_class_type != Room:
                    raise Exception
        super().__init__(contents=rooms, **kwargs)

        self.rooms = self.contents

    def __str__(self):
        return f'FloorPlan: {self.name}, Rooms: {self.rooms}'

    def __repr__(self):
        return self.__str__()