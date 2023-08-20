# Roadmap
This document serves as a roadmap to document the changes or the features added to the project after going through
each chapter. This is not exactly a changelog, though. This is more of a summary explaining the motivation behind 
each change or addition.

## Chapters 01 - 03
The first three chapters were bundled together into a single section. These chapters cover:
- **Python basics** (I'm assuming some prior experience with Python)
- Interacting with the **file system**
- Working with **CLI tools**

With this in mind, we'll start by creating a simple CLI tool that:
1. Takes one or more cities as input from the user
2. Requests the time for those cities through an API
3. Displays the current time for each city
4. Logs the information about the requested times to a log file

*(I intentionally decided to use an API to get the times, instead of using a library like `pendulum`, in order to 
be able to use the `requests` module and parse the `JSON` output)*

### Building the CLI tool

At this point we have a minimal working tool. It's not much to write home about, but it is sufficient for now.

In the book three framework for creating command line tools are shown: `argparse`, `Click` and `Fire`. I chose `Click`
to develop the tool because it seems to have the best trade-off between simplicity and control.

**When to use each tool?** In general, the rule of thumb is as follows:
- `argparse`: Use only if you need very fine-grained control over the input arguments and options of the tool being built.
For example, if you are developing a complex command with multiple nested sub-commands and options.
- `Click`: Use generally, for low complexity CLI tools. You can create powerful commands with relatively little code.
On the downside, if your CLI tool scales in complexity (e.g. you need to start nesting commands), the amount of code needed
will increase quite a lot. At that point, it might make more sense to go with `argparse`
- `Fire`: Use when you are not really building a CLI tool, but just want to expose a function for the user to iteract with. 
It's power relies on the fact that you can turn any simple function into a tool with *almost NO extra code*. This is indeed
very powerful and can be used in many ways. One useful example is the case in which you need to try what different 
functions do in a codebase you are not familiar with. You can interact with each function through the CLI thanks to `Fire`. 
Also, this framework has an interactive mode, very useful for debugging. On the downside, compared to the former frameworks, 
it gives you the least control over how arguments are parsed. Also, developing a CLI tool involves quite a lot of trial and error, 
since you don't exactly know how the changes in your function will affect how the arguments are parsed and fed to the 
function itself. Since `Fire` is based on *introspection*, arguments and function are not decoupled as they are in `Click`,
for example. 


The only thing I don't like about `Click` is that one has to pass one `--city` (o `-c`) flag per city. This is because
`--city` is an *option* rather than an *argument* (they are basically the same, but arguments are positional). The crazy
thing is that one could pass a list of cities with only one flag in `Click 7.X`... But this was changed in `Click 8.X`.

*I was able to get the desired behaviour with `argparse`, but not with `Fire`*

### Room for improvement
- Requests to the API could be parallelized to improve performance. They are handled sequentially now.<br>
*Spoler alert! We will probably do this later on, when performance benchmarking tools are introduced.*
- The logs could be handled better:
  - Logs could probably be handled better with `logging`. The current way just gave us the excuse to write files as shown in the book.
  - Logs should store information when the app fails (`stderr`). Not only on successful executions
  - The logs directory could probably be configured through a config file, rather than having to set the environment variable.

## Chapter 04
This chapter is called "Useful Linux Utilities". Many diagnostic tools are displayed in this chapter. However, I chose
to focus mainly on the Python specific ones. These new tools won't add new functionality to our World Timer app, but 
they are intended to provide complementary information about how the app runs (in terms of performance).

Other things will be introduced in this chapter:
1. We are going to start versioning this repository's releases, and we will
keep a changelog documenting all the changes between one version and another. For now, the different versions will be
managed manually by cahnging the `version` attribute in the `pyproject.toml` file.
2. Also, the main repository's `main` branch will now be protected. So we won't be pushing directly to `main`. Instead, we
will be pushing our changes to a feature branch, and then merge the feature branch to the `main` branch. (In short, this
aims to make the workflow more gitflow-friendly)

### Disk Utilities
**Disclaimer! I am not going to dig deep into these tools here! I'll just provide an overview of what the book shows**

In terms of disk performance,
two commands are mentioned: `dd` and `iostat`. These are somewhat complementary. `dd` is used to transfer (read / write)
data. `iostat` is used to monitor data transfer. The book makes an important distiction between **throughput** and
**IOPS**. Throughput is how much data is transferred per unit of time (usually expressed in megabytes per second `MB/s`). 
IOPS is how many input / output operations are carried out per unit of time (usually expressed in transfers per second `tps`).
Lastly, in terms of measuring disk performance, the book presents the `fio` tool. To be honest, I have not experimented 
much wth this tool. It is highly flexible and there are many options to customize stress tests, but this level of control over the
performance tests comes at a cost: there is a learning curve to `fio`. If this sparked your curiosity, you can find the `fio` documentation
(which include an examples section) [here](https://fio.readthedocs.io/en/latest/index.html).

Moving away from disk performance, and into disk partitioning, a few tools are shown: `fdisk`, `parted`, `lsblk` and `blkid`.
They all help with partition managing.

### Network Utilities
In this section, two **very** useful tools are displayed: the `ab` CLI tool and the `molotov` Python library. Two simple
scripts will be available in the `utils` directory. For information on how to run them, see the Utils section in `README.md`.

In the future, we will add complexity to both tools. For now, they serve as a quick introduction.

**WARNING!** These tools might overload a server if not used correctly. Be careful when choosing the arguments. 

**TIP:** you can use `https://example.com/` to test any of these tools

#### AB (Apache Benchmark)
The `load_test_ab.py` script was created to demonstrate the `ab` CLI tool. This tool is very simple to use, and usually comes 
already installed in most Linux (and macOS) distributions. We could have created a bash script to run the exact same things,
but this gave us the oportunity to use the `subprocess` module, which was introduced in Chapter 3.

#### Molotov
The `load_test_molotov.py` script was created to demonstrate the very basics of the `molotov` Python library. There is 
much more to it, but this is enough for now. We will explore more of its features in the future.

In this simple example, we wrote 2 tests: one that passes and one that fails. By adjusting the weight parameter on the 
`scenario` decorator, we can control how many times each scenario is run. In this case, 80 percent of the times the
`pass` scenario is run and 20 percent of the times the `fail` scenario is run. I have found that capturing the output
of `molotov` can be a bit difficult. What I have found toto work is to direct de output to a log file.

One final comment on this: if you went through the script, you probably have noticed the `async` keyword being used. 
This is because `molotov` uses the `asyncio` module to run the tests. This allows the tests to be ran in **multiple threads**.
I won't dive deep into this topic right now, but we will get there when we start trying to improve the performance of the app.

#### Locust
There is another Python library for load testing called `locust`. I have not used it, but is seems to be a bit bigger than `molotov`.
The [GitHub project](https://github.com/locustio/locust) has more recent commits, and many more contributors. 
So it might be worth checking it out. I might add  it in the future.
The project's official website can be found [here](https://locust.io).

### CPU Utilities
Not much to say about this section. The book mentions `top`, `htop` and `ps` as useful tools for monitoring CPU usage
(and other resources).

### Shell customization
The section provides lots of information about how to customize the shell (bash, zsh, etc.) through the _dotfiles_.<br>
Also, it provides a way to customize the Python shell or REPL.

#### PYTHONSTARTUP
In the `utils` directory, we have a file called `python_startup.py`. This file is used to customize the Python shell.
Every time a new Python shell is spawned, everything in this file will be imported. This is useful in case there are
functions or methods you want to have available in every shell.<br>
The only thing one has to do in order to use the script is to set the `PYTHONSTARTUP` environment variable.

_We are setting more environment variables... it might make sense to start handling them through a single file..._

### DEBUGGING
The book mentions `pdb` as a tool to debug Python code. It is a very simple, yet powerful tool. You won't see much of
it in this project because I plan on committing only working code. But you can find an example  in `utils/pdb_example.py`.
Being able to debug code quickly is a great skill to have. I highly encouraged you to start using `pdb` as a debugging
tool. [Here](https://realpython.com/python-debugging-pdb/) you can find a good RealPython post on how to get started.

#### strace
The book also mentions `strace` as a debugging tool. I have not included much information about this tool, since it is only avalibable on Linux. If you are working on a machine with Linux, it is worth to check out `strace`.


### BENCHMARKING
We will be using `timeit` as a benchmarking tool. This tools allows us to measure the performance of our app in terms of how long it takes to run. This goes without saying, but, when using `timeit`, you should compare results that have run on the same infrastructure (e.g. on the same machine or server).
To measure performace, we will be using the `timeit.repeat` function. The two most important parameters of this function are `repeat` and `number`. `repeat` is the number of benchmarking tests to run, and `number` is the number of times the code is run per test. A simple example makes this a lot clearer.<br>
**Example:**
```python
import timeit

def my_function():
    # code to be timed

stmt = "my_function()"  # statement to be timed

times = timeit.repeat(stmt=stmt,  repeat=5, number=10)
print(times)
```
This code means that my_function will be run a total of 50 times. The `times` variable, the return value of the `timeit.repeat` function, will be a list 5 values. Each of these 5 values corresponds to 10 runs of `my_function`. So, if the first value is 20, that means that 10 runs of `my_function` took roughly 20 seconds. Averaging this, we get a value of 2 seconds per run.

In the future, we will be adding a load testing tool to benchmark our application. Right now, we won't because we don't want to overload the server of an API we don't own (or have permission to abuse).


## Chapter 05
This chapter focuses on packaging and software distribution.

### Native Python packaging
For native Python packaging, we will leverage the `setuptools` library. This library does most of the heavy lifting for us.

To create a package from our module, one has to create a `setup.py` file in the root directory of the project. Once the file is created, we can run `python setup.py sdist`, which will create a `tar.gz` file. This file *is* the package. The `tar.gz` file can be installed through `pip`.
After running `python setup.py sdist` you will notice a few newly created directories. Feel free to explore them. The one that is important to us is `dist`. Inside this directory, we will find the `.tar.gz` file.
You can try it out by creating a new empty virtual environment, and running `pip install <path/to/file>.tar.gz`.
Alternatively, you can use `python setup.py install` to install the package (but you will need access to `setup.py` file).
One thing to watch out for, in this basic use case, are dependencies. You might successfully install the package, but the app won't run, or it will run into errors due to missing packages in the new virtual environment.

If you are using `poetry` (as I am) to manage project dependencies, you might run into some trouble when trying to package the module. Modifying the `pyproject.toml` file worked for me. I had to:
1. Remove the line containing `packages = [{include = "project-name"}]`
2. Rename the poetry project to `name = "world-timer"`, and then reinstall the poetry project (by running `poetry install`).


### PyPI
The Python Package Index (PyPI) is a repository of Python software that allows users to host Python packages and also install from it. This means that you can upload your packages, and then install them somewhere else (as long as you have an internet connection).

`twine` makes uploading pakcages a lot easier. You can upload a package to the test PyPI repository by running `twine upload --repository testpypi ./dist/*`. For this, you will need to create an ccount on test PyPI, generate a token, and create a config `.pypirc` file. [The test PyPI website](https://test.pypi.org/) will show you the steps to generate the token and config file.

In my case, I was able to install the pakcage I uploaded by running `pip install --no-deps --index-url https://test.pypi.org/simple/ world-timer`. I had to use the `--no-deps` flag because I kept running into dependency errors. They can be sorted out by being a bit tidier about the packaging process. For right now, I'll call it "good enough".

To be able to push to the actual PyPI repository, you will need a bit more leg-work (Description, Licenses, and other files). There are many articles about how to get a package ready for PyPI. Feel free to browse around!

## Debian & RPM packaging
I'm skipping over this section... I am not so interested in this type of package distribution right now.


## systemd
Since I am running a machine with macOS, I will not be using `systemd`. Instead, I will be working with the `launchd` tool (which is kind of like `systemd` for macOS). I will be using `launchctl` to interact with `launchd`.<br>

Just as a proof of concept, I have created an automated process that prints "hello from launchctl" every 5 seconds. You will find the `.plist` file in the `misc` directory. In this file, the process' config is defined.
To run it, you will have to:
- Replace PATH_TO_PYTHON with the actual path to the Python binary you are using
- Replace PATH_TO_REPO with the path to the repository
- run `launchctl load misc/world-timer.plist` (This "turns on" the process)

You should see the output in a file called `launctl_log.log`. <br>
To stop the process, run `launchctl unload misc/world-timer.plist`.

Feel free to play around with it!


## Chapter 06
This chapter goes over CI/CD: Continuous Integration and Continuous Delivery.

### CI / CD Responsibilities:
Responsibilities of each part of the CI and CD process:
- Dibujo del primer párrafo. ¿Cuáles son las responsabilidades del CI y CD?
  
### Makefile
A makefile is a file that contains instructions to achieve a specific goal. This is a fairly general description of what a makefile is, but it is a good place to start. Makefiles are very versatile tools, and can be used for a wide variety of purposes.
They are more frequently used in compiled languages (such as C os C++) than in interpreted languages (such as Python). However, makefiles can almost always be leveraged. [Here](https://makefiletutorial.com/) you can find a great tutorial.
**Since I am working on MacOS, I will be using `gmake` instead of `make` as my make tool.**
In this case, I created a very simple makefile. Each *target* groups a series of commands to be executed. In this case, I have created the following targets:

- poetry.lock: installs poetry project and creates `.lock` file
- logs_setup: creates logs directory
- run: runs the app
- clean: removes `__pycache__` files
- dist/*.tar.gz: builds the packages source distribution

With `poetry.lock` and `dist/*.tar.gz` the real power of make is shown. make will track these files and run **only** when the files needed to produce them (provided as dependencies) are modified. Try running `gmake dist/*.tar.gz` twice to see the effect!

### Cloud Computing
- AWS Code Pipeline for deploy? Or GCP Cloud Build?


## Chapter 07: Monitoring and Logging
This chapter is about monitoring and logging. The chapter starts by making a pretty big argument for automation (and hating on CTOs and founders, for some reason...). 
Quote: *"The most significant impact you can have in a company is to set up continuous integration and continuous delivery. [...].Loggong follows close behind automation in importance"*

The first part of the chapter can be summarized as follows: 
- *"Given a system, you should always know how is it monitored and how is it logging."*
A few monitoring and logging tools are introduced. `prometheus` is demonstrated in an example.

### Prometheus
Prometheus is a monitoring tool. Prometheus is a database that stores an application's metrics. For example: the number of requests, how long the requests take, the number of errors, the number of users, etc.
In Python, we can use the `prometheus_client` library to interact with Prometheus. Through the client we can define the metrcis we want to track, and then send them to Prometheus. Prometheus will run in it's own server and will process the metrics (for example, it will send the metrics over to another database for storage, or to a data visualization tool).

Also, a nice-to-have feature that Prometheus offers is its built in alert system. Alertmanager is a tool to send alerts when some metric goes out of bounds.

I have created a simple example of how to use the `prometheus_client` library, taken directly from the [documentation](https://github.com/prometheus/client_python). For now this is enough. When we start using containerization technology (i.e. Docker), we will dig a bit deeper into Prometheus and use the tool to log metrics for our app.

Our example creates a dummy request processor, and only uses the `Summary` metric to log information abour processed requests. The example launches a Prometheus server on port 8000 to visualize (rather poorly) the metrics.

To run it, simply run `poetry run python misc/prom_test.py`. You will be able to see the metrics in `localhost:8000` through your browser.

### StatsD & Graphite
The books mentions `statsd` and `graphite` as alternatives to Prometheus. I have not used either of them.

### Logging
Python's logging module is a very powerful and useful tool. [Here's](https://realpython.com/python-logging/) a great Real Python post that goes over it.
I have added a simple example `log_example.py` to the `misc` directory as a sandbox to play with the tool. However I strongly recommend going through the Real Python post mentioned above. Even in this post, there are many features that are not covered. Python's logging module is as complex as it is powerful.

In the `world-timer` app, logging is now handled by the `logging` module. So the parts of the code that wrote information to a file through the `write` method were removed. 
I decided to go with the `TimedRotatingFileHandler` instead of the `FileHandler`. This class gives us the ability to rotate the log file periodically. In this case, the rotation is done every day. Every separate log file is named with the date as a suffix. The suffixes are added to the files being rotated, so the first file (that is not rotated) won't have any suffix. A simple detail that bugs me a little bit is that one can't customize the name of the log file (So it won't be as pretty, but it will be just as useful).

I decided to go with this approach because it illustrates better a production situation where the app is running 24/7, and the logs need to be identified by date.


## Chapter X - Containerization
Since everything in this book is a lot easier to show in a running app, and to simulate running an app we need different components working together, I decided to move the containerization chapter to now. So we will explore this technology next.
