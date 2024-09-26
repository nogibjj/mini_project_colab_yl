[![Install](https://github.com/nogibjj/Liu_Yirang_Individual_Project_1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Liu_Yirang_Individual_Project_1/actions/workflows/install.yml)
[![Format](https://github.com/nogibjj/Liu_Yirang_Individual_Project_1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Liu_Yirang_Individual_Project_1/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/Liu_Yirang_Individual_Project_1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Liu_Yirang_Individual_Project_1/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/Liu_Yirang_Individual_Project_1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Liu_Yirang_Individual_Project_1/actions/workflows/test.yml)


# 706_DE_Individual_Project

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
├── Dockerfile
├── Histogram_of_ShareWomen.png
├── LICENSE
├── main.ipynb
├── main.py
├── Makefile
├── README.md
├── repeat.sh
├── requirements.txt
├── setup.sh
├── test_main.py
└── women-stem.csv

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

![alt text](<Histogram_of_ShareWomen.png>)
