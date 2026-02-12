# Difference Generator (Gendiff)

Gendiff is a command-line utility that identifies differences between two configuration files. It supports JSON and YAML formats and provides several output styles, including a nested tree, a plain text summary, and a machine-readable JSON format.

---

## 📊 Project Status
| Tool | Status |
| :--- | :--- |
| **Hexlet Tests** | [![Actions Status](https://github.com/Cheshire-12/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Cheshire-12/python-project-50/actions) |
| **Pytest and linter** | [![Python CI](https://github.com/Cheshire-12/python-project-50/actions/workflows/py-project-50.yaml/badge.svg?branch=main)](https://github.com/Cheshire-12/python-project-50/actions/workflows/py-project-50.yaml) |
| **SonarCloud Quality Gate** |  [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Cheshire-12_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Cheshire-12_python-project-50) |
| **Coverage** | [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Cheshire-12_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Cheshire-12_python-project-50) |
| **Lines of code** | [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Cheshire-12_python-project-50&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Cheshire-12_python-project-50) |

---

## 🛠 Installation

The project requires **Python 3.12 or newer** and the **`uv`** package manager/build tool for correct installation.

### 1. Installation

To install the package as a command-line tool, you must complete the full cycle: dependency synchronization, **wheel file creation**, and final installation. These steps are automated by the `make setup` command:
```bash
# 1. Clone the repository
# Choose one method:
# HTTPS (universal):
git clone https://github.com/Cheshire-12/python-project-50.git
# SSH (Requires SSH key setup):
git clone git@github.com:Cheshire-12/python-project-50.git

# 2. Run the automated installation command
# Executes: uv sync, uv build, uv tool install dist/*.whl
make setup
```
**Important**: After running this command, all executable scripts (`gendiff`) become available directly in your terminal without needing the `uv run` prefix.
### 2. Running the utility
Once installed, the `gendiff` command will be available in your terminal.
```bash
gendiff [options] <first_file> <second_file>
```
Options:
`-h, --help`: Show help message and exit.
`-f, --format`: Choose output format (`stylish`, `plain`, `json`). Default: `stylish`.

## Examples:

```bash
# Compare flat JSON files (Stylish format)
gendiff file1.json file2.json

# Compare YAML files in Plain format
gendiff -f plain file1.yaml file2.yaml

# Generate machine-readable JSON output
gendiff -f json file1.json file2.json
```
---
## 📺 Demo (Asciinema)
| Scenario | Links |
| :--- | :---: |
| Comparing Flat Files (JSON)| [Watch Demo](https://asciinema.org/a/v3P9K7xo1NBwkCe3) |
| Comparison of flat files (YAML) | [Watch Demo](https://asciinema.org/a/vt09nTXkXAfB4PI5) |
| Nested Structures | [Watch Demo](https://asciinema.org/a/tsCHqV91lXR49R9T) |
| Plain Format Output | [Watch Demo](https://asciinema.org/a/nFYMJFaTF5NfWmUg) |
|JSON Format Output | [Watch Demo](https://asciinema.org/a/lNAod8s0VRKKb76b) |

---

## Development
```bash
# Run pytest
make test

# Check code coverage
make coverage

# Run linter (Ruff)
make lint