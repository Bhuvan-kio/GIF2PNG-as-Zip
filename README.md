# 🖼️ GIF to PNG & ZIP Converter

> **animation.gif &nbsp; → &nbsp; [ frame_001.png, frame_002.png, ... ] &nbsp; → &nbsp; frames.zip**

This Python script automates the process of converting an animated GIF into a sequence of individual PNG frames and then conveniently packages them into a single `.zip` archive for easy storage and sharing.

---

## ✨ Features

-   **Frame Extraction**: Reads an animated GIF and saves every frame as a separate file.
-   **PNG Output**: Converts each frame into a high-quality PNG image.
-   **Sequential Naming**: Names the output files in a numbered sequence (e.g., `frame_000.png`) for easy sorting.
-   **Automatic ZIP Creation**: After extracting the frames, the script automatically compresses all the new PNG files into a single `.zip` file.
-   **Minimal Dependencies**: Built using the popular `Pillow` library and Python's standard `zipfile` module.

---

## 🛠️ Prerequisites

Before you begin, ensure you have Python 3 and the `Pillow` library installed.

1.  **Python 3**: If you don't have it, download it from [python.org](https://www.python.org/downloads/).
2.  **Pillow Library**: Install it using pip in your terminal or command prompt. The `zipfile` library is included with Python, so no extra installation is needed for it.
    ```bash
    pip install Pillow
    ```

---

## 🚀 How to Use

1.  **Save the Script**: Have your Python script ready (e.g., named `convert_and_zip.py`).
2.  **Configure Paths**: Open the script and edit the configuration variables to point to your input GIF and desired output folder.
3.  **Run the Script**: Open a terminal, navigate to the folder where your script is saved, and run it.
    ```bash
    python convert_and_zip.py
    ```

The script will create a folder containing all the PNG frames, as well as a separate `.zip` file in the same directory.

---

## 📄 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).