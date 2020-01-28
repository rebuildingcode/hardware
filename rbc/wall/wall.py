
class Wall:
    """Abstract class for walls"""
    def __init__(self,
        width=4,
        layer_A='1/2" Gypsum Wall Board',
        insulation=None,
        framing='2x4',
        layer_1='1/2" Gypsum Wall Board', **kwargs):

        self.width = width

        self.layer_C = kwargs.get('layer_C')
        self.layer_B = kwargs.get('layer_B')
        self.layer_A = layer_A
        self.framing = framing
        self.insulation = insulation
        self.layer_1 = layer_1
        self.layer_2 = kwargs.get('layer_2')
        self.layer_3 = kwargs.get('layer_3')
