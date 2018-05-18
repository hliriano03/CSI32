
class  SimpleRectangle:

    def __init__(self, l, w):

        self.l = l
        self.w = w
        self.area = l * w
        self.p = 2 * (l + w)

    def getLength(self):

        return self.l

    def getWidth(self):

        return self.w

    def getArea(self):

        return self.area

    def getP(self):

        return self.p

    def __eq__(self, other):

        if self.l == other.l and self.w == other.w:
            return True
        else:
            return False

    def __str__(self):

        return "Length = {} \nWidth = {} \nArea = {} \nPerimeter = {}".format(self.l,self.w,self.area,self.p)
    

    
