from locust import LoadTestShape, FastHttpUser, between
from tasks import DemoBlazeUserUserTaskSet


seconds_in_an_hour = 60 * 60
normal_users = 30
spike_users = 4 * normal_users

class DemoBlazeTestShape(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.
    Keyword arguments:
        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
    """

    stages = [                                                                          # in hours
        {"duration": 3 * seconds_in_an_hour, "users": normal_users, "spawn_rate": 5},   # 0  - 3
        {"duration": 4 * seconds_in_an_hour, "users": spike_users, "spawn_rate": 5},    # 3  - 4  - peak
        {"duration": 8 * seconds_in_an_hour, "users": normal_users, "spawn_rate": 5},   # 4  - 8
        {"duration": 9 * seconds_in_an_hour, "users": spike_users, "spawn_rate": 5},    # 8  - 9 - peak
        {"duration": 12 * seconds_in_an_hour, "users": normal_users, "spawn_rate": 5},  # 9  - 12
        {"duration": 13 * seconds_in_an_hour, "users": spike_users, "spawn_rate": 5},   # 12 - 13 - peak
        {"duration": 16 * seconds_in_an_hour, "users": normal_users, "spawn_rate": 5},  # 13 - 16
        {"duration": 17 * seconds_in_an_hour, "users": spike_users, "spawn_rate": 5},   # 16 - 17 - peak
        {"duration": 20 * seconds_in_an_hour, "users": normal_users, "spawn_rate": 5},  # 17 - 20
        {"duration": 21 * seconds_in_an_hour, "users": spike_users, "spawn_rate": 5},   # 20 - 21 - peak
        {"duration": 24 * seconds_in_an_hour, "users": normal_users, "spawn_rate": 5},  # 21 - 24
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"]) # spawn rate is always 100
                return tick_data

        return None

class DemoBlazeUser(FastHttpUser):
    # wait between 0.5 and 3 seconds between tasks
    wait_time = between(3, 10)
    # default host (don't change please)
    host = "https://demoblaze.com"
    # what tasks will MyUser be doing
    tasks = [DemoBlazeUserUserTaskSet]


