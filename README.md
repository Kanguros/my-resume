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
- `invoke.yaml`, `tasks.py` - Config and Tasks for `invoke`.


### Export to PDF

In order to export resume to PDF format, `s` is needed.

1. Install
```commandline
$wkh_url = "https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.msvc2015-win64.exe"
$fn = "wkh.exe"

Invoke-WebRequest -Uri $wkh -OutFile $fn
Invoke-Item $fn
```

3. Add `` binary folder path to system's `PATH`. By default, it is located in `C:\Program Files\wkhtmltopdf\bin`
Open cmd or PowerShell as Administrator and paste:
```commandline
setx /M path "%path%;C:\Program Files\wkhtmltopdf\bin"
```

## Usage

```commandline
invoke 
```

## Development



```commandline
 resume export resume.html --theme .\theme_even\
```