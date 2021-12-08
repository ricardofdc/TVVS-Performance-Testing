# TVVS - Performance Testing

- Gonçalo Marantes - up201706917@edu.fe.up.pt
- Ricardo Cardoso - up201604686@edu.fe.up.pt
- Tiago Silva - up201705985@edu.fe.up.pt

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

### 2. Clone our repository

Clone [this](https://github.com/ricardofdc/TVVS-Performance-Testing) GitHub repository, with the following command:

```bash
# clone the repo
git clone https://github.com/ricardofdc/TVVS-Performance-Testing.git

# change directory to project root
cd TVVS-Performance-Testing
```

### 3. Create python virtual environment (optional)

It is recommended to start a [python virtual environment](https://docs.python.org/3/tutorial/venv.html) to avoid problems with system dependencies. However, this is optional and everything should work fine either way.

```bash
# creating the environment (inside project root folder)
python3 -m venv env
```

Now your project folder will look something like this:

```
.
├── demo
│  └── ...
├── env <- NOTICE THIS FOLDER!
│  ├── bin
│  ├── include
│  ├── lib
│  ├── lib64 ⇒ lib
│  └── pyvenv.cfg
├── exercises
│  └── locustfile.py
├── img
│  └── ...
├── install.md
├── README.md
├── requirements.txt
└── server
   └── __main__.py
```

Now it is important to activate the environment:

```bash
# UNIX & MaCOS
source env/bin/activate

# WINDOWS
env\Scripts\activate.bat
```

To make sure everything went well, try te following command (UNIX only):

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
