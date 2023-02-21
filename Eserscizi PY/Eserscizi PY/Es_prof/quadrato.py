from unittest import removeResult


class Quadrato:
    def __init__(self,x,y,lato):
        self.x=x
        self.y=y
        self.lato=lato
    
    def perimetro(self):
        return(self.lato*4)
    
    def area(self):
        return(self.lato*self.lato)

    def isdentro(self, xp, yp):
        if(self.x<xp and self.x + self.lato>=xp and self.y<=yp):
            pass