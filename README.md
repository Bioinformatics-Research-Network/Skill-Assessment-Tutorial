# Skill-Assessment-Tutorial (Python) <img src="https://api.badgr.io/public/badges/MMuVRwluTd6cI33-0ILs3w/image" align="right" alt="logo" width="240" style = "border: none; float: right;">

![](https://img.shields.io/static/v1?label=Version&message=0.0.2a&color=blue)
![](https://img.shields.io/static/v1?label=Lifecycle&message=experimental&color=red)


Hello and welcome to the BRN Skill Assessment tutorial 👋!

My name is **BRN bot** and I will help you get started today (\*\*beep boop\*\* 🤖).

Let's dive in so you can earn your first Skill Assessment badge 🏆.

## Instructions

Every BRN Skill Assessment contains **Instructions** which provide the following information:

1. **Requirements** (the requirements for successful completion of the assessment)
2. **Guidance** (additional instructions and hints to aide you in this task)

If you are ready to dive in, jump to the [Requiments](#requirements) section next. 

Or stop and check out this additional information about BRN Skill Assessments:


<details>
<summary>Assessment metadata</summary>

<hr>

Each Skill Assessment also contains **metadata**, in the form of badges like these:

![](https://img.shields.io/static/v1?label=Version&message=0.0.2a&color=blue)
![](https://img.shields.io/static/v1?label=Lifecycle&message=experimental&color=red)

These badges indicate the **version** of the skill assessment you are completing. The badge you earn will be tied to the version of the skill assessment you completed.

The metadata also indicates the skill assessment **lifecycle**. For "experimental" assessments, you might encounter bugs, unclear instructions, or both. "Stable" skill assessmens should have few bugs or errors. "Superceded" skill assessments have been replaced by a newer skill assessment. "Deprecated" means that the skill assessment is no longer valid and has not been replaced.

<hr>


</details>

<details>
<summary>Getting help</summary>

<hr>

If you find a bug or get confused, please don't hesitate to contact the BRN Skill Assessment maintainers on the **#skill-assessment-help** Slack channel, and they will assist you. 

<hr>

</details>

<details>
<summary>Privacy, Code of Conduct, and Academic Honesty</summary>

<hr>

BRN has several policies which apply to Skill Assessments. During the sign up process, you agreed to each. Here, I will recap their main points:

1. **Privacy Policy**
    - The [Privacy Policy](https://www.privacypolicies.com/live/bb7b8b6b-32e1-45c1-be17-814529aeb5cb) gives you the right to request access to all of your data from BRN and for us to delete all your data. You can request either at any time by emailing privacy@bioresnet.org.
2. **Code of Conduct**
    - BRN is dedicated to maintaining appropriate conduct standards throughout its online and in-person spaces. The [Code of Conduct](https://docs.google.com/document/d/1q06RJbIsyIzLC828A7rBEhtfkujkj9kx7Y118AaWASA/edit) is the policy which governs acceptable behavior. It forbids discrimination, harassment, and other types of inappropriate conduct. 
    - While this tutorial will not involve interacting with human reviewers, subsequent assessments will -- so please be mindful of your behavior during those exchanges as well as the behavior of the reviewers. 
    - If you observe violations of this policy, you are encouraged to contact codeofconduct@bioresnet.org. 
3. **Academic Honesty**
    - BRN strictly enforces policies that discourage cheating, fraud, and plagiarism in its [Academic Honesty Policy](https://docs.google.com/document/d/1-Xoko7VDr0lK7olboGQ2CPmEnUTV3WmiDxwQQuGBgiQ/edit). Because these skill assessments certify individual capability in bioinformatics, cheating and plagiarism guidelines are stricly enforced. 
    - The most common way for **cheating** to arise is when you share (or recieve) Skill Assessment code or answers from another BRN member. Therefore, we expressly forbid sharing code or discussing Skill Assessments with anyone who is not a member of the BRN Skill Assessment working group or BRN leadership team. 
    - The most common way for **plagiarism** to arise is when a trainee copies code from other sources on the internet and does not appropriately attribute it. Copying code (with or without modification) from sources like Stack Overflow is fine as long as the source of that code is mentioned. For example:

```python
# This function copied from: https://www.stackoverflow.com/url_link
def function_from_stack_overflow(params):
    function code...

# This function adapted from: https://www.stackoverflow.com/url_link2
def function_adapted_from_stack_overflow(params):
    function code...
```

<hr>

</details>

## Requirements

This Skill Assessment will require you to write a **script**, `main.py`, which contains a **function** called `hello()` that returns the phrase `"Hello, world!"`.

Therefore, the **requirements for success** in the assessment are:

1. Write a script, `main.py`
2. Create a function `hello()` in `main.py`.
3. `hello()` should `return "Hello, world!"`. 
4. The repository must pass the automated checks (learn about these checks [here](#completing-the-assessment))

Based on the requirements, users should be able to import your script and run `hello` via the following commands:

```py
import main

print(main.hello())  # Says "Hello, world!"
```


## Guidance

### The BRN Skill Assessment Interface

Since I am helping you with this skill assessment, we will need a way to talk to eachother 💬. Fortunately, GitHub provides **Pull Requests** which will allow us to communicate. **Navigate** to the "Pull requests" tab and click the one called "Feedback". You should see a welcome message from me 🤖.

Using the pull request comments, you can issue **bot commands** which perform various tasks. The welcome message lists the ones that are available to you in this skill assessment. 

For example, issue the "hello" command by **posting this comment**:

```
@brnbot hello
```

Then I will reply:

```
Hello, @<your_username>! 😊
```

You will need to use bot commands to complete the assignment, so get used to typing "`@brnbot <command>`" in the pull request.

### Completing the assessment

Since this is your first time, I've gone ahead and completed [Requirements](#requirements) 1-3 for you 😊. But even I make mistakes sometimes 🤖... so, you may want to **check my code for errors** 🔍.

You can view and edit the code using any of the following options:


<details>
<summary>Code editing options</summary>

<hr>

1. [Clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to your local computer, and then open the code in your favorite editor (e.g., VS Code, Atom, PyCharm, etc). Once you are happy with your changes, use git to `add` your changes, `commit` them, and then `push` them back to this GitHub repo. (**Recommended approach**)
2. Edit the code in your browser by pressing the "." key to open an in-browser VS Code session. Commit your changes using the built-in version control panel.
3. You can also simply navigate to the file you want to modify in the GitHub repo and click the edit icon to add your changes and commit them directly.
4. Request access to the BRN Orchestra server (contains Jupyter Notebook, VS Code, and RStudio IDEs) by contacting training@bioresnet.org. Once granted, you will be able to open the repo in your own server sessions and `add`, `commit`, and `push` it back to GitHub.

<hr>

</details>

Once you push your changes back to the GitHub repo, **run the checks** to see if your code works correctly. You can run checks by issuing this bot command:

```
@brnbot check
```

I will see this comment and run the checks for you. You can monitor the progress of the checks in the "Actions" panel and see the results there. Once the checks are done, I will write a comment and I will tell you whether they passed or failed. If they failed, examine the log in the "Actions" tab to see what went wrong. Then update your code accordingly and rerun the checks. 

<details>
<summary>Check details</summary>

<hr>

The automated checks are run with [GitHub Actions](https://docs.github.com/en/actions) using the workflow defined in `.github/workflows/tests.yml` within this repo. 

When trigger, GitHub actions creates a new computing environment using the details in `tests.yml`. For this assessment, the environment contains python `v3.10` and the `pytest` package. That is defined in this part of the file:

```yml
- uses: actions/setup-python@v3
  with:
    python-version: '3.10'
- name: Install pytest
  run: pip install pytest
```

The repo code is then tested in the last part of the workflow:

```yml
- name: Test with pytest
  run: |
    pytest
```

The `pytest` command finds all the tests in the `tests/` folder and then executes them.

For this skill assessment, there is only one test in `tests/test_main.py`:

```python
import main

def test_hello():
    assert main.hello() == "Hello, world!"
```

This test simply imports the `main.py` script and then executes the `hello()` function. It then uses the `assert` statement to ensure that the output matches the expected value: "`Hello, world!`". If it does not, then the test will fail.

To complete a BRN Skill Assessment, **all tests** have to pass successfully.

Finally, it can be inconvenient to push your code to GitHub every time you want to run `pytest`. Fortunately, you can run tests locally by opening the terminal (MacOS/Linux) or command prompt (Windows), installing pytest, and then running pytest:


```bash
# Install pytest
pip install pytest

# Run pytest
pytest
```

**A note about academic honesty and tests**:

The `tests/` folder contains the "correct answers" to these Skill Assessments. Therefore, it is possible to ignore the assignment prompt and write your code to exactly match the outputs that the tests expect. While this might work for assessments which have no reviewers, it is still dishonest and may lead to your account being **suspended** and badges **revoked**.

<hr>

</details>

Once you pass the checks, I will issue your badge 🏆 and archive the repo. You will get an email with the link to your badge and it will also appear in your profile on the BRN Skill Assessment web platform 🔥.

### External resources

For a tutorial on how to use **git and GitHub**, check out these resources:
1. Written tutorials: [GitHub official tutorial](https://docs.github.com/en/get-started/quickstart), [freecodecamp.org](https://www.freecodecamp.org/news/git-and-github-for-beginners/), [analyticsvidhya](https://www.analyticsvidhya.com/blog/2021/09/git-and-github-tutorial-for-beginners/)
2. YouTube tutorials: [Tech with Tim](https://www.youtube.com/watch?v=DVRQoVRzMIY), [freecodecamp.org](https://www.youtube.com/watch?v=RGOj5yH7evk), [Amigoscode](https://www.youtube.com/watch?v=3fUbBnN_H2c)


For basic **python programming**, check out these resources:

1. Written tutorials: [learnpython.org](https://www.learnpython.org/), [W3 schools](https://www.w3schools.com/python/), 
2. YouTube tutorials: [freecodecamp](https://www.youtube.com/watch?v=rfscVS0vtbw), [Programming with Mosh](https://www.youtube.com/watch?v=_uQrJ0TkZlc), [Cory Schafer](https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
3. MOOCs: [EdX](https://www.edx.org/professional-certificate/introduction-to-python-programming), [Coursera](https://www.coursera.org/specializations/python)
4. Online learning platforms: [codecademy](https://www.codecademy.com/learn/learn-python-3), [DataCamp](https://www.datacamp.com/learn/python)


For learning how to use **`pytest`**, check out these resources:

1. Written: [Official pytest docs](https://pytest.org/), [real python](https://realpython.com/pytest-python-testing/)
2. YouTube: [edureka!](https://www.youtube.com/watch?v=byaxg00Gf9I)
