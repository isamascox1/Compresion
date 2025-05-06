import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

try:
    # Abrir un cuadro de diálogo para seleccionar la imagen
    input_image_path = filedialog.askopenfilename(
        title="Seleccionar imagen",
        filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if not input_image_path:
        raise Exception("No se seleccionó ninguna imagen.")

    # Abrir un cuadro de diálogo para guardar la imagen comprimida
    output_image_path = filedialog.asksaveasfilename(
        title="Guardar imagen comprimida",
        defaultextension=".jpg",
        filetypes=[("Archivos JPEG", "*.jpg")]
    )
    if not output_image_path:
        raise Exception("No se seleccionó una ruta para guardar la imagen.")

    # Abrir y comprimir la imagen
    with Image.open(input_image_path) as img:
        img.save(output_image_path, "JPEG", quality=50)
        print("Imagen comprimida correctamente.")
except Exception as e:
    print(f"Error al comprimir la imagen: {e}")

