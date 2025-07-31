from PIL import Image
import os
import zipfile

def gif_to_png_and_zip(gif_path, output_folder):
    """
    Converts a GIF file into a sequence of PNG images and creates a ZIP archive of them.

    Args:
        gif_path (str): The path to the input GIF file.
        output_folder (str): The folder where the output PNG files will be saved.
    """
    try:
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # --- Step 1: Extract frames from GIF ---
        with Image.open(gif_path) as im:
            num_frames = im.n_frames
            for i in range(num_frames):
                im.seek(i)
                frame_path = os.path.join(output_folder, f"frame_{i:03d}.png")
                im.save(frame_path, "PNG")

        print(f" Successfully extracted {num_frames} frames to '{output_folder}'")

        # --- Step 2: Create a ZIP archive of the frames ---
        zip_path = output_folder + '.zip'
        print(f" Creating ZIP archive at '{zip_path}'...")

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for i in range(num_frames):
                file_name = f"frame_{i:03d}.png"
                file_path = os.path.join(output_folder, file_name)
                # Write file to zip, using just the filename as the archive name
                zipf.write(file_path, arcname=file_name)

        print(f" Successfully created ZIP file.")

    except FileNotFoundError:
        print(f" Error: The file '{gif_path}' was not found.")
    except Exception as e:
        print(f" An error occurred: {e}")

# --- Configuration ---
#  EDIT THESE VALUES
# Set the path to your input GIF file.
input_gif = "D:\\bhuvan\\project\\GIF2PNG-as-Zip\\Input.gif"

# Set the path to the folder for the extracted frames.
# The ZIP file will be created next to this folder with the same name.
output_png_folder = "D:\\bhuvan\\project\\GIF2PNG-as-Zip\\PNG"
# --------------------

# Run the conversion
gif_to_png_and_zip(input_gif, output_png_folder)