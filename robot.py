import elfin
import time
import coordinates
import elfin_status

class robot:

    def __init__(self, sphereOrig, server_ip, port = 10003, size = 1024, rbtID = 0, r1 = 90, r2 = 120):
        self.__ip = server_ip
        self.__port = port
        self.__packet_size = size
        self.__robotID = rbtID
        self.__sphereOrig = sphereOrig
        self.__cobot = elfin.elfin()
        self.__r1 = r1
        self.__r2 = r2
        cobot.connect(server_ip, port, size, rbtID) #TODO: error handling
        initial_pos = coordinates.relativeToAbsolute(sphereOrig, [r2, 0, 0, 0, 0, 0])
        self.__moveToAbsolute(initial_pos)

    def __waitForMovement(self):
        status = self.__cobot.ReadMoveState()
        while Status(status) == Status.STATUS_MOVING:
            time.sleep(0.01)
            status = cobot.ReadMoveState()
        return status

    def __moveToAbsoluteL(self, pos):
        # Linear movement
        self.__cobot.MoveL(target)
        status = __waitForMovement()
        self.__coords = coordinates(self.__sphereOrig, cobot.ReadPcsActualPos(), coordinates.COORD_ABSOLUTE)
        if Status(status) != Status.STATUS_IDLE:
            raise RuntimeError('Unexpected status: ' + Status(status))

    def __moveToRelativeL(self, pos):
        # Linear movement
        coords = coordinates.relativeToAbsolute(self.__sphereOrig, pos)
        __moveToAbsolute(coords)

    def __moveToRelativeC(self, newPos):
        # Circular arc on R2
        oldPos = self.__coords
        newPos = coordinates(self.__sphereOrig, newPos, coordinates.COORD_RELATIVE)
        midPos = coordinates.findSphericalMid(oldPos, newPos, self.__r2, self.__sphereOrig)
        via = midPos.asAbsolute()
        target = newPos.asAbsolute()
        self.__cobot.MoveC(target, via[0:2], 1)
        status = __waitForMovement()
        self.__coords = coordinates(self.__sphereOrig, cobot.ReadPcsActualPos(), coordinates.COORD_ABSOLUTE)

    def moveToCoord(self, pos, coordType):
        newCoords = coordinates(self.__sphereOrig, pos, coordType)
        newPos = self.__coords.asRelative()
        # Back to R1
        if (newPos[0] <= self.__r1):
            newPos[0] = self.__r1
            __moveToRelativeL(newPos)
        # Back to R2 while correcting the orientation for safe movement aroud the head
        newPos[0] = self.__r2; newPos[4] = 0; newPos[5] = 0
        __moveToRelativeL(newPos)
        # Move to new pos on R2
        newPos = newCoords.asRelative()
        newPos[0] = self.__r2; newPos[3] = oldPos[3]; newPos[4] = 0; newPos[5] = 0
        __moveToRelativeC(newPos) # TODO: test that the target orientation works with type=1
        # Move to R1
        newPos = newCoords.asRelative()
        newPos[0] = self.__r1
        __moveToRelativeL(newPos)
        # Move to the actual position
        __moveToRelativeL(newCoords.asRelative())
