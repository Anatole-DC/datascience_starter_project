# Models app

Whenever you create a new model, you might want to keep track of the previous models you created. This module will store each individual model as a small python app.

Each model app will have the following architecture :

```bash
model_name/
├── cache           # Cache directory (containing your model backups)
├── README.md       # README file to document what changed about your model
└── main.py         # The main file containing the execution source code
```

To generate a model, run the following command :

```bash
make new-model MODEL_NAME="your_new_model_name"
```
