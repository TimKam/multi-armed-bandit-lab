# AI Lab 2 Multi-Armed Bandits
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
pip install -r requirements.txt
```

Check out a new branch and name it after your Umeå University ID, for example like this:

```
checkout -b tika0026
```

Then, navigate into the ``multi-armed-bandits`` directory:

```
cd multi-armed-bandits
```

Open the project in your text editor or development environment.
Then, create a copy of the file ``hand_in/tika0026_bandit.py`` and adjust the name of the copy to reflect your Umeå University ID.

Open the new file. You will see an implementation of a simple epsilon-greedy bandit.
Your task is to improve the bandit and so that you can beat its performance reliably.
Ten simulation runs with 10.000 "pulled arms" each should reduce the accumulated regret by factor X (to be determined).

## Hand-in
To hand in the exercise, first add, commit and push your changes:

```
git add --all
git commit -m 'add custom multi-armed bandit implementation'
git push
```

Then, go to ``https://git.cs.umu.se/tkampik/multi-armed-bandits/merge_requests`` and create a merge request for your branch.
