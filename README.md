# AI Lab 3 Multi-Armed Bandits
Multi-armed bandits are a simple reinforcement learning method that forms the foundation of many large-scale recommender systems.

To get an overview of multi-armed bandits in their implementation:

* ["Towards Data Science" introduction to multi-armed bandits](https://towardsdatascience.com/solving-multiarmed-bandits-a-comparison-of-epsilon-greedy-and-thompson-sampling-d97167ca9a50)

* [Academic overview paper](https://arxiv.org/pdf/1402.6028)

## Task
In the lab, you will implement a multi-armed bandit to solve an example problem.
Your bandit will need to beat a “naïve” benchmark.
Also, we will determine the best-performing bandit of all submissions.

## Requirements
You need to have the following software installed and accounts set up to absolve this exercise:

* [Python 3.8](https://www.python.org/);

* [git](https://git-scm.com/);

* An account on the CS Department's [GitLab](https://git.cs.umu.se/) server;

* A text editor or development environment like [Visual Studio Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/).

We recommend using a Unix-based operating system (Mac OS, Linux) or Windows with a bash emulator for this exercise.
If you know neither ``git`` nor ``Python``, search online for some tutorial and absolve them.

## Getting Started

Open your command line terminal.
Check out the GitLab repository for this exercise:

```
git@git.cs.umu.se:tkampik/multi-armed-bandits.git
```

Install the dependencies of the exercise project:

```
cd multi-armed-bandits
pip install -r requirements.txt
```

Check out a new branch and name it after your CS IDs, for example like this:

```
checkout -b tkampik-jcnieves
```

Then, navigate into the ``multi-armed-bandits`` directory:

```
cd multi-armed-bandits
```

Open the project in your text editor or development environment.
Create a new folder in ``hand_in/``. Name it after your CS IDs, for example ``tkampik_jcnieves``:

```
cd hand_in
mkdir tkampik_jcnieves
```

Then, create a copy of the file ``hand_in/tkampik_jcnieves/test_tkampik_jcnieves_bandit.py`` and adjust the name of the copy to reflect your CS IDs.

**Important: Your file must start with ``test_``.**

Open the new file. You will see an implementation of a simple epsilon-greedy bandit.
Your task is to improve the bandit and so that you can beat the initial bandit's performance reliably.
Ten simulation runs with 10.000 "pulled arms" each should reduce the accumulated regret by factor X (to be determined).
To test your implementation, run ``pytest <your-file-name>``.
Replace ``<your-file-name>`` with the name you have given your file, of course.

## Report
Once you have achieved satisfactory performance, don't hesitate to improve further ;-), but more importantly, write a short report that describes:

1. how you proceeded;

2. what your results are;

3. how you could improve further.

The report should be approximately one page long; not much shorter, not much longer.

## Obfuscation
Because you will submit your code to be automatically tested on GitLab, you will need to obfuscate your results there, so others cannot copy from you.

In your directory run ``pyarmor obfuscate <your-file-name>``.
Replace ``<your-file-name>`` with the name you have given your file, of course.
Then create a copy of your file somewhere on your hard drive, **but not in the project folder**.
Later, you will need to submit this copy in [Labres](https://webapps.cs.umu.se/labresults/v2/handin.php?courseid=402), together with the small report.

## Hand-in
To hand in the exercise, first add, commit and push your changes (**don't forget to adjust the branch name in the example below**):

```
git add --all
git commit -m 'add custom multi-armed bandit implementation'
git push --set-upstream origin tkampik-jcnieves
git push
```
**Important: NEVER USE THE ``--force`` OPTION WHEN PUSHING A BRANCH!**

Then, go to ``https://git.cs.umu.se/tkampik/multi-armed-bandits/merge_requests`` and create a merge request for your branch.
Make sure all tests pass for your merge requests.
Then, add the link to your merge request to your report.
Hand-in the report and a copy of your code in [Labres](https://webapps.cs.umu.se/labresults/v2/handin.php?courseid=402).
