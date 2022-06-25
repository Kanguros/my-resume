import json
import os
import webbrowser

import pdfkit
import yaml
from invoke import task, Failure


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
def parse(c):
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


@task(parse)
def html(c):
    """Generate resume.html."""
    resume_path = f"{c.content_folder}\\{c.filename}.json"
    html_file = f"{c.content_folder}\\{c.filename}.html"

    p(f"Exporting [{resume_path}] with theme [{c.theme_folder}] to [{html_file}]")

    cmd = f"resume export {html_file} --resume {resume_path} --theme {c.theme_folder}"
    p(f"Executing command [{cmd}]")
    output = c.run(cmd)
    if output.stderr:
        raise Failure(f"FAILED. Export failed due to: {output['stderr']}")
    else:
        p(f"Resume exported as [{html_file}]")

    webbrowser.open_new_tab(os.path.abspath(html_file))


@task(html)
def pdf(c):
    PDF_OPTIONS = {
        'enable-local-file-access': True,
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8"
    }

    html_file = f"{c.content_folder}\\{c.filename}.html"
    pdf_file = f"{c.filename}.pdf"
    p(f"Exporting [{html_file}] to [{pdf_file}]")
    html_file = html_file.replace(r".\"", '')

    with open(html_file, 'r') as f:
        result = pdfkit.from_file(f, pdf_file,
                                  options=PDF_OPTIONS,
                                  verbose=True)

    if not result:
        raise Failure(f"FAILED. Export failed due to: {result}")
    else:
        p(f"Resume exported as [{pdf_file}]")
    #
    # pdfkit.from_url("https://google.com", pdf_file,
    #                  options=PDF_OPTIONS)
