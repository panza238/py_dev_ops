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

TODO:
- How to upload the package to PyPI.
