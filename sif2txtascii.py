import os
from pathlib import Path
import numpy as np
from tkinter import Tk, filedialog
import sif_parser

Tk().withdraw()
folder_selected = filedialog.askdirectory(title="Selecciona la carpeta con archivos SIF")

if not folder_selected:
    print("No se seleccionó ninguna carpeta. Saliendo.")
    exit()

input_folder = Path(folder_selected)

output_txt = input_folder / "TXT_Convertidos"
output_asc = input_folder / "ASC_Convertidos"

output_txt.mkdir(exist_ok=True)
output_asc.mkdir(exist_ok=True)

sif_files = list(input_folder.glob("*.sif"))

print(f"Se encontraron {len(sif_files)} archivos SIF.")

for sif_file in sif_files:
    try:
        data, info = sif_parser.np_open(str(sif_file))

        # =========================
        # 1️⃣ Extraer intensidad
        # =========================
        if data.ndim == 3:
            intensity = data[0].squeeze()
        else:
            intensity = data.squeeze()

        intensity = np.array(intensity)
        n_pixels = len(intensity)
        pixels = np.arange(n_pixels)

        # =========================
        # 2️⃣ Buscar calibración en header
        # =========================
        coeffs = None

        if "Calibration_data" in info:
            coeffs = info["Calibration_data"]

        elif "WavelengthCalibrationCoefficients" in info:
            coeffs = info["WavelengthCalibrationCoefficients"]

        # =========================
        # 3️⃣ Calcular longitud de onda
        # =========================
        if coeffs is not None:
            wavelength = np.zeros_like(pixels, dtype=float)
            for i, c in enumerate(coeffs):
                wavelength += c * pixels**i
            print(f"🔹 Calibración encontrada en {sif_file.name}")
        else:
            print(f"⚠️ No se encontró calibración en {sif_file.name}. Usando píxeles.")
            wavelength = pixels

        # =========================
        # 4️⃣ Crear 2 columnas
        # =========================
        spectrum = np.column_stack((wavelength, intensity))

        # =========================
        # 5️⃣ Guardar archivos
        # =========================
        txt_file = output_txt / f"{sif_file.stem}.txt"
        np.savetxt(
            txt_file,
            spectrum,
            fmt="%.6f",
            delimiter="\t",
            header="Longitud_de_onda(nm)\tIntensidad",
            comments=""
        )

        asc_file = output_asc / f"{sif_file.stem}.asc"
        np.savetxt(
            asc_file,
            spectrum,
            fmt="%.6f",
            delimiter="\t",
            header="Longitud_de_onda(nm)\tIntensidad",
            comments=""
        )

        print(f"✅ {sif_file.name} → convertido correctamente en λ vs Intensidad")

    except Exception as e:
        print(f"❌ Error con {sif_file.name}: {e}")