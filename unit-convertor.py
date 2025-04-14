import streamlit as st

st.title("Unit Converter")
st.markdown("### Converts Length, Weight And Time Instantly")
st.write("# Welcome! Select a category, enter the value and get the converted result")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Select unit conversion options based on category
if category == "Length":
    unit = st.selectbox("Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select Conversion", [
        "Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours",
        "Hours to Minutes", "Hours to Days", "Days to Hours"
    ])

value = st.number_input("Enter the value", min_value=0.0, format="%.2f")

def converter_unit(category, unit, value):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

# Show the result after clicking button
if st.button("Convert"):
    result = converter_unit(category, unit, value)
    st.success(f"Converted Value: {result:.2f}")
