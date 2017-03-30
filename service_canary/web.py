from flask import Flask, make_response, jsonify

from .args import config
from .app import run_checks

app = Flask("service_canary")

@app.route('/')
def test_root():
    result = run_checks(config)
    out = "canary test results:\n"
    for key, val in result.items():
        out += "{}:\t{}\n".format(key, "PASS" if val else "FAIL")
    return make_response(out)

@app.route('/json')
def test_json():
    return jsonify(run_checks(config))
