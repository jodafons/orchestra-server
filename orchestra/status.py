
__all__ = ["JobStatus", "TaskStatus", "TaskAction"]


class JobStatus:

    UNKNOWN    = 'Unknown'
    REGISTERED = "Registered"
    ASSIGNED   = "Assigned"
    TESTING    = "Testing"
    BROKEN     = "Broken"
    FAILED     = "Failed"
    KILL       = "Kill"
    KILLED     = "Killed"
    COMPLETED  = "Completed"
    PENDING    = "Pending"
    RUNNING    = "Running"



class TaskStatus:

    UNKNOWN    = 'Unknown'
    HOLD       = "Hold"
    HOLDED     = "Holded"
    BROKEN     = "Broken"
    FAILED     = "Failed"
    KILL       = "Kill"
    KILLED     = "Killed"
    COMPLETED  = "Completed"
    REGISTERED = "Registered"
    TESTING    = "Testing"
    ASSIGNED   = "Assigned"
    ACTIVATED  = "Activated"
    PENDING    = "Pending"
    STARTING   = "Starting"
    RUNNING    = "Running"
    FINALIZED  = "Finalized"
    REMOVED    = "Removed"


#
# Task order
#
class TaskAction:
    RETRY      = "Retry"
    KILL       = "Kill"
    WAITING    = "Waiting"
    DELETE     = "Delete"


