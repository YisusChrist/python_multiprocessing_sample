Sample code to test the performance of different ways to process a list of numbers using classic, list comprehension, and multiprocessing methods.

<br>

<details>
<summary>Table of Contents</summary>

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Options](#options)
- [Results](#results)
- [License](#license)
- [Credits](#credits)

</details>

# Introduction

This Python script provides a comparison of different approaches to processing a list of numbers. It includes three methods:

- `Classic iteration`
- `List comprehension`
- `Multiprocessing`

The script measures the execution time for each method and compares their performance.

# Prerequisites

- Python 3.7 or later
- Rich library (optional, for enhanced console output)

> [!NOTE]
> The software has been developed and tested using Python `3.12.1`. The minimum required version to run the software is Python 3.7. Although the software may work with previous versions, it is not guaranteed.

# Usage

1. Clone the repository:

   ```sh
   git clone https://github.com/YisusChrist/python_multiprocessing_sample.git
   ```

2. Navigate to the project directory:

   ```sh
   cd python_multiprocessing_sample
   ```

3. Run the script:

   ```sh
   python main.py
   ```

# Options

- `DIVIDE`: Boolean flag to determine whether to divide or multiply the numbers.
- `MAX_NUMBER`: The maximum number used in the processing function.
- `TEST_SIZE`: Size of the list of numbers to process.

# Results

The script will display the execution time for each method along with the first few processed numbers.

# License

This project is released under the [GPL-3.0 License](https://opensource.org/licenses/GPL-3.0).

# Credits

Special thanks to [Julynx](https://github.com/Julynx) for the inspiration to create this project. He provided the idea and the initial code to compare the performance of different methods to process a list of numbers.

The version published here is an enhanced and more complete version of the original code.
