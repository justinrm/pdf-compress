import os
import subprocess
import shutil

def compress_pdfs(input_dir, output_dir_name="compressed_pdfs"):
    """Compresses PDF files in a directory using Ghostscript.

    Args:
        input_dir: The directory containing the original PDF files.
        output_dir_name: The name of the subdirectory to store compressed PDFs.
                      Defaults to "compressed_pdfs".
    """

    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        return

    output_dir = os.path.join(input_dir, output_dir_name)
    os.makedirs(output_dir, exist_ok=True)  # Create if it doesn't exist

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            try:
                # Ghostscript command for compression (adjust quality as needed)
                # -dPDFSETTINGS=/screen  (for low-res, smallest file size)
                # -dPDFSETTINGS=/ebook   (for medium quality)
                # -dPDFSETTINGS=/prepress (for high quality)
                # -dPDFSETTINGS=/default  (default quality)

                command = [
                    "gs",
                    "-sDEVICE=pdfwrite",
                    "-dCompatibilityLevel=1.4",  # Important for some PDFs
                    "-dPDFSETTINGS=/screen", # Adjust this for compression level
                    "-dNOPAUSE",
                    "-dQUIET",
                    "-dBATCH",
                    "-sOutputFile=" + output_path,
                    input_path,
                ]

                subprocess.run(command, check=True)  # check=True raises exception on error

                print(f"Compressed: {filename}")

            except subprocess.CalledProcessError as e:
                print(f"Error compressing {filename}: {e}")
            except FileNotFoundError:
                print("Error: Ghostscript (gs) is not installed. Please install it (e.g., 'sudo apt install ghostscript').")
                return
            except Exception as e:  # Catch other potential errors
                print(f"An unexpected error occurred: {e}")
                return

    print("Compression complete.")


if __name__ == "__main__":
    input_directory = input("Enter the directory containing PDF files: ")  # Get input from the user
    compress_pdfs(input_directory)
