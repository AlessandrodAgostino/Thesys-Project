#@author: Alessandro d'Agostino
import cmath
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


class Branch:
    """
    This class intends to implements the concept of 'branche' in a more complicated L-system drawing.
    Every branch is intended as an ordered couple of points in a complex space(about now).
    Every branch knows from who it was genereted and who it generates.
    A branch knows if it's a ramification's end (Free extreme)
    Every branch knows its own level of iteration.
    """

    def __init__(self,
                 tail = complex(0,0),
                 head = complex(0,1), #as complex numbers
                 iter_lev = 0,
                 origin = None):
        self.tail = tail #Tail coordinates
        self.head = head #Head coordinates
        self.iter_lev = iter_lev #Iteration Level
        self.origin = origin #Who generates this branch, if 'None' the branch is the starting one.
        self.generate = [] #Who is generated by this branch.

    def draw(self, **kwargs):
        plt.plot((self.tail.real,self.head.real), (self.tail.imag, self.head.imag), **kwargs)

    def thick_draw(self, thick,**kwargs):
        #Quantity useful for drawing
        # thick : Ratio between length and width
        l = abs(self.tail - self.head)
        pivot = [self.tail.real,self.tail.imag]
        ll_corner = (pivot[0]-l*thick/2, pivot[1]) #Lower-left corner
        theta = - (np.pi/2 - cmath.phase(self.head - self.tail))/np.pi*180

        #transformation
        ts = plt.gca().transData
        tr = mpl.transforms.Affine2D().rotate_deg_around(pivot[0],pivot[1], theta)
        t = tr + ts

        #Rotated rectangle
        rect = mpl.patches.Rectangle(ll_corner,l*thick,l,linewidth=2,edgecolor='r',facecolor='r',transform=t)

        plt.gca().add_patch(rect)
