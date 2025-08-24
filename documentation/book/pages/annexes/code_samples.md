# Useful code samples

This section was made to provide you some code samples that I always find myself using in my projects.

## Multi-threaded action

In projects, you can often have functions that have the multiple identical tasks to run, that can potentially run for a long time. In this case you want to use two things :
- A way of displaying the progress
- A way of running tasks in parallel

```python
from multiprocessing.pool import ThreadPool

from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
)

from package import your_long_function

with Progress(
        TextColumn("Your long task"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:

        progress_task = progress.add_task("", total=len(stuff_to_process))

        def task(arg):
            your_long_function(...)

            progress.update(
                progress_task, advance=1, description=f"Processing {arg}"
            )
            return result

        with ThreadPool(processes=NUMBER_OF_THREADS) as pool:
            all_tasks_results = pool.starmap(
                task, [(arg,) for arg in stuff_to_process]
            )
```
