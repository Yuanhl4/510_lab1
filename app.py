import streamlit as st

# Set page config to add a title and favicon
st.set_page_config(page_title="YH's Portfolio", page_icon=":smiley:")

# Use columns to layout the intro section
col1, col2 = st.columns(2)
with col1:
    st.header("Hello, I'm YH!")
    st.write("510 Example")

# Projects Section
st.write("---")
st.subheader("Project")
with st.expander("510's lab"):
    st.write("""
        **Project Name**: 510_lab1
        **Description**: Example 
        **Technologies Used**: Python, Streamlit
        **GitHub Link**: [Visit GitHub](https://github.com/Yuanhl4/510_lab1)  
    """)

# Contact Section
st.write("---")
st.subheader("Contact Me")
contact_form = """
<form action="https://formsubmit.co/your_email_here" method="POST">
    <input type='text' name='name' placeholder='Your name' required>
    <input type='email' name='email' placeholder='Your email' required>
    <button type='submit'>Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Footer
st.write("---")
