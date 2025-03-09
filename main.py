import random
import streamlit as st

st.set_page_config(page_title="🎲 Random Number Generator",layout="wide",page_icon="🎲")

# Generates random number
def generate_random_number():
    st.session_state.number = random.randint(st.session_state.min,st.session_state.max)

# Starts/Resets game
def reset_game():
    generate_random_number()
    st.session_state.response = ""
    st.session_state.attempts = 0

# On change handler for guess
def on_change_handler_guess():
    st.session_state.attempts += 1
    if st.session_state.guess < st.session_state.number:
        st.session_state.response = ":red[Too small]"
    elif st.session_state.guess > st.session_state.number:
        st.session_state.response = ":red[Too large]"
    else:
        st.session_state.response = ":green[Correct guess!]"
        
# Defaults
if "min" not in st.session_state:
    st.session_state.min = 1
    st.session_state.max = 10
    reset_game()

st.header("🎲 Random Number Generator")
st.write("Guess the number!")



# Provide input field for entering guess
st.number_input("Guess:",key="guess",on_change=on_change_handler_guess,step=1,min_value=st.session_state.min,max_value=st.session_state.max,disabled = True if st.session_state.response == ":green[Correct guess!]" else False)
if st.session_state.response:
    st.write(f"Attempts: {st.session_state.attempts}")
    st.write(st.session_state.response)
    if st.session_state.response == ":green[Correct guess!]":
        if st.button("Reset game",on_click=reset_game):
            reset_game()

# Options
st.subheader("Options",divider=True)
st.write("Range")
[col1,col3] = st.columns(2)
with col1:
    st.number_input("Minimum",key="min",step=1)
with col3:
    st.number_input("Maximum",key="max",step=1)