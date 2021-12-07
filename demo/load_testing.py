from locust import FastHttpUser, LoadTestShape, task, constant

class LoadStagesShape(LoadTestShape):
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
        {"duration": 20, "users": 5, "spawn_rate": 10},    # 0   - 20
        {"duration": 140, "users": 100, "spawn_rate": 10}, # 20  - 140
        {"duration": 160, "users": 5, "spawn_rate": 10},   # 140 - 160
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

class PeakUser(FastHttpUser):
    # wait 0.5 seconds
    wait_time = constant(0.5)
    host = 'http://localhost:8080'

    @task
    def test_root(self):
        self.client.get("/")

"""
    @task
    def test_route1(self):
        self.client.get("/route1")

    @task
    def test_route2(self):
        self.client.get("/route2")

    @task
    def test_route3(self):
        self.client.get("/route3")

    @task
    def test_route4(self):
        self.client.get("/route4")

"""
