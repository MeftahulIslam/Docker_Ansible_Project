import os
from flask import Flask, render_template

import pulumi.automation as auto
import mysql.connector



def ensure_plugins():
    ws = auto.LocalWorkspace()
    ws.install_plugin("aws", "v4.0.0")

ensure_plugins()
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY="misf",
    PROJECT_NAME="misf",
    PULUMI_ORG=os.environ.get("PULUMI_ORG"),
)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


import sites

app.register_blueprint(sites.bp)

import virtual_machines

app.register_blueprint(virtual_machines.bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)