# Project 1: Continuous Integration using Gitlab Actions of Python Data Science Project

# Explanation Video


# Directory

Liu_Yirang_Individual_Project_1/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│       ├── format.yml
│       ├── install.yml
│       ├── lint.yml
│       └── test.yml
├── mylib/
│   ├── __init__.py
│   └── calculator.py
├── .gitignore
├── returnvsrisk.png
├── rollingaverage.png
├── stocks.md
├── stocks.csv
├── Dockerfile
├── main.py
├── Makefile
├── README.md
├── repeat.sh
├── requirements.txt
├── setup.sh
├── test_lib.py
└── test_main.py

# Requirements
The project structure must include the following files:
* Jupyter Notebook with: 
  * Cells that perform descriptive statistics using Polars or Panda.
  * Tested by using nbval plugin for pytest
* Makefile with the following:
  * Run all tests (must test notebook and script and lib)
  * Formats code with Python black
  * Lints code with Ruff
  * Installs code via:  pip install -r requirements.txt

test_script.py to test script
test_lib.py to test library
Pinned requirements.txt
Gitlab Actions performs all four Makefile commands with badges for each one in the README.md
