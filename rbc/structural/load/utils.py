import logging

log = logging.getLogger(__name__)

def sum_loads(*loads):
    """

    Requirements
    ------------

    - all loads need to be the same type (PointLoad, UniformLoad, MomentLoad)
    - all loads need to be acting in the same direction (X, Y, Z)

    """
    log.info('Received loads: %s', loads)

    load_type = type(loads[0])
    direction = loads[0].direction
    unit = loads[0].force_unit

    for load in loads:
        if type(load) != load_type:
            raise Exception('Given loads must have the same type.')

        if load.direction != direction:
            raise Exception('Given loads must have the same direction.')

        if load.force_unit != unit:
            raise Exception('Given loads must have the same direction.')

    return sum([load.magnitude for load in loads]), unit
