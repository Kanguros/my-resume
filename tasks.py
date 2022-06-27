import logging
import os

import yaml
from invoke import task
from jinja2 import Environment, FileSystemLoader, Template

logging.basicConfig(level="INFO", format='%(levelname)-8s| %(message)s')

logger = logging.getLogger(__name__)


def load_yaml(filepath) -> dict:
    logger.debug(f"Loading YAML from file [{filepath}]")
    with open(filepath, mode="r") as f:
        yaml_data = yaml.safe_load(f)
        logger.debug(f"Data from YAML [{filepath}] loaded.")
    return yaml_data


def load_jinja(folder, main_file) -> Template:
    logger.debug(f"Setting up Jinja Environment in path [{folder}]")
    env = Environment(
        loader=FileSystemLoader(folder))
    logger.debug(f"Setting Jinja Template as [{main_file}]")
    template = env.get_template(main_file)
    logger.debug(f"Jinja Template set")
    return template


def save_html(data, filepath) -> str:
    logger.debug(f"Saving data [ID:{id(data)}] to HTML file [{filepath}]")
    filepath = filepath \
        if filepath.endswith('html') \
        else f"{filepath}.html"
    with open(filepath, mode="w+") as f:
        f.writelines(data)
    logger.debug(f"Data [{filepath}] saved.")
    return filepath


def get_template(path):
    logger.debug(f"Loading Jinja template from path [{path}]")
    folder = os.path.dirname(path)
    main_file = os.path.basename(path)
    return load_jinja(folder, main_file)


INPUT_DATA = "./data.yaml"
TEMPLATE = "./resume/template/base.html"
OUTPUT = "./resume/resume.html"


@task
def html(c):
    """Generate resume.html."""

    logger.info(f"Loading input data...")
    data = load_yaml(INPUT_DATA)

    logger.info(f"Getting template...")
    template = get_template(TEMPLATE)

    logger.info(f"Rendering HTML file...")
    render = template.render(data)

    logger.info(f"Page rendered. Saving...")
    save_html(render, OUTPUT)
    logger.info(f"Page available at {OUTPUT}")



    # def _consolidate(self, path):
    #     soup = bs4.BeautifulSoup(open(path).read(),
    #                              features="html.parser")
    #     stylesheets = soup.findAll("link",
    #                                {"rel": "stylesheet"})
    #     for style in stylesheets:
    #         style_path = os.path.join(os.path.dirname(path),
    #                                   str(style["href"]).replace('./', ''))
    #         style_data = bs4.element.NavigableString(open(style_path).read())
    #         tag_style = soup.new_tag('style')
    #         tag_style.insert(0, style_data)
    #         tag_style['type'] = 'text/css'
    #         style.replaceWith(tag_style)
    #     open(path, "w").write(str(soup))
