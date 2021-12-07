# TVVS - Performance Testing

# What is Locust?

Locust is an easy to use, scriptable and scalable performance testing tool.

You define the behaviour of your users in regular Python code, instead of being stuck in a UI or restrictive domain specific language.

This makes Locust infinitely expandable and very developer friendly.

# Installation Guide

### 1. Install Python

[Install Python](https://docs.python-guide.org/starting/installation/) 3.6 or later, if you don't already have it.

### 2. Clone this repo

```bash
# clone the repo
git clone https://github.com/ricardofdc/TVVS-Performance-Testing.git
# change directory to project root
cd TVVS-Performance-Testing
```

### 3. Create python virtual environment

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

To make sure everything went well, try te following commands

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
which locust
# /home/.../TVVS-Performance-Testing/env/bin/locust
```

You may need to run the command as admin or with the `--user` flag.  
Validate your installation. If this doesn't work, [check the Locust's wiki](https://github.com/locustio/locust/wiki/Installation) for some possible solutions.

Great! Now we're ready to create our first test.

# Tutorial

We developed a very simple Python server for you to run locally, in order to perform the first test. Run this command in order to start that server:

```` shell
$ py server
````

Then, to do this tutorial open a new terminal and run this command to change to the `tutorial` folder:

```` shell
$ cd tutorial
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

```` shell
$ locust
[2021-12-06 16:08:50,336] .../INFO/locust.main: Starting web interface at http://0.0.0.0:8089
[2021-12-06 16:08:50,357] .../INFO/locust.main: Starting Locust 2.5.0
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
> Note:   
> Interpreting performance test results can be quite complex.  
> In this graph above we can see that this server has a bottleneck of around 18 *HelloWorldUsers*, performing around 2.1 requests per second.

Response times (in milliseconds):

![Test1 Response Times](img/test1_rt.png)

Number of users:

![Test1 Number of Users](img/test1_nou.png)

## 2. Writing a locustfile



# References

[Locust Documentation - Locust 2.5.0 documentation](https://docs.locust.io/en/stable/index.html)
