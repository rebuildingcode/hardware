

def get_polygon_label(content):
    if hasattr(content, 'name'):
        # get label for polygon-type objects with name attribute
        label = content.name
    else:
        # otherwise default to using the area value as the label
        # this supports shapely's Polygon object
        label = f"AREA: {content.area}"

    return label