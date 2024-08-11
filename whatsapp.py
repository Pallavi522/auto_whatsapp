import pywhatkit as kit
import streamlit as st

# Streamlit interface
st.title("WhatsApp Automation App")

# Input fields for user
phone_number = st.text_input("Recipient Phone Number (with country code)", "")
message = st.text_area("Message to Send", "")
hour = st.number_input("Hour (24-hour format)", min_value=0, max_value=23, value=0)
minute = st.number_input("Minute", min_value=0, max_value=59, value=0)

# Send WhatsApp message
if st.button("Send Message"):
    if phone_number and message:
        try:
            kit.sendwhatmsg(phone_number, message, hour, minute)
            st.success("Message scheduled successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please fill in all fields.")
