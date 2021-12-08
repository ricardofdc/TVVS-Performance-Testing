from locust import FastHttpUser, LoadTestShape, task, constant

class LoadStagesShape(LoadTestShape):
    # test will run for 120 seconds
    time_limit = 120
    # max number of users
    max_users = 30
    # curve starts going down after 100 seconds
    end_load =  100
    # Number of users to start/stop per second
    spawn_rate = 5

    def tick(self):
        run_time = round(self.get_run_time())

        user_count = self.max_users if run_time < self.end_load else 0

        if run_time < self.time_limit:
            return (user_count, self.spawn_rate)
        else:
            return None

class PeakUser(FastHttpUser):
    # wait 0.5 seconds
    wait_time = constant(0.5)
    host = 'http://localhost:8080'

    @task
    def test_root(self):
        self.client.get("/")

