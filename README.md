# My Resume

Repository with my CV and scripts to build it.
To simplify the generating process, Python's libraries `jinja` and `invoke` are used.

### Setup

- `poetry install`

### Files and folders

- `notes` - My more-or-less raw notes.
- `resume` - Theme for `jsonresume`. It is a copy/paste of default one. 
- `tasks.py` - 'invoke' task's.


## Usage

```commandline
invoke html
```

## Development



```commandline
 resume export resume.html --theme .\theme_even\
```