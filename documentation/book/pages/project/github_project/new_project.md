# Create a new github project

When I create a new project, I follow these steps :
1. Create the project structure locally
2. Create the project on github
3. Add the github remote to the local repository
4. Push to github

## Create the project structure locally

Create the following files :
- A `.gitignore` file
- A `README.md` file
- Eventually your `.vscode` config

> You can also start working on your code right away before making your first commit. But it's better to keep track as soon as possible.

Once you are ready, you can run the following command at the root of your working directory.

```bash
git init
```

## Create the project on github

You can click on the [create a new repository](https://github.com/new) button. Enter the project informations, make sure all github suggested files are not added, we'll add them manually.

## Add the github remote to the local repository

On your project's landing page, click on the "<> Code" button, then copy the url in the "SSH" section.

> Since a couple of years, we can't use the http remote to edit the projects. Use the http remote when you only want to work on the project locally, as you won't be able to push your modifications to the remote.  
> If you want to backup a project where you don't have the write access, you can [fork the project](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).

In your local working directory, set the remote like this :

```bash
git remote add origin <your-remote-url>
```

## Push to github

You are now ready to make your first commit. You can use the following command to push your code.

```python
git add .
git commit -m "Initial commit"
git push origin master
```

```{admonition} Attention !
:style: danger

This should be the only time you push on master !
```
