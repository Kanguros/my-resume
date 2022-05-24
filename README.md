# My Resume

Repository with my CV and scripts to build it. 
To build nice, clean and simple CV `json-resume` is used. 
To simplify the generating process, Python's `invoke` is used.

### Prerequisites

- `poetry`
- `npm` - Installed along with `Node.js`. 


### Setup

```commandline
poetry install
npm install
```

### Files and folders

- `content` - Data for resume.
- `theme` - Theme for `jsonresume`. It is a copy/paste of default one. 
- `invoke.yaml`, `tasks.py` - Tasks and config for `invoke`.

## Usage

```commandline
 resume export resume.html --theme .\theme_even\
```