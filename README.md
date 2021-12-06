# TVVS - Performance Testing

## What is Locust?

Locust is an easy to use, scriptable and scalable performance testing tool.

You define the behaviour of your users in regular Python code, instead of being stuck in a UI or restrictive domain specific language.

This makes Locust infinitely expandable and very developer friendly.

## Installation Guide

Clone this repository:

````
$ git clone https://github.com/ricardofdc/TVVS-Performance-Testing.git
````

[Install Python](https://docs.python-guide.org/starting/installation/) 3.6 or later, if you don't already have it.

Install Locust:

````
$ pip3 install locust
````

You may need to run the command as admin or with the `--user` flag.  
Validate your installation. If this doesn't work, [check the Locust's wiki](https://github.com/locustio/locust/wiki/Installation) for some possible solutions.

````
$ locust -V
locust 2.5.0
````

Great! Now we're ready to create our first test.

## References

[Locust Documentation - Locust 2.5.0 documentation](https://docs.locust.io/en/stable/index.html)
