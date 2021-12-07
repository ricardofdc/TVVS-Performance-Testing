# Exercises

## System Data

An e-commerce system has launched about a week ago (https://www.demoblaze.com/), and after the first week the following data was collected:

- Average online users: **50**
- Average requests per second: **30**

## System Requirements

Imagine an e-commerce system with the following non-functional performance requirements:

**(1)** The system must successfully answer at least 98% of incoming requests.

<details>
    <summary>💡 Hint</summary>
    A simple load test with the system collected data should suffice
</details>

---

**(2)** During black-friday (which lasts for 24 hours) the system's usage is expected to grow 100% (100 online users and about 60 requests per second). During this time, the system much reply successfully to at least 95% of incoming requests.

<details>
    <summary>💡 Hint</summary>
    Look at the slides and try to draw a RPS curve that resembles a stress testing curve!
</details>

---

**(3)** Besides black friday, the store also does flash sales that last about 1 hour. These flash days usually happen 6 times a day and causes the website's activity to grow 200% during these hours.

<details>
    <summary>💡 Hint</summary>
    Maybe try a peak testing approach!
</details>

## Exercises

For each non-functional requirement, write a performance test using the locust library.

You can find hints after each requirement if you need extra help!

### Tips and Tricks

For each performance requirements create a python script following the examples.

After that you can run it like this:

```bash
locust -f requirement1.py
```


