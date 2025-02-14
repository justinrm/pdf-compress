# pdf-compress

A Python script to compress PDF files using Ghostscript.

## Description

This script takes a directory containing PDF files as input, compresses them using Ghostscript, and saves the compressed PDFs into a new subdirectory within the input directory.  It offers different compression levels to balance file size and quality.  The script also includes robust error handling and checks for Ghostscript installation.

## Installation

1.  **Clone the repository (optional):**  If you cloned the repository, navigate to the directory where you cloned it.

2.  **Save the script:** Save the Python code as `pdf-compress.py`.

3.  **Install Ghostscript:** Ghostscript is required for PDF compression. On Ubuntu/Debian-based systems, install it using:

    ```bash
    sudo apt install ghostscript
    ```

    For other distributions, use the appropriate package manager (e.g., `yum`, `dnf`, `brew`).

## Usage

1.  **Run the script:** Open a terminal, navigate to the directory where you saved `pdf-compress.py`, and execute:

    ```bash
    python pdf-compress.py
    ```

2.  **Enter the directory:** The script will prompt you to enter the path to the directory containing the PDF files you want to compress.  Make sure to provide the full path.

3.  **Compressed PDFs:** The compressed PDFs will be saved in a new subdirectory within the input directory, named `compressed_pdfs` by default.

## Compression Levels

You can adjust the compression level by modifying the `-dPDFSETTINGS` option within the Ghostscript command in the script. The available options are:

*   `/screen`: Lowest quality, smallest file size (suitable for on-screen viewing).
*   `/ebook`: Medium quality (a good balance for most uses).
*   `/prepress`: High quality (for professional printing).
*   `/default`: Default quality.

To change the compression level, open `pdf-compress.py` in a text editor and modify the line containing `-dPDFSETTINGS` to your desired setting.  For example, to use ebook quality, change it to:

```python
"-dPDFSETTINGS=/ebook",
