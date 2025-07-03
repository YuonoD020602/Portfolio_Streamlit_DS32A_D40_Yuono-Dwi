# Kontak Page for Streamlit Application
# This module displays contact information with links to LinkedIn, GitHub, and WhatsApp.
import streamlit as st

def tampilkan_kontak():
    st.title("📞 Kontak")

    st.markdown("Silakan hubungi saya melalui kanal berikut:")

    # Tiga kolom untuk LinkedIn, GitHub, WhatsApp
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/yuonodraharjo/)"
        )

    with col2:
        st.markdown(
            "[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/YuonoD020602)"
        )

    with col3:
        st.markdown(
            "[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-25D366?logo=whatsapp)](https://wa.me/6281227068269)"
        )

    # Garis pemisah
    st.markdown("---")

    # Email
    st.write("📧 Email: [yuonodwiraharjo26@gmail.com](mailto:yuonodwiraharjo26@gmail.com)")

    # Penutup dengan pesan positif
    st.success("Terima kasih telah mengunjungi! Jangan ragu untuk menghubungi saya untuk kolaborasi, riset, atau peluang kerja.")
