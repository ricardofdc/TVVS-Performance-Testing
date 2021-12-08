# TVVS - Performance Testing

# What is Locust?

Locust is an easy to use, scriptable and scalable performance testing tool.

You define the behavior of your users in regular Python code, instead of being stuck in a UI or restrictive domain specific language.

This makes Locust infinitely expandable and very developer friendly.

# Installation Guide

### 1. Install Python

[Install `Python`](https://docs.python-guide.org/starting/installation/) 3.6 or later, if you don't already have it.

```bash
# for Ubuntu/Debian
sudo apt-get install python3 python3-dev

# for fedora
sudo dnf install python3 python3-devel
```

[`pip`](https://pip.pypa.io/en/stable/installation/) usually comes bundled with Python, but make sure you have it installed anyway.

```bash
pip -V
# pip 21.2.4 from /home/.../python3.X/site-packages/pip (python 3.X)
```

### 2. Clone this repo

```bash
# clone the repo
git clone https://github.com/ricardofdc/TVVS-Performance-Testing.git

# change directory to project root
cd TVVS-Performance-Testing
```

### 3. Create python virtual environment (optional)

It is recommended to start a [python virtual environment](https://docs.python.org/3/tutorial/venv.html) to avoid problems with system dependencies:

```bash
# creating the environment (inside project root)
python3 -m venv env
```

Now it is important to activate the environment:

```bash
# UNIX & MaCOS
source env/bin/activate

# WINDOWS
env\Scripts\activate.bat
```

To make sure everything went well, try te following command:

```bash
which python
# the result should be something like this:
# /home/.../TVVS-Performance-Testing/env/bin/python
```

After you're done working on this project, simply run the following command to quit out of the virtual environment:

```bash
deactivate
```

### 4. Install Locust and other dependencies

Use pip to install project requirements on your virtual environment

```bash
pip install -r requirements.txt
```

Make sure that `locust` is installed and working:

```bash
locust -V
# locust 2.5.0
```

You may need to run the command as admin or with the `--user` flag.  
Validate your installation. If this doesn't work, [check the Locust's wiki](https://github.com/locustio/locust/wiki/Installation) for some possible solutions.

Great! Now we're ready to create our first test.

# Exercises

We developed a very simple Python server for you to run locally, in order to perform the first exercise. Run this command in order to start that server:

```` bash
python server
````

Then, to do these exercises open a new terminal and run this command to change to the `exercises` folder:

```` bash
cd exercises
````

## 1. Getting started

A Locust test is essentially a Python program. This makes it very flexible and particularly good at implementing complex user flows. But it can do simple tests as well, so lets start with that:

```` py
from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")
````

This user will make HTTP requests to `/hello`, and then `/world`, again and again. 

Put the code in a file named *`locustfile.py`* in your current directory and run `locust`:

```` bash
locust
# [2021-12-06 16:08:50,336] .../INFO/locust.main: Starting web interface at http://0.0.0.0:8089
# [2021-12-06 16:08:50,357] .../INFO/locust.main: Starting Locust 2.5.0
````

> If you want to run locust with other files you can run the command `locust -f <file_name>.py`

### Locust's web interface

Once you’ve started Locust, open up a browser and point it to http://localhost:8089. You will be greeted with something like this:

![Locust's web ui](img/home_page.png)

Point the test at our simple Python web server and try it out!

The following screenshots show what it might look like when running this test targeting 50 concurrent users with a ramp up speed of 1 users/s.

![Test1 statistics](img/test1_statistics.png)

Locust can also visualize the results as charts, showing things like requests per second (RPS):

![Test1 Total Requests per Second](img/test1_trps.png)

Response times (in milliseconds):

![Test1 Response Times](img/test1_rt.png)

Number of users:

![Test1 Number of Users](img/test1_nou.png)

## 2. Test E-Commerce System

An e-commerce system has launched about a week ago (https://www.demoblaze.com/), and after the first week the following data was collected:

- Average online users: **50**
- Average requests per second: **30**

**System Requirements**

The owner of this system told us that it has the following non-functional performance requirements:

**1.** The system must successfully answer at least 98% of incoming requests during an average load.

<details>
    <summary>💡 Hint</summary>
    A simple load test with the system collected data should be enough.
</details>


---

**2.** During black-friday (which lasts for 24 hours) the system's usage is expected to grow 100% (100 online users and about 60 requests per second). During this time, the system should reply successfully to at least 95% of incoming requests.

<details>
    <summary>💡 Hint</summary>
    Look at the slides and try to develop a test capable of drawing a Requests per Second (RPS) curve that resembles a stress testing curve!
</details>

---

**3.** Besides black friday, the store also does some flash sales that last about 1 hour. These flash sales usually happen 6 times a day and causes the website's activity to grow 300%. During this time the system should be able to reply successfully to at least 90% of incoming requests.

<details>
    <summary>💡 Hint</summary>
    In this case developing a spike test may be the best testing approach!
</details>

---

**4.** Challenge: Find out when the system stops answering more than 50% of incoming requests!

<details>
    <summary>💡 Hint</summary>
    Have you tried looking at breakpoint tests! 🤔
</details>

However the owner is not entirely sure that these requirements are met and needs you to test them. For each non-functional requirement, write a performance test using the locust library.

You can find hints after each requirement and a step-by-step guide bellow to help you if you want!

## Exercise guides

Locust offers some classes that can be extended for more configuration, you can find the documentation here:
- [HttpUser](http://docs.locust.io/en/stable/api.html#httpuser-class) and [FastHttpUser](http://docs.locust.io/en/stable/increase-performance.html)
- [LoadTestShape](http://docs.locust.io/en/stable/custom-load-shape.html)
- [TaskSet](http://docs.locust.io/en/stable/api.html#taskset-class) and [SequentialTaskSet](http://docs.locust.io/en/stable/api.html#sequentialtaskset-class)

```Python
from locust import LoadTestShape, FastHttpUser, task, constant, between
from random import randint

class LoadStagesShape(LoadTestShape):
    """
    The tick() method that returns
        - a tuple with the desired user count and spawn rate
        - or None to stop the tes
    Locust will call the tick() method approximately once per second.
    """
    def tick(self):
        user_count = 10
        spawn_rate = 1
        # user count will ramp up to 10 by increasing
        # the user_count by 1 user per second
        return (user_count, spawn_rate)

class PeakUser(FastHttpUser):
    # PICK THIS -> wait 0.5 seconds between tasks
    wait_time = constant(0.5)
    # OR THIS -> wait randomly between 1 and 3 seconds between tasks
    wait_time = between(1, 3)
    # where will the requests be sent
    host = 'https://demoblaze.com'

    @task
    def test_root(self):
        self.client.get("/")

    # this task will be 5 times more likely to be chosen
    @task(5)
    def test_root(self):
        # item IDs between 1 and 15
        item_id = randint(1, 15)
        self.client.get(f'/prod.html?idp_={item_id}')
```

### 2.1. Load Test Guide

```python
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
```
### 2.2. Stress Test Guide

Same as Load test, just increase the number of users OR decrease the `wait_time` between user tasks.

### 2.3. Spike Test Guide

```python
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
```

### 2.4. Breakpoint Test Guide

Keep increasing users over time. How about something like this:

```Python
class BreakpointShape(LoadTestShape):
    # max number of users
    max_users = sys.maxsize
    # Number of users to start/stop per second
    spawn_rate = 5

    def tick(self):
        # no time-limit
        return (self.max_users, self.spawn_rate)
```

# References

[Locust Documentation - Locust 2.5.0 documentation](https://docs.locust.io/en/stable/index.html)
