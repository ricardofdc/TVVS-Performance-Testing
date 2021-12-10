from locust import LoadTestShape, FastHttpUser, between
from tasks import DemoBlazeUserUserTaskSet
import sys

class DemoBlazeTestShape(LoadTestShape):
    # max number of users
    max_users = sys.maxsize
    # Number of users to start/stop per second
    spawn_rate = 2

    def tick(self):
        # no time-limit
        return (self.max_users, self.spawn_rate)

class DemoBlazeUser(FastHttpUser):
    # wait between 0.5 and 3 seconds between tasks
    wait_time = between(3, 10)
    # default host (don't change please)
    host = "https://demoblaze.com"
    # what tasks will MyUser be doing
    tasks = [DemoBlazeUserUserTaskSet]


