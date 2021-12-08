from locust import FastHttpUser, LoadTestShape, task, constant

class SpikeStagesShape(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.
    Keyword arguments:
        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
    """

    stages = [
        {"duration": 45, "users": 5, "spawn_rate": 100},    # 0   - 45
        {"duration": 60, "users": 100, "spawn_rate": 100},  # 45  - 60  - peak
        {"duration": 105, "users": 5, "spawn_rate": 100},   # 60  - 105
        {"duration": 120, "users": 100, "spawn_rate": 100}, # 105 - 120 - peak
        {"duration": 165, "users": 5, "spawn_rate": 100},   # 120 - 165
        {"duration": 180, "users": 100, "spawn_rate": 100}, # 165 - 180 - peak
        {"duration": 225, "users": 5, "spawn_rate": 100},   # 180 - 225
        {"duration": 240, "users": 100, "spawn_rate": 100}, # 225 - 240 - peak
        {"duration": 285, "users": 5, "spawn_rate": 100},   # 240 - 285
    ]

    def __init__(self):
        super().__init__()

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"]) # spawn rate is always 100
                return tick_data

        return None

class SpikeUser(FastHttpUser):
    # wait 0.5 seconds
    wait_time = constant(0.5)
    host = 'http://localhost:8080'

    @task
    def test_root(self):
        self.client.get("/")
