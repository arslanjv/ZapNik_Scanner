from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
import subprocess
import os
import json
from scan import run_nikto, run_owasp_zap
from email_script import send_email

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        target_url = request.form.get("target_url").strip()
        if not target_url.startswith(("http://", "https://")):
            target_url = f"http://{target_url}"

        send_email_option = request.form.get("send_email") == "on"
        nikto_tuning = request.form.get("nikto_tuning", "")
        zap_options = [
    	    request.form.get("zap_scanning"),
    	    request.form.get("zap_alert"),
    	    request.form.get("zap_depth"),
    	    request.form.get("zap_duration"),
	]
        zap_options = [opt for opt in zap_options if opt]  # Remove empty options


        nikto_output = os.path.join(os.getcwd(), "nikto_output.json")
        zap_output = os.path.join(os.getcwd(), "zap_output.json")
        results = {}

        results["nikto"] = run_nikto(target_url, nikto_output, nikto_tuning)
        results["owasp_zap"] = run_owasp_zap(target_url, zap_output, zap_options)

        output_file = os.path.join(os.getcwd(), "output.json")
        with open(output_file, "w") as file:
            json.dump(results, file, indent=4)

        if send_email_option:
            email_config = load_email_config()
            if email_config:
                send_email(email_config, output_file)

        return redirect(url_for("result"))

    return render_template("main.html")





@app.route("/results")
def result():
    try:
        with open("output.json", "r") as output_file:
            results = json.load(output_file)
        return render_template("result.html", results=results)
    except FileNotFoundError:
        return "Error: No results found. Please perform a scan first."

@app.route('/get-output')
def get_output():
    directory = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(directory, 'output.json')

def load_email_config():
    try:
        with open("email_config.json", "r") as config_file:
            return json.load(config_file)
    except Exception as e:
        print(f"Error loading email configuration: {e}")
        return None

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3002,debug=False)
