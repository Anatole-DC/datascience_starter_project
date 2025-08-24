# Git and github workflow

This section describes the workflow I follow when developping anything.

1. Create an issue on github
2. Create a branch on github and fetch it and check it out locally
3. Develop your feature
4. Push and create pull request
5. Once everything is done merge back to master

## Github issue

Github issues were initially created for user to signal issues that they had found using the project. But they can be used as feature ticket.

## Create a branch

On the newly created issue, there is a "Development" button. On it you will find a "create a branch" button under the form of a link. Create your branch from it using proper naming conventions.

On your computer, you can run the commands :

```bash
git fetch origin
git checkout your-new-branch
```

When following these steps, this allows other developpers to know on what you are working. If you had created the branch locally, they wouldn't be aware of what your are planning to work on.

## Start working on the feature

Write code, make commits.

## Create the pull request

```{note}
On the very first commit and push to github, you will be asked to create a new pull-request. I would advise to create the pull request right away, but you can wait until you want to merge your updates back to master.
```

Click on the "create pull request" button. Once it's created, you should see all the commits you have made listed.

```{admonition} Tips !
Your pull request should mention the issue you've created at the beggining under the "Development" section. If this is not the case, link it manually.

The reason we do this is because closing the pull request when merging will close the issue automatically, indicating to everyone working on the project that this feature is now implemented.
```

## Merge on master

If you don't have any conflicts, you should see a "Merge" button. When merging :
- If merging to another branch, use the normal merge
- If merging to a master branch, switch to "squash and merge"
