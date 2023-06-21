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
be able to use the `requests` module and parse the output)*

### Building the CLI tool
MINIMAL WORLD TIMER V0 WORKNG!
TODO:
- EXPLAIN WORKINGS, FEATURES AND LIMIATIONS (LOGS BASE PATH CONFIG, ONE -c FLAG PER CITY, LOGS HANDLED INEFFICIENTLY)
- CONFIGURE GIT --LOCAL CORRECTLY!
