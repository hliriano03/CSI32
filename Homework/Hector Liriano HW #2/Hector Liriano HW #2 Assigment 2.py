# 3/4

# COMMENT: I read the problem and it wants you to return a Fraction object.
# However, I know I gave you the okay in class.
def __neg__(self):

    self._numer = -self._numer

    return self._numer

def __invert__(self):

    # COMMENT: Want to return a fraction type.
    # What about division by 0?
    return str(self._denom) + '/' + str(self._numer)
