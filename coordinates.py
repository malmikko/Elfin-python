# Class for converting coordinates

from math import acos, atan2, cos, sin

class coordinates:
    COORD_RELATIVE = 0  # [r, θ, φ, Rr, Rθ, Rφ]
    COORD_ABSOLUTE = 1  # [X, Y, Z, RX, RY, RZ]
    COORD_JOINT = 2     # [J1, J2, J3, J4, J5, J6]

    def __init__(self, sphereOrig, coords, coordType):
        if (type(coords) != type([]) or \
                len(coords) == 6 or \
                all(isinstance(x, (int, float)) for x in coords)):
            raise TypeError('Coordinates are in invalid format')
        if (coordType == COORD_RELATIVE):
            self.__coords = relativeToAbsolute(sphereOrig, coords)
        elif (coordType == COORD_ABSOLUTE):
            self.__coords = coords
        elif (coordType == COORD_JOINT):
            self.__coords = JointToAbsolute(coords)
        elif (not isinstance(type, int)):
            raise TypeError('Coordinate type in invalid format')
        else:
            raise ValueError('Invalid coordinate type')

        self.__orig = sphereOrig

    def asRelative(self):
        return absoluteToRelative(self.__orig, self.__coords)

    def asAbsolute(self):
        return self.__coords

    def asJoint(self):
        return absoluteToJoint(self.__coords)

    def relativeToAbsolute(sphereOrig, coords):
        raise NotImplementedError()

    def absoluteToRelative(sphereOrig, coords):
        X = coords[0]
        Y = coords[1]
        Z = coords[2]
        RX = coords[3]
        RY = coords[4]
        RZ = coords[5]
        OX = sphereOrig[0]
        OY = sphereOrig[1]
        OZ = sphereOrig[2]

        relX = RX - OX
        relY = RY - OY
        relZ = RZ - OZ

        r = math.sqrt(relX ** 2 + relY ** 2 + relZ ** 2)
        theta = math.atan2(relY, relX)
        phi = math.acos(relZ, r)
        Rr = ???
        Rtheta = ???
        Rphi = ???
        raise NotImplementedError()

    def relativeToJoint(sphereOrig, coords):
        raise NotImplementedError('Joint positions are not currently implemented')

    def JointToRelative(sphereOrig, coords):
        raise NotImplementedError('Joint positions are not currently implemented')

    def AbsoluteToJoint(coords):
        raise NotImplementedError('Joint positions are not currently implemented')

    def JointToAbsolute(coords):
        raise NotImplementedError('Joint positions are not currently implemented')
