# Commits

Once you want to back up your code, start by adding the files to your commit.

Once you added your files (make sure that they are properly added by running `git status`), you can create your commit.

```bash
git commit -m "your commit title"

# Or

git commit -m "your commit title" -m "Your optionnal commmit description"
```

Same as branch, indicate the scope of your commit. If additional explaination are needed, don't forget about the commit description !

```bash
commit -m "feat(preproc): add new preprocessing function"

commit -m "doc(preproc): improve the preprocessing doc" -m "Added new preprocessing behavior in the documentation, and update old doc for CLI commands"
```

Limit the usage of `git add .`. Prefer using your code architecture to add features that are similar.

```bash
git add package/data/   # Will add all data related updates
```

If the updates are spreaded arround your projects, use vscode's source control to add files manually.
