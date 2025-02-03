# 📌 Test Automation Project

## 📖 Overview

This repository contains test automation implementations for multiple tasks, including UI Testing, API Testing (REST & SOAP), and Test Case Preparation. The tasks cover functional and non-functional testing, automated UI tests using Selenium, API testing using Postman and SoapUI, and database structure illustrations.

## 🏆 Tasks Completed

### **✅ Task 1: Testcase Preparation**

- **Functional Test Scenario:**
  - Google account signup process.
  - Detailed test steps defined.
- **Non-Functional Test Scenarios:**
  - Performance Testing
  - Security Testing
  - Usability Testing

### **✅ Task 2: HTTP REST Service Test**

- Created **Postman Collection** covering all HTTP methods for `/post` endpoint at `https://jsonplaceholder.typicode.com`.
- Illustrated **database table structures** for `post`, `comment`, and `user` (ERD diagram).
- **Bonus:** Created **Postman Collection Runner** with a dataset for bulk testing.

### **✅ Task 3: HTTP SOAP Service Test**

- Created a **SoapUI project** for `https://www.crcind.com/csp/samples/SOAP.Demo.cls`.
- Covered all operations (requests + responses).
- **Bonus:** Added **Test Suite with Load Testing** in SoapUI for a single operation.

### **✅ Task 4: UI Testing with Selenium**

- Developed a **Selenium WebDriver test script** to:
  - Open `https://academy.eteration.com/`.
  - Click on **Instructors** page (`https://academy.eteration.com/instructors`).
  - Verify that the instructor list is **not empty** and has exactly **8 instructors**.
- **Bonus:** Used **Selenium IDE** to record and automate the "SUBSCRIBE TO NEWSLETTER" scenario.

## 🚀 Setup & Execution

### **🔹 Prerequisites**

Ensure the following tools are installed:

- **Postman** (for REST API testing) - [Download](https://www.postman.com/downloads/)
- **SoapUI** (for SOAP API testing) - [Download](https://www.soapui.org/downloads/)
- **Selenium WebDriver** with:
  - Python/Java (based on implementation)
  - ChromeDriver (ensure it's in the system path)
  - `pip install selenium` (for Python users)

### **🔹 Running Tests**

#### 1️⃣ **Selenium UI Tests**

```bash
python test_eteration_academy.py  # Run Selenium WebDriver tests
```

#### 2️⃣ **Postman API Tests**

- Open Postman and import the provided collection.
- Click **Run Collection** to execute tests.

#### 3️⃣ **SoapUI Tests**

- Open SoapUI.
- Load the provided project.
- Run test cases under the Test Suite.

## 📜 License

This project is open-source and free to use.

## 👨‍💻 Author

**Ramadan Cesur**

---
