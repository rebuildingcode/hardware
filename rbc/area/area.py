class Area():
    def __init__(self, nodes):
        """Four nodes required to create an Area

        Args:
            nodes (Iterable of Nodes)
        """
        self.nodes = self.validate(nodes)

    def area(self):
        """Calculate and return the area"""
        len_x = self.nodes['2'].x - self.nodes['1'].x
        len_y = self.nodes['1'].y - self.nodes['4'].y
        return len_x * len_y

    def validate(self, nodes):
        """Validate that set of nodes represents a rectangular area

        Args:
            nodes (Iterable of Nodes)
        Returns: dict of nodes
        """
        assert len(nodes) == 4
        x_set = set([node.x for node in nodes])
        y_set = set([node.y for node in nodes])
        z_set = set([node.z for node in nodes])

        assert len(x_set) == len(y_set) == 2
        assert len(z_set) == 1  # only support areas in one z-plane

        top_left = [node for node in nodes 
                    if node.x == min(x_set) and node.y == max(y_set)][0]
        top_right = [node for node in nodes 
                     if node.x == max(x_set) and node.y == max(y_set)][0]
        bottom_right = [node for node in nodes 
                        if node.x == max(x_set) and node.y == min(y_set)][0]
        bottom_left = [node for node in nodes 
                        if node.x == min(x_set) and node.y == min(y_set)][0]

        return {
            '1': top_left,
            '2': top_right,
            '3': bottom_right,
            '4': bottom_left,
        }