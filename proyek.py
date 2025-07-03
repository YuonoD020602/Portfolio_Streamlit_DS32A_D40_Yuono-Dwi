import streamlit as st
import pandas as pd
import altair as alt

def show_actor():
    st.title("🎬 Actor Explorer")
    st.markdown("Explore and filter **Top 1000 Highest-Grossing Movie Actors** from global box office data.")
    st.caption("Use this dashboard to identify high-performing actors and use them in your prediction model.")

    st.markdown("---")

    # Load and clean dataset
    df = pd.read_csv("actor rank.csv", sep="\t")
    df["box_office_actor"] = df["box_office_actor"].str.replace(",", "").astype(float)
    df["average_actor"] = df["average_actor"].str.replace(",", "").astype(float)
    df["actor"] = df["actor"].str.strip()
    df["actor_score"] = 1001 - df["rank_actor"]

    # ================================
    # 🎛️ FILTER SECTION
    # ================================
    st.subheader("🎛️ Filter Actors")

    with st.expander("🔧 Customize your filter"):
        col1, col2 = st.columns(2)
        with col1:
            min_movies = st.slider("🎞️ Minimum Number of Movies", 1, 150, 30)
            box_office_range = st.slider(
                "💰 Total Box Office Range (USD)",
                min_value=int(df["box_office_actor"].min()),
                max_value=int(df["box_office_actor"].max()),
                value=(int(df["box_office_actor"].min()), int(df["box_office_actor"].max()))
            )
        with col2:
            avg_box_office_range = st.slider(
                "📈 Average Gross per Actor (USD)",
                min_value=int(df["average_actor"].min()),
                max_value=int(df["average_actor"].max()),
                value=(int(df["average_actor"].min()), int(df["average_actor"].max()))
            )
            search_actor = st.text_input("🔎 Search Actor Name")

    # ================================
    # 📌 FILTERING LOGIC
    # ================================
    filtered = df[
        (df["movies_actor"] >= min_movies) &
        (df["box_office_actor"].between(*box_office_range)) &
        (df["average_actor"].between(*avg_box_office_range))
    ]
    if search_actor:
        filtered = filtered[filtered["actor"].str.contains(search_actor, case=False, na=False)]

    st.markdown(f"🎯 **{len(filtered)}** actors matched your filters.")

    # ================================
    # 📊 METRICS
    # ================================
    st.markdown("### 📈 Summary Statistics")

    col1, col2, col3 = st.columns(3)
    col1.metric("🎬 Avg. Movies", f"{filtered['movies_actor'].mean():.1f}")
    col2.metric("💰 Total Gross", f"${filtered['box_office_actor'].sum():,.0f}")
    col3.metric("⭐ Avg. Actor Score", f"{filtered['actor_score'].mean():.1f}")

    # ================================
    # 📉 CHART
    # ================================
    st.markdown("### 📊 Box Office Performance")

    st.caption("Total box office by actor, colored by their average gross per movie.")
    chart = alt.Chart(filtered).mark_bar().encode(
        x=alt.X("box_office_actor:Q", title="Total Box Office (USD)"),
        y=alt.Y("actor:N", sort="-x", title="Actor"),
        color=alt.Color("average_actor:Q", scale=alt.Scale(scheme="blues"), legend=alt.Legend(title="Avg. Gross")),
        tooltip=["actor", "rank_actor", "actor_score", "movies_actor", "box_office_actor", "average_actor"]
    ).properties(width=800, height=450).interactive()

    st.altair_chart(chart, use_container_width=True)

    # ================================
    # 🌟 HIGHLIGHT
    # ================================
    if not filtered.empty:
        top_actor = filtered.sort_values("box_office_actor", ascending=False).iloc[0]
        st.success(f"🌟 Top Actor: **{top_actor['actor']}** — ${top_actor['box_office_actor']:,.0f} total gross | Score: {top_actor['actor_score']}")

    # ================================
    # 📄 DATA TABLE
    # ================================
    st.markdown("### 📋 Full Actor Table")

    with st.expander("🔍 View Data Table"):
        st.dataframe(
            filtered[["rank_actor", "actor", "movies_actor", "box_office_actor", "average_actor", "actor_score"]].reset_index(drop=True),
            use_container_width=True
        )

    # ================================
    # 🔗 LINK TO PREDICTION
    # ================================
    st.markdown("---")
    st.info("📌 Ready to predict? Use selected actor names in the **Machine Learning** page to estimate movie revenue.")
