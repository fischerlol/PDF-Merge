# PDF Merge Tool

A simple and efficient tool to merge multiple PDF files. Whether you have PDFs in different directories or all in the current directory, this tool is your one-stop solution for merging them into a single file.

## Features

- Merge PDFs from a specified directory.
- Merge specific PDF files using their paths.
- Merge all PDFs from the current directory.
- Specify the name of the output file.

## Prerequisites

Before you get started, make sure you have the following installed:
- Python 3.8+

## Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/fischerlol/PDF-Merge.git
```

2. Navigate to the project directory:
```bash
cd pdf-merge-tool
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Add the tool to your system's PATH. For Windows users:
   - Open System Properties -> Advanced -> Environment Variables.
   - In the System Variables section, find the PATH variable, select it, and click Edit.
   - In the Edit Environment Variable window, click New and add the path to the `pdf-merge-tool` directory.
   - Click OK to save the changes.

## Usage

Once installed, you can use the tool directly from your command prompt:

- Merge PDFs from a specified directory:
```bash
pdf-merge -d path-to-directory
```

- Merge specific PDF files:
```bash
pdf-merge -f path-to-pdf1 -f path-to-pdf2 ...
```

- Merge all PDFs from the current directory:
```bash
pdf-merge -c
```

- Specify the name of the output file (default is `merged.pdf`):
```bash
pdf-merge -d path-to-directory -o output-filename.pdf
```

## Contributing

Pull requests are welcome! If you encounter any issues or have suggestions for improvements, please open an issue first to discuss what you'd like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
