import streamlit as st

def convert_units(value, unit_from, unit_to):
    convertions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
        
    }

    key = f"{unit_from}_{unit_to}"

    if key in convertions:
        convertion = convertions[key]
        return value * convertion
    else:
        return"Convertion not supported"
    
st.title("Unit Convertor")

value = st.number_input("Enterthe value:", min_value=1.0, step=1.0)

unit_from = st.selectbox("Convert from:",["meter", "kilometer", "gram","kilogram"])
unit_to = st.selectbox("Convert to:",["meter", "kilometer", "gram","kilogram"])

if st.button("Convert"):
    result = convert_units(value , unit_from, unit_to)
    st.write(f"Converted value: {result}")