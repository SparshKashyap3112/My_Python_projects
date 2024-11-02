import streamlit as st

st.title("Py.PASSWORD")
st.header("Welcome to \"PyPasswod\" Generator")
import streamlit as st
import random
import string

# User inputs
l = st.slider("Select password length", min_value=3, max_value=50, value=12)
upper = st.checkbox("Include Uppercase Letters") 
numbers = st.checkbox("Include Numbers")
special = st.checkbox("Include Special Characters")

# Function to generate password
def generate_password(l, upper, numbers, special):
    characters = string.ascii_lowercase
    if upper:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(l))
    return password

# Generate password button
if st.button("Generate Password"):
    if not (upper or numbers or special):
        st.error("Please select at least one character type!")
    else:
        password = generate_password(l, upper, numbers, special)
        st.success(f"Generated Password: {password}")

# Run the app
if __name__ == "__main__":
    st.write("Customize your password options and click 'Generate Password'.")

# streamlit run filename.py
