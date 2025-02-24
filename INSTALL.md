# Installation Guide

Follow these steps to set up the project on your local machine using **Python 3.10.x** (recommended by Viam).

## Prerequisites

- **Python 3.10.x** (any version from 3.10.0 to 3.10.9)
- `pip` (Python package manager)

## Installation Steps

1. **Clone the Repository** (if applicable):

    ```bash
    git clone https://github.com/yourusername/yourprojectname.git
    cd yourprojectname
    ```

2. **Install Python 3.10.x** (if you don’t have it installed yet):

    If you're using **`pyenv`** (recommended for managing Python versions):

    ```bash
    pyenv install 3.10.x  # Replace with the desired 3.10 version
    pyenv global 3.10.x    # Set it as your global version
    ```

    Example (to install Python 3.10.7 specifically):

    ```bash
    pyenv install 3.10.7
    pyenv global 3.10.7
    ```

    Alternatively, you can download and install Python 3.10.x from the official [Python website](https://www.python.org/downloads/release/python-3100/).

3. **Create the Virtual Environment**:

    Ensure you're using **Python 3.10.x** for the virtual environment:

    ```bash
    python3 -m venv venv
    ```

4. **Activate the Virtual Environment**:

    - On **macOS/Linux**:

        ```bash
        source venv/bin/activate
        ```

    - On **Windows**:

        ```bash
        .\venv\Scripts\activate
        ```

    After activation, your terminal should show `(venv)` before the command prompt.

5. **Install Dependencies**:

    Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    If you don’t have a `requirements.txt` file, manually install the necessary packages:

    ```bash
    pip install <package-name>
    ```

## Deactivate Virtual Environment

Once you’re done working in the virtual environment, deactivate it by running:

```bash
deactivate

