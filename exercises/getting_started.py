from locust import TaskSet, HttpUser, LoadTestShape, task, constant
import time

class MyUserTaskSet(TaskSet):

    # A method with the name "on_start" will be called for each 
    # simulated user when they start.
    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})

    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")

    @task
    def slow(self):
        self.client.get("/slow")

    @task(3)
    def view_items(self):
        # Here we will load 10 different URLs by using a variable query 
        # parameter. In order to not get 10 separate entries in Locust's 
        # statistics we use the name parameter to group all those requests 
        # under an entry named "/item" instead.
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)

class MyUser(HttpUser):
    # default host
    host = "http://localhost:8080"

    wait_time = constant(0.5)

    tasks = [MyUserTaskSet]

class MyLoadTestShape(LoadTestShape):
    # the duration of the test
    time_limit = 60
    # max number of users
    max_users = 50
    # Number of users to start/stop per second
    spawn_rate = 2

    # the tick() method returns either:
    #  - a tuple containing:
    #     1. maximum number of users
    #     2. user spawn or de-spawn rate (users per second)
    #  - None, ending the test
    # This method is called approximately every second.
    def tick(self):
        # get time elapsed (in seconds)
        run_time = round(self.get_run_time())

        # check if time limit has been reached
        if run_time < self.time_limit:
            return (self.max_users, self.spawn_rate)
        else:
            return None
