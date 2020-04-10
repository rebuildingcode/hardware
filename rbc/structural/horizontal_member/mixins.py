class UniformlyLoadedMixin:
    @property
    def max_moment(self):
        """Maximum bending moment for a given length and uniform load
        Max moment occurs at the mid-length of the member

        Equation
        --------
        M = w * l^2 / 8

        """
        w = self.uniform_load
        l = self.length

        return w * l ** 2 / 8

    @property
    def max_shear(self):
        """Maximum shear force for a given length and uniform load
        Max shear occurs at the supports

        Equation
        --------
        V = w * l / 2

        """
        w = self.uniform_load
        l = self.length

        return w * l / 2
