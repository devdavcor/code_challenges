import speedtest


def medir_velocidad():
    st = speedtest.Speedtest()

    print("Iniciando prueba de velocidad...")
    velocidad_descarga = st.download() / 1_000_000  # Convertir a Mbps
    velocidad_carga = st.upload() / 1_000_000  # Convertir a Mbps

    print(f"Velocidad de descarga: {velocidad_descarga:.2f} Mbps")
    print(f"Velocidad de carga: {velocidad_carga:.2f} Mbps")


if __name__ == "__main__":
    medir_velocidad()
