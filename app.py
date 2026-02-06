streamlit
pandas
import streamlit as st

st.set_page_config(
    page_title="Researcher Profile",
    page_icon="🧠",
    layout="wide"
)

# ---------- Sidebar ----------
st.sidebar.title("Quick links")
email = st.sidebar.text_input("Contact email (optional)", "")
if email:
    st.sidebar.write(f"📧 {email}")

st.sidebar.markdown("---")
st.sidebar.markdown("**Sections**")
st.sidebar.markdown("- About\n- Research\n- Publications\n- Projects\n- Skills\n- Contact")

# ---------- Header ----------
st.title("Your Name — Researcher Profile")
st.caption("Affiliation • City, Country • Research interests")

col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.subheader("About")
    st.write(
        "Write a short bio here (3–6 lines). "
        "Focus on your research area, methods, and what impact your work aims to have."
    )

    st.subheader("Research focus")
    st.markdown(
        """
- **Theme 1:** (e.g., Migration & health)
- **Theme 2:** (e.g., Gendered violence & mental health)
- **Methods:** (e.g., qualitative interviews, mixed methods, epidemiology)
- **Current work:** (1–2 lines)
"""
    )

with col2:
    st.subheader("Highlights")
    st.metric("Years in research", "X")
    st.metric("Projects", "X")
    st.metric("Publications", "X")

    st.markdown("### Profiles")
    st.markdown("- ORCID: https://orcid.org/xxxx-xxxx-xxxx-xxxx")
    st.markdown("- Google Scholar: https://scholar.google.com/")
    st.markdown("- LinkedIn: https://linkedin.com/")

st.markdown("---")

# ---------- Publications ----------
st.header("Publications (selected)")
pubs = [
    {"year": 2026, "title": "Paper title here", "venue": "Journal/Conference", "link": "https://"},
    {"year": 2025, "title": "Paper title here", "venue": "Journal/Conference", "link": "https://"},
]
for p in pubs:
    link = p["link"].strip()
    if link and link != "https://":
        st.markdown(f"**{p['year']}** — {p['title']}  \n*{p['venue']}*  \n🔗 {link}")
    else:
        st.markdown(f"**{p['year']}** — {p['title']}  \n*{p['venue']}*")

st.markdown("---")

# ---------- Projects ----------
st.header("Projects")
projects = [
    {"name": "Project name", "role": "Role", "what": "1–2 lines on what it does", "status": "Ongoing"},
    {"name": "Project name", "role": "Role", "what": "1–2 lines on outcomes/outputs", "status": "Completed"},
]
for pr in projects:
    st.subheader(pr["name"])
    st.write(f"**Role:** {pr['role']}  \n**Status:** {pr['status']}")
    st.write(pr["what"])

st.markdown("---")

# ---------- Skills ----------
st.header("Skills & tools")
skills_col1, skills_col2 = st.columns(2)
with skills_col1:
    st.markdown(
        """
- Qualitative methods (interviews, thematic analysis)
- Research governance & ethics
- Data management (REDCap, codebooks)
"""
    )
with skills_col2:
    st.markdown(
        """
- R (epidemiology, analysis)
- Python (data cleaning, EDA)
- Writing & dissemination (policy briefs, papers)
"""
    )

st.markdown("---")

# ---------- Contact ----------
st.header("Contact")
st.write("Add a preferred contact method or a short note for collaborators.")
st.info("Tip: Keep personal details minimal if this is fully public.")


