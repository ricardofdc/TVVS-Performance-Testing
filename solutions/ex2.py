from locust import LoadTestShape, FastHttpUser, between
from tasks import DemoBlazeUserUserTaskSet

class DemoBlazeTestShape(LoadTestShape):
    # test will run for 24 hours
    time_limit = 24 * 60 * 60
    # max number of users
    max_users = 30 * 2 # DOUBLE THE USERS
    # Number of users to start/stop per second
    spawn_rate = 1

    def tick(self):
        run_time = round(self.get_run_time())

        if run_time < self.time_limit:
            return (self.max_users, self.spawn_rate)
        else:
            return None

class DemoBlazeUser(FastHttpUser):
    # wait between 0.5 and 3 seconds between tasks
    wait_time = between(3, 10)
    # default host (don't change please)
    host = "https://demoblaze.com"
    # what tasks will MyUser be doing
    tasks = [DemoBlazeUserUserTaskSet]


