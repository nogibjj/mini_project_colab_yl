[![Format](https://github.com/nogibjj/Liu_Yirang_Individual_Project_1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Liu_Yirang_Individual_Project_1/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/Liu_Yirang_Individual_Project_1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Liu_Yirang_Individual_Project_1/actions/workflows/install.yml)


# 706_DE_Individual_Project

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

# Assignment Requirements
*  Jupyter Notebook with:
    * Cells that perform descriptive statistics using Polars or Panda
    * Tested by using nbval plugin for pytest
* Makefile with the following:
    * Run all tests (must test notebook and script and lib)
    * Formats code with Python Black
    * Lints code with Ruff
    * Installs code via: pip install -r requirements.txt
* test_script.py to test script
* test_lib.py to test library
* Pinned requirements.txt
* GitHub Actions performs all four Makefile commands with badges for each one in the README.md
