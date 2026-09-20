#<imports, listas y variables previas al programa>
import streamlit as st #para interfaz
import random as rd #codigo al azar
from datetime import datetime #para la fecha

if "ordenado" not in st.session_state:
    st.session_state.ordenado = False

pagos = ["Efectivo","Tarjeta"]

st.title("Restaurante: El python")

col1,col2,col3,col4,col5,col6= st.columns([5,5,5,4.5,5,4])

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap');

    body {
        font-family: 'Roboto Mono', monospace;
        background-color: #1e1e2f;
    }

    .stNumberInput {
        border: 2px solid #ffffff;
        border-radius: 20px;
        margin-bottom: 15px;
        padding: 5px;
        background-color: rgb(18, 4, 53);
    }
    </style>
""", unsafe_allow_html=True)
#<imports, listas y variables previas al programa>

#<MAIN>

with col1:
    c1 = st.number_input("sandwich while queso", 
    min_value=0, step=1,)
    st.title("$50")
    st.write("Un sanwis de quesito derretido bien rico...")

with col2:
    c2 = st.number_input("def nachos(carnita)",
    min_value=0,max_value=10,value=0)
    st.title("$65")
    st.write("Unos nachos con queso, crema, frijoles y carnita")

with col3:
    c3 = st.number_input("Waffle Input",
    min_value=0,max_value=10,value=0)
    st.title("$60")
    st.write("Un Waffle con nutella, mermelada, lechera o maní")

with col4:
    c4 = st.number_input("for peperoni in waffle",
    min_value=0,max_value=10,value=0)
    st.title("$65")
    st.write("Los clasicos Wafflepizzas de Ludus (Los extraño tanto como a ella)")

with col5:
    c5 = st.number_input("Nieve.append(s)",
    min_value=0,max_value=10,value=0)
    st.title("$30")
    st.write("3 bolas de nieve en un vasito, sabor vainilla, chocolate o fresa")

with col6:
    c6 = st.number_input("Pal or Mitas",
    min_value=0,max_value=10,value=0)
    st.title("$40")
    st.write("Solo traduce 'or' y veras que es")

#<LOGICA DE BOTONES>
boton = st.button("Ordenar")

if boton:
    st.session_state.ordenado = True
#<LOGICA DE BOTONES>

total = c1*50 + c2*65 + c3*60 + c4*65 + c5*30 + c6*40 #lit la cuenta lol
dia_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
total_iva = total*0.16
total2 = total + total_iva

if st.session_state.ordenado and (c1+c2+c3+c4+c5+c6)==0:
    st.write("No puedes ordenar nada lol, ordena algo anda :3")
if st.session_state.ordenado and (c1+c2+c3+c4+c5+c6)>=1:
    st.write("Cual sera tu metodo de pago?")
    metodo = st.selectbox("Pago: ",pagos)
    ticket =     "##########################################\n"
    ticket+=     "#             RESTAURANTE                #\n"
    ticket+=     "#                 EL                     #\n"
    ticket+=     "#               PYTHON                   #\n"
    ticket+=     "##########################################\n"
    ticket+=     "==========================================\n"
    ticket+=    f"Tiempo de compra: {dia_hora}\n"
    ticket+=     "Datos del pedido:\n"
    ticket+=    f"Metodo de pago:                 {metodo}\n"
    if c1>=1:
        ticket+=    f"    Sanwich while queso     $   {c1*50}//MXN\n"
    if c2>=1:
        ticket+=    f"    def nachos(carnita)     $   {c2*65}//MXN\n"
    if c3>=1:
        ticket+=    f"    Waffle Input            $   {c3*60}//MXN\n"
    if c4>=1:
        ticket+=    f"    for pepperoni in waffle $   {c4*65}//MXN\n"
    if c5>=1:
        ticket+=    f"    helado.append(s)        $   {c5*30}//MXN\n"
    if c6>=1:
        ticket+=    f"    Pal or Mitas            $   {c6*40}//MXN\n"
    ticket+=         "------------------------------------------\n"
    ticket+=     f"SUBTOTAL:                   $   {total}//MXN\n"
    ticket+=     f"     IVA:                   $   {total_iva}//MXN\n"
    ticket+=     f"   TOTAL:                   $   {total2}//MXN\n"
    if metodo == "Efectivo":
        st.write("Bien, toma, este es tu codigo de verificacion," \
        "muestralo en caja y paga")

        a = rd.randint(0,9)
        b = rd.randint(0,9)
        c = rd.randint(0,9)
        d = rd.randint(0,9)
        
        st.write(f"{a}{b}{c}{d}")
        st.write(f"Total: ${total}//MXN")
        ticket+=     f"==========================================\n"
        st.download_button(
        label="⬇️ Descargar Ticket",
        data=ticket,
        file_name="ticket.txt",
        mime="text/plain"
        )

    if metodo == "Tarjeta":

        tarjeta = st.text_input("Tarjeta: ")

        if len(tarjeta)<16 or len(tarjeta)>16:
            st.write("Coloca 16 digitos por favor")

        elif not tarjeta.isnumeric():
            st.write("Solo coloca digitos por favor")
            
        else:
            ticket+=  f" TARJETA: {tarjeta[0]}{tarjeta[1]}{tarjeta[2]}{tarjeta[3]}************\n"
            ticket+=     f"==========================================\n"
            st.write("El pago fue aceptado con exito")
            st.write(f"Total: ${total}//MXN")
            dia_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
            st.download_button(
            label="⬇️ Descargar Ticket",
            data=ticket,
            file_name="ticket.txt",
            mime="text/plain"
            )