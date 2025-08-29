import streamlit as st
import requests

# URL de ton API FastAPI
API_URL = "http://127.0.0.1:80/upload"

# Types de documents supportés
CLASS_NAMES = ["Carte_Nina", "invoice", "mail", "passeport","photo"]

st.title("📄 Vérification des documents")

# Choix du type attendu
expected_type = st.selectbox("Choisissez le type de document attendu :", CLASS_NAMES)

# Upload du fichier
uploaded_file = st.file_uploader("Uploader un document (PDF ou image)", type=["pdf", "jpg", "jpeg", "png"])

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
    data = {"expected_type": expected_type}

    # Appel à l’API FastAPI
    response = requests.post(API_URL, files=files, data=data)

    if response.status_code == 200:
        result = response.json()
        if result["status"] == "accepted":
            st.success(f"✅ {result['message']}")
        else:
            st.error(f"❌ {result['message']}")
    else:
        st.error("Erreur lors de la communication avec l’API.")