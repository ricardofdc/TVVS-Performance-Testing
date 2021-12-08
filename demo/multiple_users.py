"""
WARNING: THIS DOES NOT WORK!
"""

from re import S
from locust import FastHttpUser, LoadTestShape, task, constant, between
import random
import string  

class LoadStagesShape(LoadTestShape):
    # test will run for 120 seconds
    time_limit = 120
    # max number of users
    max_users = 30
    # curve starts going down after 100 seconds
    end_load =  100
    # Number of users to start/stop per second
    spawn_rate = 5

    def __init__(self):
        super().__init__()

    def tick(self):
        run_time = round(self.get_run_time())

        user_count = self.max_users if run_time < self.end_load else 0

        if run_time < self.time_limit:
            return (user_count, self.spawn_rate)
        else:
            return None

class ApiUser(FastHttpUser):
    # wait 0.5 seconds
    wait_time = between(1, 2)
    host = 'https://api.demoblaze.com'

    @task
    def test_login(self):
        self.client.post("https://api.demoblaze.com/login", json={"username": "cenas", "password": "cenas"})

    @task
    def test_signup(self):
        self.client.post("https://api.demoblaze.com/signup", json=self.generate_random_user())

    def generate_random_user(self):
        return {
            "username": ''.join((random.choice(string.ascii_lowercase) for x in range(5))),
            "password": ''.join((random.choice(string.ascii_lowercase) for x in range(5))) 
        }

class StorefrontUser(FastHttpUser):
    # wait 0.5 seconds
    wait_time = constant(0.5)
    host = 'https://demoblaze.com'

    @task
    def test_root(self):
        self.client.get("/")

    # this task will be 5 times more likely to be chosen
    @task(5)
    def test_root(self):
        # item IDs between 1 and 15
        item_id = random.randint(1, 15)
        self.client.get(f'/prod.html?idp_={item_id}')

