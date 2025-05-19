import os
import importlib.util
from flask import Flask, Blueprint

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

# Dynamically load and register blueprints from the api_blueprints directory
blueprint_dir = os.path.join(os.path.dirname(__file__), 'api_blueprints')
for filename in os.listdir(blueprint_dir):
    if filename.endswith('.py'):
        module_name = filename[:-3]  # Remove the .py extension
        filepath = os.path.join(blueprint_dir, filename)

        spec = importlib.util.spec_from_file_location(module_name, filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isinstance(attribute, Blueprint):
                app.register_blueprint(attribute)