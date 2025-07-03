import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import PolynomialFeatures
from numerize import numerize

def prediksi():
    # --- LOAD & PREPARE DATA ---
    data_actor = pd.read_csv('actor rank.csv', sep='\t')
    data_actor['actor'] = data_actor['actor'].str.lower()
    imdb_joblib = joblib.load('imdb_joblib')

    st.title("🎥 Movie Revenue Prediction")
    st.caption("Estimate a movie's **worldwide gross revenue** based on actors, budget, content rating, and more.")

    st.markdown("## 🧑‍🤝‍🧑 Actor Selection")
    st.info("Enter up to 4 actors. Partial names accepted. The system will automatically assign a score based on ranking.")

    with st.form("Prediction Form"):
        col1, col2, col3, col4 = st.columns(4)
        a1 = col1.text_input('🎭 1st Actor')
        a2 = col2.text_input('🎭 2nd Actor')
        a3 = col3.text_input('🎭 3rd Actor')
        a4 = col4.text_input('🎭 4th Actor')

        def get_score(name):
            if not name:
                return 1, "Not Provided"
            matched = data_actor[data_actor['actor'].str.contains(name.lower(), na=False)]
            if matched.empty:
                return 1, "❌ Not Found"
            rank = matched.iloc[0]['rank_actor']
            return 1001 - rank, f"✅ Found: Rank {rank}"

        # Score dan info aktor
        a1_score, a1_status = get_score(a1)
        a2_score, a2_status = get_score(a2)
        a3_score, a3_status = get_score(a3)
        a4_score, a4_status = get_score(a4)
        total_score = a1_score + a2_score + a3_score + a4_score

        with st.expander("🔎 Actor Ranking Status"):
            colA, colB, colC, colD = st.columns(4)
            colA.markdown(f"**1st:** {a1_status}")
            colB.markdown(f"**2nd:** {a2_status}")
            colC.markdown(f"**3rd:** {a3_status}")
            colD.markdown(f"**4th:** {a4_status}")

        st.markdown("---")
        st.markdown("## 🔞 Content Ratings")
        st.caption("Set the intensity levels for movie content (0 = none, 3 = severe).")

        def slider_with_icon(label, icon):
            return st.select_slider(f"{icon} {label}", ['None', 'Mild', 'Moderate', 'Severe'],
                                    value='None', key=label)

        def map_level(val): return {'None': 0, 'Mild': 1, 'Moderate': 2, 'Severe': 3}[val]

        col1, col2, col3, col4, col5 = st.columns(5)
        violence = map_level(col1.select_slider('Violence', ['None', 'Mild', 'Moderate', 'Severe']))
        nudity = map_level(col2.select_slider('Nudity', ['None', 'Mild', 'Moderate', 'Severe']))
        profanity = map_level(col3.select_slider('Profanity', ['None', 'Mild', 'Moderate', 'Severe']))
        alcohol = map_level(col4.select_slider('Alcohol', ['None', 'Mild', 'Moderate', 'Severe']))
        frightening = map_level(col5.select_slider('Frightening Scenes', ['None', 'Mild', 'Moderate', 'Severe']))

        st.markdown("---")
        st.markdown("## 🎬 Movie Details")

        col_dur, col_bud = st.columns(2)
        duration = col_dur.number_input('⏱️ Duration (minutes)', min_value=30, max_value=300, value=120)
        budget_million = col_bud.number_input('💵 Budget (in million USD)', min_value=1, max_value=500, value=200)
        budget = budget_million * 1_000_000

        # --- PREDICTION DATA ---
        data_input = pd.DataFrame([{
            'duration': duration,
            'nudity': nudity,
            'violence': violence,
            'profanity': profanity,
            'alcohol': alcohol,
            'frightening': frightening,
            'budget': budget,
            'is_Action': 1,
            'is_Adventure': 0,
            'is_Comedy': 1,
            'is_Drama': 0,
            'is_Romance': 1,
            'is_Other': 0,
            'total_star_score': total_score
        }])
        poly = PolynomialFeatures(degree=2)
        data_poly = poly.fit_transform(data_input)

        submitted = st.form_submit_button("🚀 Predict Revenue")

        if submitted:
            st.markdown("---")
            st.subheader("📊 Prediction Result")

            result = imdb_joblib.predict(data_poly)[0]
            revenue = "$ " + numerize.numerize(int(result))

            st.success("✅ Prediction Successful!")
            st.markdown(f"""
                <div style='text-align:center; padding:20px; background-color:#f5f9ff; border-radius:10px;'>
                    <h2>🌍 Estimated Worldwide Gross:</h2>
                    <h1 style='color:#3c8dbc'>{revenue}</h1>
                </div>
            """, unsafe_allow_html=True)

            st.caption("This prediction is based on the actor ranking, content intensity, duration, and budget.")
