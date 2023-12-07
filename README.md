# Formal Languages

## Install setup

### Creating a Virtual Environment

1. Create a project directory.
2. Change into the project directory.
3. Run

```commandline 
cd my/project/files
python3 -m venv <name_of_virtualenv>
or
python -m venv <name_of_virtualenv>
```

##### Activate the environment

###### Linux:

```commandline
source venv/bin/activate
```

###### Windows:

```commandline
cd my/project/files/name_of_virtualenv/Scripts
activate
```

#### The python environment setup

```commandline
cd my/project/files
pip install -r requirements.txt 
```

Before running the app add input automata files into input_automata

#### Run the app

Activate environment before running

```commandline
python main.py in command line
F5 in main.py in vscode
Shift + F10 in main.py in pycharm
```