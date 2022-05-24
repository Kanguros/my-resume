import json

import yaml
from invoke import task


def p(s, prefix="|> "):
    print(f"{prefix}{s}")


def load_yaml(file):
    with open(file) as f:
        data = yaml.safe_load(f)
        return data


def save_json(data, file):
    with open(file, "w+") as f:
        json.dump(data, f)


@task
def parse_yaml(c):
    """Parse content of a resume from `resume.yaml` to `resume.json."""
    input_file = f"{c.filename}.yaml"
    input_path = f"{c.content_folder}\\{input_file}"

    p(f"Loading YAML file [{input_file}] data from folder [{input_path}]")
    data = load_yaml(input_path)
    p(f"Data loaded.")

    json_file = f"{c.filename}.json"
    p(f"Dumping to JSON as [{json_file}]")

    json_path = f"{c.content_folder}\\{json_file}"
    save_json(data, json_path)
    p(f"Data saved in [{json_path}]")


@task(parse_yaml)
def export(c):
    """Generate resume.html."""
    html_file = f"{c.filename}.html"
    resume_path = f"{c.content_folder}\\{c.filename}.json"
    theme = c.theme_folder
    p(f"Exporting [{resume_path}] with theme [{theme}] to [{html_file}]")

    cmd = f"resume export {html_file} --resume {resume_path} --theme {theme}"
    p(f"Executing command [{cmd}]")
    c.run(cmd)
