from locust import FastHttpUser, LoadTestShape, task, constant
import sys

class BreakpointShape(LoadTestShape):
    # max number of users
    max_users = sys.maxsize
    # Number of users to start/stop per second
    spawn_rate = 5

    def tick(self):
        # no time-limit
        return (self.max_users, self.spawn_rate)

class BreakpointUser(FastHttpUser):
    # wait 0.5 seconds
    wait_time = constant(0.5)
    host = 'http://localhost:8080'

    @task
    def test_root(self):
        self.client.get("/")
