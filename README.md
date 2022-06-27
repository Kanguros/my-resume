# My Resume

Repository with my CV and scripts to build it.
To simplify the generating process, Python's libraries `jinja` and `invoke` are used.

### Setup

- `poetry install`

### Files and folders

- `notes` - My more-or-less raw notes.
- `resume` - Folder for theme and its assets.
- `tasks.py` - `invoke` task's.


## Usage

```commandline
invoke html
```

Create HTML single page, prepared to be print to PDF. 