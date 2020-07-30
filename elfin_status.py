# This file contains the status/error codes for the elfin robot.
# The list is currently incomplete.
from enum import Enum

class Status(Enum):
    STATUS_MOVING =              1009   # Robot is moving
    STATUS_IDLE =                1013   # Robot is waiting for a command to execute
    STATUS_ERROR =               1025   # Robot has encountered an error
    STATUS_TEACH =               1044   # Robot is in teach mode
    ERROR_COLLISION =           30000   # Safety shutdown due to collision
    ERROR_COLLISION_BODY =      30001   # Shutdown due to collision with robot body (?)
    ERROR_OVER_JOINT_LIMIT =    30002   # Joint was rotated over its limit
    ERROR_SINGULARITY =         30003   # Robot has multiple ways to move or it can't reach the point
    ERROR_CALCUALATION_FAILED = 30005   # Robot can't calculate the movement path
