import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

st.set_page_config(layout="wide")
title = "The best company"
st.header(title)
content = """
Proin vel condimentum est. Sed aliquet auctor enim in luctus. Donec id vestibulum odio, ut efficitur quam. 
Curabitur ac justo aliquam, faucibus mi sit amet, hendrerit metus. Mauris vestibulum magna ut sem tempus ultricies. 
Donec lobortis, turpis vel interdum malesuada, augue quam aliquet lectus, in egestas massa lacus a felis. 
Aliquam ut dui suscipit, congue magna ut, aliquet ipsum. Mauris venenatis ut purus eget feugiat. Praesent viverra 
enim in viverra varius. Phasellus euismod ac velit at pharetra.
"""
st.write(content)
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")


with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")