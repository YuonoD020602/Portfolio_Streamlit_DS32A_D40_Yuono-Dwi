
import streamlit as st
st.set_page_config(page_title="Portfolio | Yuono Dwi Raharjo",
                   layout="wide", page_icon="🚀")

# Judul halaman utama
st.title("🚀 Portfolio Yuono Dwi Raharjo")
st.header("🔬 Data Scientist & Developer")

# Sidebar
st.sidebar.title("📂 Navigasi")
st.sidebar.markdown("---")
st.sidebar.markdown("👋 **Selamat datang!**\nSilakan pilih halaman yang ingin kamu lihat.")

# Navigasi halaman (nama TETAP)
page = st.sidebar.radio("Pilih Halaman",
                        ["Tentang Saya", "Proyek", "Machine Learning", "Kontak"])

st.sidebar.markdown("---")
st.sidebar.info("✨ Dibuat dengan Streamlit oleh Yuono Dwi Raharjo")

if page == 'Tentang Saya':
    import tentang
    tentang.show_about_me()

if page == 'Proyek':
    import proyek
    proyek.show_actor()  # Importing the proyek module to display actor analysis

if page == 'Machine Learning':
    import prediksi
    prediksi.prediksi()  # Importing the prediksi module to run the prediction model

if page == 'Kontak':
    import kontak
    kontak.tampilkan_kontak() # Importing the kontak module to display contact information 
