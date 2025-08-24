# Code quality

Code quality ensures that you have consistent code between every developpers. They are mutliple tools for this.

## Formater

Formaters automatically format your code following rules that you have set. In python, a popular tool is [black](https://pypi.org/project/black/). You can run it like this.

```bash
black .
```

You can also use [editorconfig](https://editorconfig.org/), which is a tool that can be directly [integrated in vscode](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig). You need to use it with an config file. You can find a config file [here](https://github.com/Anatole-DC/datascience_starter_project/blob/master/.editorconfig).

## Linter

The linter is a tool that will enforce the rules. It returns an error for each rule not respected. In python, you can use [flake8](https://pypi.org/project/flake8/). It also needs a config file. You can find an exemple [here](https://github.com/Anatole-DC/datascience_starter_project/blob/master/.flake8). You can run the linter like this.

```bash
flake8
```

```{note}
Linter are typically used within [ci-cd pipelines]() to prevent code from beeing commited to the master branch without previous formatting.
```
