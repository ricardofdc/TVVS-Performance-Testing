from locust import TaskSet, HttpUser, LoadTestShape, task, constant
import time

class MyUserTaskSet(TaskSet):

    # A method with the name "on_start" will be called for each 
    # simulated user when they start.
    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})

    # Methods decorated with @task are the core of your locust file. 
    # For every running user, Locust creates a greenlet (micro-thread), 
    # that will call those methods.
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
    
    # Here we will define the waiting time between the user's tasks
    #
    # With `wait_time` = constant(0.5) this user will execute 
    # its tasks with constant interval of 0.5 seconds between each
    # task.
    #
    # Another way we can specify the wait time is with
    # between(). With `wait_time` = between(1, 5), the user
    # will execute its tasks with a random interval between 1
    # and 5 seconds.
    wait_time = constant(0.5)

    # The tasks array defines the tasks that will be executed
    # by this user. In this case, the array as an element which
    # is an instance of MyUserTaskSet. So this user will execute
    # the tasks defined in the MyUserTaskSet class
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
