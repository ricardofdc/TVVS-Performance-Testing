from locust import FastHttpUser, LoadTestShape, task, constant

class MyShape(LoadTestShape):
    

    def __init__(self):
        super().__init__()

    def tick(self):
        # get current run_time
        run_time = round(self.get_run_time())
        # TODO: draw the users curve
        return None

class MyUser(FastHttpUser):
    # TODO: Change this
    wait_time = ...
    host = ...

    # TODO: Feel free to add more 
    @task
    def test_root(self):
        self.client.get("/")

