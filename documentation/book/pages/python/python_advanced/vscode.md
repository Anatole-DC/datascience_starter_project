# Configure vscode properly

When you work on your code, it's essential that your tools are well configured for the current project.

## Extensions

Vscode works with extensions, and you can specify them for each project so that other developpers can easily configure their code editor. You specify extensions within the [.vscode/extensions.json](https://github.com/Anatole-DC/datascience_starter_project/blob/master/.vscode/extensions.json) file.

## Debug and launch

If you think print debug is better, it is probably because you have not used the full potential of the debugger. To configure it, create a [.vscode/launch.json](https://github.com/Anatole-DC/datascience_starter_project/blob/master/.vscode/launch.json) file.

### Breakpoint

When a code hit a breakpoint, it means the previous code was working. If you need to log a value, you can simply type its name in the debug console.

### Other types of breakpoint

You can add these types of breakpoint as well :
- Conditionnal breakpoint, triggered when the condition is true. Useful when you want to trigger a breakpoint according to a certain state, for instance when a variable reach a value it should not reach.
- Trigger breakpoint, when triggered when another breakpoint elsewhere is triggered.
- Log point, yes is allows you to log debug, but here you can add them dynamically without having to stop, edit and restart your code.

## Tests

You can run your test from your editor, which is easier when you want to trigger specific tests. [Here is a config file](https://github.com/Anatole-DC/datascience_starter_project/blob/master/.vscode/settings.json) to configure vscode and pytest.

```{admonition} Extra feature !
The config file also allows you to hide the `__pycache__/` directories. This makes your coding environment a bit cleaner in my opinion.
```
