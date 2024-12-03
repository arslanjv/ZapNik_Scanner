# ZapNik Scanner

**ZapNik Scanner** is a Python-based web application designed to streamline vulnerability scaning and assessment and web application security testing by leveraging the powerful tools **Nikto** and **OWASP ZAP (Zaproxy)**. The tool provides a user-friendly, Flask-powered web interface for security professionals and analysts to conduct thorough scans of websites, detect vulnerabilities, and generate comprehensive reports.

---

## Key Features

### **Integration with Nikto**

- Perform server-side vulnerability scaning.
- Detect misconfigurations, outdated software, and other security risks.
- Fast and automated scan execution with detailed output on webpage with filtering.

### **Integration with OWASP ZAP**

- Conduct application security Scanning.
- Identify common vulnerabilities like SQL injection, XSS, and broken authentication.

### **Email Report Feature**

- After running a scan, **ZapNik** can automatically send the **`output.json`** file to a specified recipient via email if Configured in email_configuration.json.
- The scan results are sent as an email attachment, allowing for easy sharing of the report.

### **Flask-Powered Interface**

- Accessible through a web browser.
- Intuitive design for managing targets, initiating scans, and viewing results.

### **Reports**

- Generate reports in JSON format.
- Provide detailed findings with recommendations for remediation.

### **Cross-Platform Compatibility**

- Works on any linux platform that supports Python, Nikto, and OWASP ZAP(zaproxy).
- Easy setup and configuration for rapid deployment.

---

## How It Works

1. **Input Target**: Users provide a target URL or IP address through the web interface.
2. **Select Scan Options**:
   - Choose Default or Advance.
   - Configure advanced options such as **Tuning** for nikto and Active Scanning, **Alert Threshold**, **Spider Max Depth** and **Spider Max Duration (mins)** for zap.
3. **Run Scans**:
   - Click on Start Scan Button.
   - After scan completion shows result in well formated way on webpage.
   - Navigation between nikto and zap results with filtering.
4. **View Results**:
   - Examine detailed findings in the browser.
   - output.json is also generated.
5. **Send Email with Results**:
   - Once the scan is complete, an email with the **`output.json`** file is sent to the provided recipient address.

---

## Installation and Setup

1. **Clone the repository**:
   ```bash
   https://github.com/arslanjv/ZapNik_Scanner.git
   cd ZapNik_Scanner
   ```
2. **Install Python** (3.8 or later):
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
3. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Install Nikto**:
   ```bash
   sudo apt install nikto
   ```
6. **Install Nikto for Ubuntu/Mint**:
   ```bash
   wget https://github.com/sullo/nikto/archive/refs/tags/2.5.0.tar.gz
   tar -xvzf 2.5.0.tar.gz
   cd nikto-2.5.0/program
   ln -sf "$(pwd)/nikto.pl" /usr/local/bin/nikto
   chmod +x /usr/local/bin/nikto
   ```
7. **Install OWASP ZAP(Zaproxy)**:
   ```bash
   sudo apt install zaproxy
   ```
8. **Run the application**:
   ```bash
   sudo python app.py
   ```
9. **Access the web app**:
   Open a web browser and navigate to.
   ```bash
    http://127.0.0.1:3002.
   ```

---

---

## Contribution

Contributions are welcome! If you'd like to improve the tool or add features, feel free to submit a pull request.

### How to Contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make changes and commit them with a descriptive message.
4. Push your branch to your forked repository.
5. Submit a pull request with a description of your changes.

---

## License

This project is licensed under the [MIT License](../LICENSE).

---

## Acknowledgments

This project was developed to enhance web application security testing by integrating Nikto and OWASP ZAP. It is a collaborative effort to make security tools more accessible and easier to use for penetration testers, security analysts, and developers.

- [Muhammad Arsalan Javed](https://github.com/arslanjv)
- [Hafiz Mustafa Zain](https://github.com/mustafaazain)
- [Ahmed Tahir](https://github.com/CentricPants)
