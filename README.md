# 🚀 AutoTest360 – End-to-End Automation Framework for E-Commerce Web App

AutoTest360 is a complete *end-to-end automation testing framework* built using *Selenium, **PyTest, and **Python. This framework automates UI testing scenarios such as **user login, **product search, and **adding to cart* on the live website [AutomationExercise](https://automationexercise.com).

---

## 📌 Key Features

- ✅ Page Object Model (POM) architecture
- ✅ PyTest-based test suite with fixtures
- ✅ HTML test reports with pytest-html
- ✅ Logging using custom utility
- ✅ Clean modular structure (tests/pages/utils)
- ✅ Easily scalable and maintainable

---

## 🧱 Folder Structure

AutoTest360/
├── tests/ # Test scripts
│ ├── test_login.py
│ ├── test_search.py
│ └── test_cart.py
├── pages/ # Page Object classes
│ ├── login_page.py
│ ├── search_page.py
│ └── cart_page.py
├── utils/ # Configuration and logging
│ ├── config.py
│ └── logger.py
├── reports/ # HTML test reports (auto-generated)
├── requirements.txt # Python dependencies
├── pytest.ini # PyTest configuration
└── README.md # Project documentation



---

## ⚙ Technologies Used

- Python 🐍
- Selenium WebDriver
- PyTest
- HTML Reporting (pytest-html)
- ChromeDriver
- Page Object Model (POM)

---

## 🚀 How to Run the Project

### 1️⃣ Install Python Packages

```bash
pip install -r requirements.txt


 Update Login Credentials
Open utils/config.py and replace:

python
Copy code
USERNAME = "your_email@example.com"
PASSWORD = "your_password"
3️⃣ Run All Tests
bash
Copy code
pytest
4️⃣ View Test Report
Go to the reports/ folder

Open report.html in your browser

🌐 Test Scenarios Covered
Test Case	Description
Login Test	Verifies valid user login
Search Test	Checks if search results display correctly
Cart Test	Adds a product to cart and verifies cart page


🧪 Sample Test Report Preview

💡 Future Enhancements
Add negative test cases

Integrate with Jenkins for CI/CD

Add API testing module

Cross-browser testing support

🙋‍♂ Author
👨‍💻 Raj Kumar Ramisetty
📧 ramisettyrajkumar007@gmail.com
🔗LINKEDIN : https://www.linkedin.com/in/ramisetty-raj-kumar-bb432b27b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

🐙 GITHUB : 
https://github.com/RamisettyRajkumar
