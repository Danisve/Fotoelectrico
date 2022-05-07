import streamlit as st
st.title("Efecto fotoélectrico")
st.write("Cuando la luz brilla en un metal,los electrones pueden ser expulsados de la superficie del metal en un fenómeno conocido como el efecto fotoeléctrico.")
st.write("Debido al efecto fotoeléctrico fue prueba que la luz tiene una dualidad, es decir, se puede comportar como partícula y como onda.")
st.image("FOTO.png")
st.subheader("Modelo propuesto por Einstein")
st.write("Con base en el modelo ondulatorio de la luz, los físicos predijeron que el aumento de la amplitud de la luz incrementaría la energía cinética de los fotoelectrones emitidos, mientras que el aumento de la frecuencia incrementaría la corriente medida. Contrario a las predicciones, los experimentos mostraron que el aumento en la frecuencia incrementaba la energía cinética de los fotoelectrones, mientras que el aumento en la amplitud de la luz incrementaba la corriente.")
st.write("Con base en estos descubrimientos, Einstein propuso que la luz se comportaba como una corriente de partículas llamadas fotones con una energía de:")
st.latex("E= hv")
st. write ("La energía de un fotón es proporcional a la frecuencia de la luz (f) por lo que la amplitud de la luz (h) es proporcional al número de fotones con una frecuencia dada."
st.markdown("![Alt Text](https://upload.wikimedia.org/wikipedia/commons/6/6e/EFECTOFOTOELECTRICOpeq.gif)")
st.subheader("Bandgap")
st.write("El bandgap o tambien conocido como banda prohibida es la energía mínima necesaria para excitar un electrón desde su estado ligado a un estado libre que le permita participar en la conducción, dentro de una celda solar. Lo importante a resaltar aqui es el intervalo de banda es la cantidad mínima de energía necesaria para un electrón de liberarse de su estado de enlace. Cuando se cumple la energía de banda prohibida, el electrón es excitado a un estado libre, y por lo tanto puede participar en la conducción.La brecha de banda determina la cantidad de energía que se necesita del sol para la conducción, así como la cantidad de energía que se genera.Un agujero se crea donde el electrón estaba obligado anteriormente. Este agujero también participa en la conducción.")
           
df = pd.DataFrame(
    np.random.randn(23, 2),
    columns=('col %d' % i for i in range(2)))

st.table(df)
