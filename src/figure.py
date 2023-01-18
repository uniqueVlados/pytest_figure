class Figure:
    area = 0

    def __init__(self):
        pass
    
    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError
        return self.area + figure.area
