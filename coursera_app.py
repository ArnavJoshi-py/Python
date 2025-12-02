import streamlit as st

# Page config
st.set_page_config(page_title="Coursera Demo", layout="wide")

# Header
st.title("Coursera Demo Website")
st.write("Learn skills online with online courses, certificates, and degrees.")

# Search bar
query = st.text_input("🔍 Search for courses", "")
if query:
    st.write(f"Showing results for: **{query}**")

st.markdown("---")

# Featured courses section
st.header("Featured Courses")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Python for Everybody")
    st.write("University of Michigan")
    st.button("Enroll Now", key="python")

with col2:
    st.subheader("Machine Learning")
    st.write("Stanford University")
    st.button("Enroll Now", key="ml")

with col3:
    st.subheader("Google Data Analytics")
    st.write("Google")
    st.button("Enroll Now", key="gda")

st.markdown("---")

# Explore categories
st.header("Browse Categories")

categories = [
    "Data Science", "Business", "Computer Science",
    "Personal Development", "Arts & Humanities"
]

selected = st.selectbox("Choose a category", categories)
st.write(f"You selected: **{selected}**")

st.markdown("---")

# Footer
st.write("© 2025 Coursera Demo • Built with Streamlit")
