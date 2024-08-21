import streamlit as st

# Datos del producto
precios_proveedor = {
    100: 30.56,
    250: 38.13,
    500: 40.30,
    1000: 48.96,
    1500: 62.48,
    2000: 72.22,
    2500: 80.06,
    5000: 117.93
}

# Datos del envío y diseño
costo_envio = 16.99
costo_diseno = 85.00

# Función para calcular el costo final


def calcular_costo_final(unidades):
    if unidades in precios_proveedor:
        costo_proveedor = precios_proveedor[unidades]
        costo_final = costo_proveedor + costo_envio + costo_diseno
        return costo_final
    else:
        return None


# Interfaz de usuario con Streamlit
st.title("Calculadora de Costo para Business Cards")
st.write("Agencia de Marketing Digital: Inzings")

# Aquí añadimos la frase con el resaltado en naranja y letras negras
st.markdown(
    """
    **Mensaje:** Gracias por preferirnos! Aquí está el detalle de su presupuesto para las Business cards que desea.
    <span style="background-color: #fb8500; color: black; padding: 5px; border-radius: 5px;">
    Tenga en cuenta que este precio incluye: diseño, impresión y envío por correo postal hasta su dirección.
    </span>
    """,
    unsafe_allow_html=True
)

# Selección de la cantidad de unidades
unidades = st.selectbox("Seleccione la cantidad de unidades", [
                        100, 250, 500, 1000, 1500, 2000, 2500, 5000])

if st.button("Calcular"):
    costo_final = calcular_costo_final(unidades)
    if costo_final is not None:
        st.success(f"El costo final para {
                   unidades} tarjetas de presentación es: ${costo_final:.2f}")
    else:
        st.error("Cantidad no disponible. Por favor, elige una cantidad válida.")

# Pie de página
st.write("Inzings.io - Su aliado en marketing digital")
