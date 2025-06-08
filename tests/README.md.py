# 🧪 Selenium Test Automation Suite

This project contains a suite of automated UI tests written in Python using **Selenium** and **pytest**.
The tests are structured by difficulty level and cover a wide range of web automation techniques — from basic interactions to advanced handling of multiple windows, frames, and JavaScript execution.

---

## 📁 Project Structure



tests/
├── easy/
│ ├── login/
│ └── browser_commands/
├── intermediate/
│ ├── dropdowns/
│ ├── sliders/
│ └── iframes/
├── advanced/
│ ├── tabs/
│ └── authentication/
conftest.py

## 🚀 How to Run the Tests

1. **Clone the repo**:
   ```bash
   git clone https://github.com/demian-rafasquino/Selenium-Scripts.git
   cd Selenium-Scripts

2.Create a virtual environment (optional but recommended):
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3.Install the dependencies:
pip install -r requirements.txt

4.Run all tests:
pytest tests/

5.Run a specific test file:
pytest tests/easy/login/test_simple_login_1.py

Technologies Used

Python 3.13
Selenium
pytest

Author
Demian Rafasquino