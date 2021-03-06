from locust import LoadTestShape, FastHttpUser, between
from tasks import DemoBlazeUserUserTaskSet

class DemoBlazeTestShape(LoadTestShape):
    # test will run for 1 hour
    time_limit = 60 * 60
    # max number of users
    max_users = 30
    # curve starts going down after 59.5 minutes
    end_load =  59 * 60 + 30
    # Number of users to start/stop per second
    spawn_rate = 1

    def tick(self):
        run_time = round(self.get_run_time())

        user_count = self.max_users if run_time < self.end_load else 0

        if run_time < self.time_limit:
            return (user_count, self.spawn_rate)
        else:
            return None

class DemoBlazeUser(FastHttpUser):
    # wait between 0.5 and 3 seconds between tasks
    wait_time = between(3, 10)
    # default host (don't change please)
    host = "https://demoblaze.com"
    # what tasks will MyUser be doing
    tasks = [DemoBlazeUserUserTaskSet]


