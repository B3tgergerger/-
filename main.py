import os
import zstandard as zstd
import brotli
from tkinter import Tk, filedialog, Button, Label

def compress_file(input_file, output_file, method='zstd'):
    if method == 'zstd':
        cctx = zstd.ZstdCompressor()
        with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
            f_out.write(cctx.compress(f_in.read()))
    elif method == 'brotli':
        with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
            f_out.write(brotli.compress(f_in.read()))
    else:
        raise ValueError("Unsupported compression method")

def main():
    root = Tk()
    root.title("File Compressor")

    def select_files():
        files = filedialog.askopenfilenames(title="Select files to compress")
        for file in files:
            output_file = filedialog.asksaveasfilename(defaultextension=".zst", filetypes=[("Zstandard files", "*.zst"), ("Brotli files", "*.br")])
            compress_file(file, output_file, method='zstd')
            Label(root, text=f"File saved: {output_file}").pack()

    Button(root, text="Select and Compress Files", command=select_files).pack()
    root.mainloop()

if __name__ == "__main__":
    main()
