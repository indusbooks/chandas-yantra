import streamlit as st
import random

st.title("🌺 Chandaḥ–Sāra–Yantram")
st.caption("Chando vāṅmayam sarvam")

k = st.slider("Gaṇas per pāda", 1, 6, 3)

mode = st.radio("Mode", ["AI","Random","Gayatri","Dandaka"])

if st.button("🔥 Generate"):
seq = [random.choice(["G","L"]) for _ in range(k*3)]
kannada = " ".join(["ವಿಷ್ಣು" if s=="G" else "ಬ್ರಹ್ಮ" for s in seq])

st.markdown("### 📜 Output")
st.write("Kannada:", kannada)
st.write("Sequence:", "".join(seq))