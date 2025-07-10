# import streamlit as st

# st.header("Business Assistant")

# question = st.text_input("Type your question below:")

# info = {
#     "working_hours": "Our working hours are 24/7",
#     "address_of_building": "We are located at Uztelecom",
#     "location_of_building": "Our office is at Uztelecom",
#     "contact_info": "+998 90 788-66-80",
#     "mobile": "+998 90 788-66-80",
#     "gmail_address": "sanjar.meb@gmail.com",
# }

# reply = "Not legal cuestion !!!"

# if question:
#     lower_q = question.lower()
#     for keyword in info:
#         if keyword in lower_q:
#             reply = info[keyword]
#             break
#     st.success(reply)

import streamlit as st

st.header("Business Assistant")

question = st.text_input("Type your question below:")

info = {
    "Working hours": "Our working hours are 24/7",
    "Address of building": "We are located in Mukimi Street, Mirzo Ulugbek District, Tashkent, Uzbekistan",
    "Location of building": "Our office is on Mukimi Street, Mirzo Ulugbek District, Tashkent, Uzbekistan",
    "Contact info": "+998 90 788-66-80",
    "Mobile": "+998 90 788-66-80",
    "Email address": "sanjar.meb@gmail.com",
}

default_reply = "Try to ask another question"

def get_reply(user_input: str) -> str:
    user_input = user_input.lower()
    for keyword, response in info.items():
        if keyword in user_input:
            return response
    return default_reply

if question:
    response = get_reply(question)
    st.success(response)