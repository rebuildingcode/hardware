class UniformlyLoadedMixin:
    @property
    def max_moment(self):
        """Maximum bending moment for a given length and uniform load
        Max moment occurs at the mid-length of the member

        Equation
        --------
        M = w * l^2 / 8

        """
        w = abs(self.uniform_load)
        l = self.length

        if 'pinned' in self.conn and 'roller' in self.conn:
            return w * l ** 2 / 8
        else:
            raise Exception('max_moment method only supports simple beams. '
                            'Connections must be combination for pinned and '
                            'roller.')

    @property
    def max_shear(self):
        """Maximum shear force for a given length and uniform load
        Max shear occurs at the supports

        Equation
        --------
        V = w * l / 2

        """
        w = abs(self.uniform_load)
        l = self.length

        if 'pinned' in self.conn and 'roller' in self.conn:
            return w * l / 2
        else:
            raise Exception('max_shear method only supports simple beams. '
                            'Connections must be combination for pinned and '
                            'roller.')
