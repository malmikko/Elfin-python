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
        cobot.connect(server_ip, port, size, rbtID) #TODO: error handling
        initial_pos = coordinates.relativeToAbsolute(sphereOrig, [r2, 0, 0, 0, 0, 0])
        self.moveToAbsolute(initial_pos)

    def moveToAbsolute(self, pos):
        self.__cobot.MoveL(target)
        status = cobot.ReadMoveState()
        while Status(status) == Status.STATUS_MOVING:
            time.sleep(0.01)
            status = cobot.ReadMoveState()
        if Status(status) == Status.STATUS_IDLE:
            return 0
        else:
            return 1 # Error

    def moveToCoord(self, pos, coordType):
        
