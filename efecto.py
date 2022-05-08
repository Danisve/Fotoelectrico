import streamlit as st
st.title("Efecto fotoélectrico")
st.write("Cuando la luz brilla en un metal,los electrones pueden ser expulsados de la superficie del metal en un fenómeno conocido como el efecto fotoeléctrico.")
st.write("Debido al efecto fotoeléctrico fue prueba que la luz tiene una dualidad, es decir, se puede comportar como partícula y como onda.")
st.image("FOTO.png")
st.subheader("Modelo propuesto por Einstein")
st.write("Con base en el modelo ondulatorio de la luz, los físicos predijeron que el aumento de la amplitud de la luz incrementaría la energía cinética de los fotoelectrones emitidos, mientras que el aumento de la frecuencia incrementaría la corriente medida. Contrario a las predicciones, los experimentos mostraron que el aumento en la frecuencia incrementaba la energía cinética de los fotoelectrones, mientras que el aumento en la amplitud de la luz incrementaba la corriente.")
st.write("Con base en estos descubrimientos, Einstein propuso que la luz se comportaba como una corriente de partículas llamadas fotones con una energía de:")
st.latex("E= hv")
st. write("La energía de un fotón es proporcional a la frecuencia de la luz (f) por lo que la amplitud de la luz (h) es proporcional al número de fotones con una frecuencia dada.")
st.markdown("![Alt Text](https://upload.wikimedia.org/wikipedia/commons/6/6e/EFECTOFOTOELECTRICOpeq.gif)")
st.subheader("Bandgap")
st.write("El bandgap o tambien conocido como banda prohibida es la energía mínima necesaria para excitar un electrón desde su estado ligado a un estado libre que le permita participar en la conducción, dentro de una celda solar. Lo importante a resaltar aqui es el intervalo de banda es la cantidad mínima de energía necesaria para un electrón de liberarse de su estado de enlace. Cuando se cumple la energía de banda prohibida, el electrón es excitado a un estado libre, y por lo tanto puede participar en la conducción.La brecha de banda determina la cantidad de energía que se necesita del sol para la conducción, así como la cantidad de energía que se genera.Un agujero se crea donde el electrón estaba obligado anteriormente. Este agujero también participa en la conducción.")
st.markdown("![Alt Text](https://upload.wikimedia.org/wikipedia/commons/1/1f/Bulkbandstructure.gif)")
st.write("Ese “agujero” que participa en la conducción, su movimiento es análogo al movimiento de una burbuja en un líquido. A pesar de que en realidad es el líquido que se mueve, es más fácil para describir el movimiento de la burbuja que va en la dirección opuesta.")
st.markdown("![Alt Text](https://i.pinimg.com/originals/c1/4f/b5/c14fb5f3ad4a890f9296c2f842068463.gif)")
Energia = st.select_slider("dame la energía del fotón", options=["4.60*10**-19","7.08*10**-19","6.25*10**-19","3.78*10**-19","4.33*10**-19"])
st.write("Tu metal es",Energia)
if Energia = 4.60*10**-19:
  st.write("Tu metal es el calcio")
if Energia = 7.08*10**-19:
  st.write("Tu metal es el estaño")
if Energia = 3.78*10**-19:
  st.write ("Tu metal es el sodio")
if Energia = 6.25*10**-19:
  st.write ("Tu metal es el Hafnio")
if Energia = 4.33*10**-19):
  st.write("Tu metal es el Samario")
  
