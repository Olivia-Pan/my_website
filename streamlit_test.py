import streamlit as st
import base64

st.set_page_config(layout="centered")

st.title("Test PDF Display")

try:
    with open("fin_pre3.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
        pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" 
                width="100%" height="600" type="application/pdf"></iframe>
        """
        st.markdown("### 🔽 Presentation Slides")
        st.markdown(pdf_display, unsafe_allow_html=True)
except Exception as e:
    st.error(f"❌ Error loading PDF: {e}")
