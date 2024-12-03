import os
import subprocess
import json
from email_script import send_email 


def load_email_config():
    try:
        # Load email configuration from the JSON file
        with open("email_config.json", "r") as config_file:
            email_config = json.load(config_file)
        return email_config
    except Exception as e:
        print(f"Error loading email configuration: {e}")
        return None


def run_nikto(target_url, output_file, tuning_options=""):
    try:
        print("[*] Running Nikto Scan...")
        nikto_command = ['nikto', '-h', target_url, '-o', output_file, '-Format', 'json']
        if tuning_options:
            nikto_command += ['-Tuning', tuning_options]
        print("command = ", nikto_command)
        subprocess.run(nikto_command, check=False)
        print("[+] Nikto scan completed.")

        with open(output_file, "r") as nikto_file:
            nikto_results = json.load(nikto_file)
        return nikto_results
    except Exception as e:
        print(f"Error during Nikto scan: {e}")
        return {"error": str(e)}

def run_owasp_zap(target_url, output_file, zap_config=None):
    try:
        print("[*] Running OWASP ZAP Scan...")
        zap_command = f"sudo zaproxy -cmd -quickurl {target_url} -quickprogress -quickout {output_file}"
        if zap_config:
            for config in zap_config:
                zap_command += f" -config {config}"
        print("command= ", zap_command)
        subprocess.run(zap_command, shell=True, check=True)

        # Check if output file exists
        if not os.path.exists(output_file):
            raise FileNotFoundError(f"OWASP ZAP output file not created: {output_file}")

        with open(output_file, "r") as zap_file:
            zap_results = json.load(zap_file)
        return zap_results
    except FileNotFoundError as fnf_error:
        print(f"Error during OWASP ZAP scan: {fnf_error}")
        return {"error": str(fnf_error)}
    except Exception as e:
        print(f"Error during OWASP ZAP scan: {e}")
        return {"error": str(e)}


def main():
    # Read configuration from JSON or prompt user
    target_url = input("Enter the target URL: ").strip()
    include_email = input("Do you want to receive an email after the scan? (yes/no): ").strip().lower() == "yes"

    email_config = load_email_config() if include_email else None

    # Initialize results
    results = {}

    # Run Nikto

    #print(os.environ)
    nikto_output_path = os.path.join(os.getcwd(), "nikto_output.json")
    results["nikto"] = run_nikto(target_url, nikto_output_path)

    # Run OWASP ZAP
    zap_output_path = os.path.join(os.getcwd(), "zap_output.json")
    results["owasp_zap"] = run_owasp_zap(target_url, zap_output_path)

    # Save results to output.json
    output_file = "output.json"
    with open(output_file, "w") as json_file:
        json.dump(results, json_file, indent=4)
    print(f"[+] Results saved to {output_file}")

    # Send email if opted
    if include_email and email_config:
        send_email(email_config, output_file)


if __name__ == "__main__":
    main()
