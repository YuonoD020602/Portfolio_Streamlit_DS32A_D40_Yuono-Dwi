import streamlit as st

def show_about_me():
    st.title("👤 About Me: Yuono!")

    with st.expander("📌 Quick Introduction"):
        st.markdown("""
        Hello! I'm **Yuono Dwi Raharjo**, a *Data Science and Psychometrics Enthusiast*  
        with a background in Psychology and extensive experience in data analysis, psychometric assessment, and dashboard development.  
        I believe that **good data leads to wise decisions** — whether in business, education, or public services.
        """)

    tab1, tab2, tab3 = st.tabs(["🎓 Education", "🧠 Skills", "💼 Experience"])

    with tab1:
        st.markdown("### 🎓 Education")
        st.markdown("""
        - **Data Science Bootcamp — Dibimbing.id** *(2025)*  
          Final Score: 98/100  
          Focus: Python, SQL, EDA, Dashboarding, Segmentation, People Analytics  
        
        - **Bachelor of Psychology — Universitas Gadjah Mada** *(2021–2025)*  
          GPA: 3.85/4.00  
          Focus: Psychometrics, Statistics, Research Methods, Big Data, Deep Learning

        - **Bachelor of Geophysics — UPN Veteran Yogyakarta** *(2020–2021)*  
          GPA: 4.00/4.00  
          Focus: Applied Mathematics
        """)

    with tab2:
        st.markdown("### 🛠️ Core Skills")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- **Data Science:** Python, SQL, R, SPSS, Jamovi")
            st.markdown("- **Data Visualization:** Power BI, Tableau, Looker Studio")
            st.markdown("- **Psychometrics & Stats:** CFA, SEM, CTT")
        with col2:
            st.markdown("- **Research & HR Analytics**")
            st.markdown("- **Financial & Project Management**")
            st.markdown("- **Tools:** Canva, Figma, Capcut")

    with tab3:
        st.markdown("### 💼 Selected Experience")

        st.markdown("**📌 UPAP Psychology UGM (2024)** – Development Staff")
        st.caption("• Created 100+ psychological test items, managed digital item bank, performed psychometric analysis, and led training sessions.")

        st.markdown("**📌 Psimetrika Indonesia (2023)** – Technical Staff Intern")
        st.caption("• Scoring tests, CTT analysis, developing digital questions on ethics, and HEXACO-SEM report writing.")

        st.markdown("**📌 Leadership & Assistant Roles**")
        st.caption("• Treasurer and HR Head in multiple committees | Teaching Assistant in Statistics & Quantitative Research")

    st.markdown("---")

    st.success("Thank you for visiting! I'm open to collaborations, research projects, and new opportunities.")
