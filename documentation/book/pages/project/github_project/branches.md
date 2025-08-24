# Branches

First check on which branch you are.

```bash
git branch
```

If you are on master (main), it's a good practice to pull the modifications from github.

```bash
git pull
```

> By pulling before working, you ensure to work on the latest version of the branch.

Then you can checkout on the branch you want to work on. Whenever your start working on something new (new feature, bug fixing), **<u>you MUST navigate to a branch</u> that is not master**  !!!

```bash
# To navigate to an existing branch
git checkout "your-branch-name"

# To create a new branch
git checkout -b "your-branch-name"
```

Your branch name should explain most of the work you are planning to do. Examples :

```bash
feature/implement-data-preprocessing
fix/solve-wrong-numbers-of-units-in-lstm
doc/add-deployement-documentation
refactoring/clean-data-processing-function
