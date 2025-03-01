# Git and Github workflow

This document gives a general example on how to collaborate on code with git and github.

## Create github repo

You can follow [this tutorial](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories) to create your repository on github.

## Start developping locally

Start by [cloning the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

**Make sure to clone in ssh mode and not in https !**

### Branches

First check on which branch you are.

```bash
git branch
```

If you are on master (main), it's a good practice to pull the modifications from github.

```bash
git pull
```

> By pulling before working, you ensure to work on the latest version of the branch.

Then you can checkout on the branch you want to work on. Whenever your start working on something new (new feature, bug fixing), **<u>you MUST navigate to a branch</u> that is not master (main)**  !!!

```bash
# To navigate to an existing branch
git checkout "your-branch-name"

# To create a new branch
git checkout -b "your-branch-name"
```

See [this document](best_practices.md#branches) on how to properly name your branches.

### Commits

Once you want to back up your code, start by adding the files to your commit. See [this best practice](best_practices.md#commit-content) on how to properly add files to your commits.

Once you added your files (make sure that they are properly added by running `git status`), you can create your commit.

```bash
git commit -m "your commit title"

# Or

git commit -m "your commit title" -m "Your optionnal commmit description"
```

See [this document](best_practices#commit) on commit title best practices.

### Push to github

Once your commit is ready, you can push it to github.

```bash
git push
```

> If you created your branch locally, you are going to get an error.  
> It will give you a suggestion that you can copy paste.  
> `git push --set-upstream origin "your-branch-name"  
> This is because github does not know your branch name yet, so this command indicates what branch name to use.

When you navigate to your project github page, you are going to see a warning asking you if you want to create a "Pull Request".  You can follow [this tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request#creating-the-pull-request) to understand how to proceed with pull requests.

From now on, all your commits will be added to this pull requests.

## Merge on master

Once your work is done, you can merge your pull request into your master (main) branch. See [this tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request#merging-a-pull-request) to learn how to perform a merge.

> My advice is the following :  
> Use "Create a merge commit" for branch to branch merge
> Use "Squash and merge" for branch to master (main) branch

## Ideal best practice

This section describes the "ideal" best practices on how to collaborate on code.

### Start with an issue

When you identify a feature, a bug, or anything that requires changes in the code, submit an issue on the github project. See [this tutorial](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) on how to create an issue.

The advantages of issues is that they can used in github project's to track the progression.

### Create a branch from the issue

You can then create a branch from the issue you've created. See [this tutorial](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue) for further explainations.

### Fetch the branch

On you local repository, you can run `git fetch origin master` or `git pull` to get this newly created branch. You can then checkout without `-b` option, as the branch already exists.

Follow the beginning of this document on how to work locally.

### Advantages

The main benefits of this technic, in addition to task decomposition and tracking, is that whenever you merge your pull requests, the issues will be closed, allowing for automatic progress tracking on your project.