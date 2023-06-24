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
