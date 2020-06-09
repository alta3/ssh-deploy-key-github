# `ssh-deploy-key-github.py`

```
(venv) ubuntu@tmc:~/git/ssh-deploy-key-github$ python3 ssh-deploy-key-github.py -h

usage: ssh-deploy-key-github.py [-h] -i PUBLIC_KEY -r REPO [-u USER]

optional arguments:
  -h,            --help                 show this help message and exit
  -i PUBLIC_KEY, --pulic-key PUBLIC_KEY deploy this ssh public key FILE
  -r REPO,       --repo REPO            add ssh deploy key to this target github repo
  -u USER,       --user USER            target repos owner (org or user)

```

### Setup

```
./setup.sh
```

### TODO

- [ ] Add more docstrings
- [ ] Handle exceptions (see TODOs in code)
- [ ] Add logging of all actions completed or failed (stderr) 
- [ ] Document how-to: Install in a venv
- [ ] Document how-to: Do a no-impact test run (example usage)
- [ ] Document how-to: Run as an ansible module
