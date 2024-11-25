import streamlit as st
import time
import pytz
from datetime import datetime
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="MK316 Customized Timer", layout="centered")

# Initialize session state for countdown
if "countdown_started" not in st.session_state:
    st.session_state.countdown_started = False
if "start_time" not in st.session_state:
    st.session_state.start_time = 0
if "remaining_time" not in st.session_state:
    st.session_state.remaining_time = 0
if "time_up" not in st.session_state:
    st.session_state.time_up = False

# Title
st.title("🐧 MK316 Customized Timer ")

# Function to display the current time (as a live digital clock)
def display_current_time(current_time_placeholder):
    seoul_tz = pytz.timezone('Asia/Seoul')  # Set timezone to Seoul
    current_time = datetime.now(seoul_tz).strftime("%H:%M:%S")  # Convert to Seoul time
    
    # Style the clock (increase font size and set color)
    current_time_placeholder.markdown(
        f"<h2 style='text-align: center; font-size: 60px; color: #5785A4;'>{current_time}</h1>",  # Large font
        unsafe_allow_html=True
    )

# Function to update the progress circle
def update_progress_circle(remaining_time, total_time, time_up=False):
    fig, ax = plt.subplots(figsize=(2, 2))  # Smaller figure size to fit layout
    
    if time_up:
        # Show "Time's Up!" in the center of the circle
        ax.pie([1], colors=['#6d8c9c'], startangle=90, counterclock=False, wedgeprops=dict(width=0.15))
        ax.text(0, 0, "Time's Up!", fontsize=12, va='center', ha='center', color="gray")  # "Time's Up!" message inside the circle
    else:
        # Calculate the proportion of remaining time
        fraction_completed = remaining_time / total_time if total_time > 0 else 0
        ax.pie([fraction_completed, 1 - fraction_completed], colors=['#5785A4', '#D5DEDD'], startangle=90, counterclock=False, wedgeprops=dict(width=0.3))
        
        # Format and add remaining time as text in the center of the circle
        minutes, seconds = divmod(remaining_time, 60)
        ax.text(0, 0, f"{int(minutes):02d}:{int(seconds):02d}", fontsize=12, va='center', ha='center')  # Remaining time
    
    ax.set_aspect('equal')
    return fig

# Function to start the countdown timer
def start_countdown():
    if not st.session_state.countdown_started:
        st.session_state.remaining_time = st.session_state.start_time
        st.session_state.countdown_started = True
        st.session_state.time_up = False

# Function to reset the countdown timer
def reset_countdown():
    st.session_state.start_time = 0
    st.session_state.remaining_time = 0
    st.session_state.countdown_started = False
    st.session_state.time_up = False

# Input field for countdown time in seconds
st.session_state.start_time = st.number_input("Set Countdown Time (in seconds)", min_value=0, max_value=7200, value=10)

# Two columns: one for current time and buttons, another for circular progress
col1, col2 = st.columns([2, 1])

# Left column: Current time, input, buttons
with col1:
    # Placeholder to display the current time
    current_time_placeholder = st.empty()
    
    # Buttons to Start and Reset the countdown
    start_button, reset_button = st.columns([1, 1])
    with start_button:
        if st.button("Start"):
            start_countdown()
    with reset_button:
        if st.button("Reset"):
            reset_countdown()

    # Placeholder for displaying countdown text message
    countdown_placeholder = st.empty()

# Right column: Circular progress chart
with col2:
    progress_placeholder = st.empty()

# Timer countdown loop (only runs when countdown has started)
if st.session_state.countdown_started and not st.session_state.time_up:
    while st.session_state.remaining_time > 0:
        # Display the circular progress chart with time in the center
        fig = update_progress_circle(st.session_state.remaining_time, st.session_state.start_time)
        progress_placeholder.pyplot(fig)

        # Display countdown time
        minutes, seconds = divmod(st.session_state.remaining_time, 60)
        countdown_placeholder.write(f"**Remaining Time:** {int(minutes):02d}:{int(seconds):02d}")
        
        # Update the remaining time
        st.session_state.remaining_time -= 1
        
        # Sleep for a second
        time.sleep(1)

        # Update current time in the placeholder
        display_current_time(current_time_placeholder)
        
    # When the countdown finishes
    st.session_state.time_up = True
    fig = update_progress_circle(0, st.session_state.start_time, time_up=True)  # Add "Time's Up!" message
    progress_placeholder.pyplot(fig)
    # countdown_placeholder.write("⏰ **Time's Up!**")

    # Play the sound using Streamlit's audio player
    audio_file = open("timesup.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")

    st.session_state.countdown_started = False
