from locust import LoadTestShape, FastHttpUser, between
from tasks import DemoBlazeUserUserTaskSet

"""
TODO: Change this
"""
class DemoBlazeTestShape(LoadTestShape):
    # max number of users
    max_users = 50
    # Number of users to start/stop per second
    spawn_rate = 5

    # the tick() method returns either:
    #  - a tuple containing:
    #     1. maximum number of users
    #     2. user spawn or de-spawn rate (users per second)
    #  - None, ending the test
    # This method is called approximately every second.
    def tick(self):
        # In this example, for every instance of the test
        # there will be a maximum number of 50 users, which
        # increase at a rate of 5 users per second
        # 
        # So in the beginning of the test there are 0 users,
        # after 10 seconds, there are 50 users. And since
        # this method never returns None, the test will run
        # forever with 50 users
        return (self.max_users, self.spawn_rate)

class DemoBlazeUser(FastHttpUser):
    # wait between 0.5 and 3 seconds between tasks
    wait_time = between(3, 10)
    # default host (don't change please)
    host = "https://demoblaze.com"
    # what tasks will MyUser be doing
    tasks = [DemoBlazeUserUserTaskSet]


