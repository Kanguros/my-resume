


DATA_FILE = "data.yaml"
TEMPLATE_FILE = "resume.j2"

def _get_data():
    """ Load the data from the YAML file """
    with open(DATA_FILE, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def _get_template():
  	""" Retrieve the template """
    template_loader = jinja2.FileSystemLoader(searchpath="templates")
    template_env = jinja2.Environment(loader=template_loader)
    return template_env.get_template(TEMPLATE_FILE)

if __name__ == '__main__':
    # Loads YAML file
    data = _get_data()
    # Loads HTML file
    template = _get_template()
    # Fills in the variables in the HTML file
    output_text = template.render(**data)