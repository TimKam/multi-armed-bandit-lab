[![CircleCI](https://circleci.com/gh/TimKam/multi-armed-bandit-lab.svg?style=svg)](https://circleci.com/gh/TimKam/multi-armed-bandit-lab)

# AI Lab 3 Multi-Armed Bandits
Multi-armed bandits are a simple reinforcement learning method that forms the foundation of many large-scale recommender systems.

To get an overview of multi-armed bandits in their implementation take a look at:

* ["Towards Data Science" introduction to multi-armed bandits](https://towardsdatascience.com/solving-multiarmed-bandits-a-comparison-of-epsilon-greedy-and-thompson-sampling-d97167ca9a50)

* [Academic overview paper](https://arxiv.org/pdf/1402.6028)

## Task
In the lab, you will implement a multi-armed bandit to solve an example problem.
Your bandit will need to beat a “naïve” benchmark.
Also, we will determine the best-performing bandit of all submissions.

## Requirements
You need to have the following software installed and accounts set up to absolve this exercise:

* [Python 3.7.x or 3.8.x](https://www.python.org/);

* [git](https://git-scm.com/);

* A [GitHub](https://github.com/) account;

* A text editor or development environment like [Visual Studio Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/).

We recommend using a Unix-based operating system (Mac OS, Linux) or Windows with a bash emulator for this exercise.
If you don't know either ``git`` or ``Python``, search online for some tutorials and absolve them.

## Getting Started

Fork the GitHub repository we use for this exercise: [https://github.com/TimKam/multi-armed-bandit-lab](https://github.com/TimKam/multi-armed-bandit-lab).

Open your command line terminal.
Clone your fork.

```
git clone git@github.com:<your-GitHub-username>/multi-armed-bandit-lab.git
```

**Note:** Replace ``<your-GitHub-username>`` with your actual username.

Install the dependencies of the exercise project:

```
cd multi-armed-bandits
pip install -r requirements.txt
```

Check out a new branch and name it after your CS IDs:

```
checkout -b <CS-ID-1>-<CS-ID-2>
```

**Note:** Replace ``<CS-ID-1>-<CS-ID-2>`` with your actual CS IDs.

Then, navigate into the ``multi-armed-bandits`` directory:

```
cd multi-armed-bandits
```

Open the project in your text editor or development environment.
Create a new folder in ``hand_in/``. Name it after your CS IDs:

```
cd hand_in
mkdir <CS-ID-1>-<CS-ID-2>
```

Then, create a copy of the files ``hand_in/tkampik_jcnieves/bandit.py`` and ``hand_in/tkampik_jcnieves/test_runner.py`` and move them into your newly created folders.

**Important: Keep the names of the files as they are: ``bandit.py`` and ``test_runner.py``.**

Open your ``bandit.py`` file. You will see an implementation of a simple epsilon-greedy bandit.
Your task is to improve the bandit and so that you can beat the initial bandit's performance reliably.
Out of 20 simulation runs with 1.000 "pulled arms" each, your new bandit should outperform the reference bandit by at least 30% (30% more reward gained) in at least 17 runs.

To test your implementation, open your ``test_runner.py`` file.
Delete the line ``assert True`` (line 21) and remove the comment in front of the next line.
Then, run ``pytest`` in the repository's root directory.

## Report
Once you have achieved satisfactory performance, don't hesitate to improve further ;-), but more importantly, write a short report that describes:

1. how you proceeded;

2. what your results are;

3. how you could improve further.

The report should be approximately one page long; not much shorter, not much longer.

## Obfuscation
Because you will submit your code to be automatically tested on GitHub, you will need to obfuscate your results there, so others cannot copy from you.

1. In your directory, run the following command:

    ```
    pyarmor obfuscate --platform windows.x86_64 --platform linux.x86_64 --platform darwin.x86_64 bandit.py
    ```

2. Then, create a copy of your file somewhere on your hard drive, **but not in the project folder**.

3. Delete the ``bandit.py`` file in "your" folder in the git project.

4. To be able to run the tests, rename the ``dist`` directory the obfuscator has generated to ``test``.

5. To make the obfuscated code run on the continuous integration server, create a new directory in the ``test/pytransform/platforms/`` folder. Name this directory ``centos6`` and copy the folder ``x86_64`` from the ``test/pytransform/platforms/linux`` directory into the ``centos6`` directory.

6. Then, move the ``test_runner.py`` file to the ``test`` directory.

7. Run ``pytest`` in the project's root directory and make sure the tests pass.

Later, you will need to submit this copy in [Labres](https://webapps.cs.umu.se/labresults/v2/handin.php?courseid=402), together with the small report.

## Hand-in
To hand in the exercise, first add, commit and push your changes (**don't forget to adjust the branch name in the example below**):

```
git add --all
git commit -m 'add custom multi-armed bandit implementation'
git push --set-upstream origin <your-branch-name>
git push
```
**Important: NEVER USE THE ``--force`` OPTION WHEN PUSHING A BRANCH!**

Then, go to ``https://github.com/TimKam/multi-armed-bandit-lab/pulls`` and create a pull request for your branch.
Make sure all tests pass for your pull requests.
Then, add the link to your pull request to your report.
Hand-in the report and a copy of your code in [Labres](https://webapps.cs.umu.se/labresults/v2/handin.php?courseid=402).
