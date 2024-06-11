# AutoGen

This repository contains Python notebooks to get started with the AutoGen framework.

## How to Run the Notebooks in This Project

### Prerequisites

Ensure you have the following installations on your computer:

1. **Visual Studio Code (VS Code)**
   - Download and install from [VS Code download](https://code.visualstudio.com/download).
   - After installation, install the Python extension from Microsoft in your VS Code.

2. **Python**
   - Download and install from [Python downloads](https://www.python.org/downloads/).
   - Ensure the version is Python >= 3.8, < 3.13.

3. **Anaconda**
   - Download and install from [Anaconda download](https://www.anaconda.com/download).

### Setup Instructions

1. **Create and Activate a Conda Environment**
   - Open Anaconda Prompt and create an environment:
     ```sh
     conda create -n pyautogen python=<<your_python_version>>
     ```
   - Activate the environment:
     ```sh
     conda activate pyautogen
     ```

2. **Install Required Packages**
   - Install AutoGen:
     ```sh
     pip install pyautogen
     ```
   - Install AutoGen Studio:
     ```sh
     pip install autogenstudio
     ```

3. **Launch VS Code from the Anaconda Environment**
   - Use the following command to launch VS Code:
     ```sh
     code .
     ```

4. **Select the Python Interpreter in VS Code**
   - Open the command palette with `Ctrl+Shift+P` and select:
     ```
     Python: Select Interpreter
     ```

### Running the Notebooks

1. **Clone the Repository**
   - Clone this repository to your local machine.

2. **Configure the Environment**
   - Add the appropriate values for keys in the `.env` file.

3. **Execute Notebooks**
   - Run any notebook using the command:
     ```sh
     python <<notebook_name>>.py
     ```

Enjoy working with AutoGen!
