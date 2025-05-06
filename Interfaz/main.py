import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image

def seleccionar_imagen():
    try:
        # Abrir un cuadro de diálogo para seleccionar la imagen
        ruta_imagen = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if not ruta_imagen:
            return  # Si no se selecciona nada, salir de la función

        # Intentar comprimir la imagen
        output_path = filedialog.asksaveasfilename(
            title="Guardar imagen comprimida",
            defaultextension=".jpg",
            filetypes=[("Archivos JPEG", "*.jpg")]
        )
        if not output_path:
            return  # Si no se selecciona nada, salir de la función

        # Obtener el valor de calidad seleccionado
        calidad = int(opcion_calidad.get())

        with Image.open(ruta_imagen) as img:
            img.save(output_path, "JPEG", quality=calidad)
            messagebox.showinfo("Éxito", "Imagen comprimida correctamente")
    except Exception as e:
        # Mostrar el error en un cuadro de diálogo
        messagebox.showerror("Error", f"Error al comprimir la imagen: {e}")

def elegir_calidad():
    # Abrir un cuadro de diálogo para seleccionar la calidad
    calidad = simpledialog.askinteger(
        "Calidad de compresión",
        "Ingrese un valor de calidad (1-100):",
        minvalue=1,
        maxvalue=100
    )
    if calidad is not None:
        opcion_calidad.set(str(calidad))
        label_calidad.config(text=f"Calidad seleccionada: {calidad}")  # Actualizar la etiqueta

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Compresor de Imágenes")

# Crear un título principal
titulo = tk.Label(ventana, text="Compresión de imagen", font=("Arial", 16, "bold"))
titulo.pack(pady=5)

# Crear un subtítulo
subtitulo = tk.Label(ventana, text="by isamascox1", font=("Arial", 10, "italic"))
subtitulo.pack(pady=2)

# Crear un botón para elegir la calidad de compresión
btn_calidad = tk.Button(ventana, text="Elegir Calidad", command=elegir_calidad)
btn_calidad.pack(pady=5)

# Variable para almacenar la calidad seleccionada
opcion_calidad = tk.StringVar(value="50")  # Valor predeterminado

# Crear una etiqueta para mostrar la calidad seleccionada
label_calidad = tk.Label(ventana, text="Calidad seleccionada: 50")  # Valor inicial
label_calidad.pack(pady=5)

# Crear un botón para seleccionar la imagen
btn_seleccionar = tk.Button(ventana, text="Seleccionar Imagen", command=seleccionar_imagen)
btn_seleccionar.pack(pady=20)

# Ejecutar el bucle principal de la interfaz
ventana.mainloop()