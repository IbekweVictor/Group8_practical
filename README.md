# 🛡️ OWASP ZAP Scan – Flask Integration

A Flask-based web application that integrates with **OWASP ZAP (Zed Attack Proxy)** to perform automated vulnerability scans on web applications.

This project demonstrates how to connect a Python Flask backend to the OWASP ZAP API to initiate scans, monitor progress, and retrieve security findings through a simple web interface.

---

## 📖 Overview

This application provides:

- A web interface to submit a target URL
- Automated Spider scanning
- Automated Active vulnerability scanning
- Retrieval and display of detected alerts
- Basic scan result presentation in the browser

It serves as a practical example of integrating Dynamic Application Security Testing (DAST) into a Python web application.

---

## 🔎 About OWASP ZAP

OWASP ZAP is an open-source web application security scanner maintained by the Open Worldwide Application Security Project (OWASP).

It is commonly used for:

- Automated vulnerability detection
- Web application penetration testing
- Security testing in CI/CD pipelines
- API security assessments

This project communicates with ZAP through its REST API using Python.

---

## 🏗️ Project Structure

# 🛡️ OWASP ZAP Scan – Flask Integration

A Flask-based web application that integrates with **OWASP ZAP (Zed Attack Proxy)** to perform automated vulnerability scans on web applications.

This project demonstrates how to connect a Python Flask backend to the OWASP ZAP API to initiate scans, monitor progress, and retrieve security findings through a simple web interface.

---

## 📖 Overview

This application provides:

- A web interface to submit a target URL
- Automated Spider scanning
- Automated Active vulnerability scanning
- Retrieval and display of detected alerts
- Basic scan result presentation in the browser

It serves as a practical example of integrating Dynamic Application Security Testing (DAST) into a Python web application.

---

## 🔎 About OWASP ZAP

OWASP ZAP is an open-source web application security scanner maintained by the Open Worldwide Application Security Project (OWASP).

It is commonly used for:

- Automated vulnerability detection
- Web application penetration testing
- Security testing in CI/CD pipelines
- API security assessments

This project communicates with ZAP through its REST API using Python.

---

## 🏗️ Project Structure

OwaspZap-Scan-/
│
├── app.py                # Main Flask application (ZAP integration logic)
├── templates/            # HTML templates
│   ├── index.html
│   ├── scan.html
│   └── results.html
│
├── static/               # CSS / frontend assets
├── OWASP_SCAN/           # Scan-related output directory
└── README.md

## ⚙️ How the Application Works

### 1. User Submits Target
The user enters a URL (e.g., `http://127.0.0.1:5000/`) in the web interface.

### 2. ZAP Spider Scan
The backend:
- Sends the target to OWASP ZAP
- Initiates a Spider scan to discover endpoints

### 3. Active Scan
After spidering:
- ZAP performs active vulnerability testing against discovered endpoints

### 4. Retrieve Alerts
Once scanning is complete:
- The application retrieves alerts from ZAP
- Displays vulnerability details on the results page

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8+
- pip
- OWASP ZAP installed locally OR running in Docker

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/IbekweVictor/OwaspZap-Scan-
cd OwaspZap-Scan-

---

### 2️⃣ Install Dependencies

```bash
pip install Flask python-owasp-zap-v2.4
```

Or, if available:

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Start OWASP ZAP

Run ZAP in daemon mode (Docker example):

```bash
docker run -u zap -p 8080:8080 owasp/zap2docker-stable zap.sh -daemon -port 8080 -host 0.0.0.0
```

Ensure the ZAP API is accessible at:

```
http://127.0.0.1:8080
```

---

### 4️⃣ Run the Flask Application

```bash
python app.py
```

Open in your browser:

```
http://127.0.0.1:5000/
```

---

## 📊 Example Scan Flow (Local Flask App)

To test the scanner:

1. Start OWASP ZAP.
2. Run the Flask app:

   ```
   http://127.0.0.1:5000/
   ```
3. Navigate to the scan page.
4. Enter:

   ```
   http://127.0.0.1:5000/
   ```
5. Start the scan.

The application will:

* Spider the local Flask app
* Perform active vulnerability tests
* Display detected alerts in the results page

---

## 🔍 Types of Vulnerabilities Detected

Depending on the target application, ZAP may detect:

* Cross-Site Scripting (XSS)
* SQL Injection
* Missing security headers
* Cookie security issues
* Server misconfigurations
* Insecure authentication patterns

---

## ⚠️ Security Notice

Only scan applications that you own or have explicit permission to test.

Unauthorized scanning of systems may be illegal.

---

## 🛠️ Limitations

* Requires OWASP ZAP to be running
* Scans are synchronous (may block while running)
* No persistent storage of scan history
* Basic UI implementation

---

## 🔮 Future Improvements

* Asynchronous/background scan processing
* Exportable HTML/JSON reports
* Authentication system
* Database integration
* CI/CD pipeline integration
* Dockerized full-stack deployment

---

## 👤 Author

Victor Ibekwe
GitHub: [https://github.com/IbekweVictor]


