from locust import TaskSet, task
import random
import string
import re

class DemoBlazeUserUserTaskSet(TaskSet):
    # demoblaze API url
    api_host = "https://api.demoblaze.com"
    # session token
    token = ''
    # default item ID
    item_id = 1

    """
    on_start is always executed once at the beginning of the task (duh)
    """
    def on_start(self):
        # randomize auth credentials
        auth_credentials = {
            "username": ''.join((random.choice(string.ascii_lowercase) for x in range(10))),
            "password": ''.join((random.choice(string.ascii_lowercase) for x in range(10))) 
        }

        # sign up
        self.client.options(f"{self.api_host}/signup")
        response = self.client.post(f"{self.api_host}/signup", json = auth_credentials)

        # login and set auth token
        self.client.options(f"{self.api_host}/login")
        response = self.client.post(f"{self.api_host}/login", json = auth_credentials)
        self.token = re.match("\"Auth_token: (.+?)\"", response.text)[1]

    """
    Visit main page
    - Prob: 2 / 10
    """    
    @task(2)
    def main_page(self):
        self.client.get("/")
        self.client.get(f"{self.api_host}/entries")   
    
    """
    Visit product page
    - Prob: 3 / 10
    """    
    @task(3)
    def click_product(self):
        self.pick_and_click_product()
    
    """
    Add product to cart
    - Prob: 2 / 10
    """  
    @task(2)
    def add_product(self):
        self.pick_and_click_product()
        self.add_to_cart()
    
    """
    Add product to cart and go to cart
    - Prob: 2 / 10
    """  
    @task(2)
    def add_and_buy_product(self):
        self.pick_and_click_product()
        self.add_to_cart()
        self.check_cart()

    """
    Visit cart page
    - Prob: 2 / 10
    """  
    @task(1)
    def view_cart(self):
        self.check_cart()

    """
    HELPER METHODS
    """
    def pick_and_click_product(self):
        # choose random product
        self.item_id = random.randint(1, 15)
        # view product
        self.client.get(f"/prod.html?idp_={self.item_id}")
        self.client.options(f"{self.api_host}/check")
        self.client.options(f"{self.api_host}/view")
        self.client.post(f"{self.api_host}/check",json={"token": self.token})
        self.client.post(f"{self.api_host}/view",json={"id": self.item_id})

    def add_to_cart(self):
        self.client.options(f"{self.api_host}/addtocart")
        self.client.post(f"{self.api_host}/addtocart", json = {"id": "fb3d5d23-f88c-80d9-a8de-32f1b6034bfd", "cookie": self.token, "prod_id": self.item_id, "flag": 'true'})
    
    def check_cart(self):
        self.client.get("/cart.html")
        self.client.options(f"{self.api_host}/check")
        self.client.options(f"{self.api_host}/viewcart")
        self.client.post(f"{self.api_host}/check", json={"token": self.token})
        self.client.post(f"{self.api_host}/viewcart", json={"cookie": self.token,"flag":'true'})
        self.client.options(f"{self.api_host}/view")
        self.client.post(f"{self.api_host}/check", json={"token": self.token})
        self.client.post(f"{self.api_host}/view", json={"id": self.item_id})
