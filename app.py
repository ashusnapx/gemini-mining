import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Step 1: Load environment variables
load_dotenv()

# Step 2: Configure Google Gemini Pro model
genai.configure(api_key=os.getenv('GOOGLE_GEMINI_KEY'))
model = genai.GenerativeModel('gemini-pro')

# Step 3: Define the role of Gemini Pro
def role_to_streamlit(role, response_text):
    return f'{role.capitalize()}: {response_text}'

# Function to get Gemini responses
def get_gemini_responses(input_prompt, user_input):
    response = model.generate_content([user_input, input_prompt])
    return response.text

# Step 4: Ask the application to store the context of chat
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Step 5: Set up the frontend
st.set_page_config(page_title='DGMS Gemini Guru', page_icon="🚜", layout="wide")
st.title('OneStop Solution For Your Coal Mines Queries 🚜')

# Job description input area
job_description = st.text_area('Pen down your problems:', key='input')

# Buttons
variant1 = st.button('Solution according to DGMS')

# Updated prompt for mining-related queries according to DGMS and CMR 2017 rules and regulations
input_prompt_mines_dgms = """
Seeking guidance in mining operations according to DGMS rules and Coal Mines Regulations (CMR) 2017, I request concise insights into the following:

- **DGMS Guidelines and CMR 2017 Regulations**:
   - Provide key provisions and requirements relevant to [insert specific question or topic].
   - Reference the rule numbers and sections for detailed information.

- **Safety Protocols and Best Practices**:
   - Share concise insights on safety protocols endorsed by DGMS and CMR 2017.
   - Highlight recent updates or advancements in safety standards.
   - Include references to the specific guidelines.

- **Environmental Compliance**:
   - Discuss DGMS and CMR 2017 regulations focusing on environmental sustainability in mining.
   - Highlight key measures for minimizing environmental impact.
   - Include references to relevant environmental compliance guidelines.

- **Technological Innovations**:
   - Explore brief details of technological innovations encouraged by DGMS and CMR 2017.
   - Include information on modern tools, equipment, and practices.
   - Provide references to DGMS and CMR 2017 mandates supporting these innovations.

- **Diagrams and Visual Aids**:
   - If possible, include concise diagrams illustrating key concepts or safety measures.
   - Reference the specific sections or guidelines in DGMS and CMR 2017 related to the visuals.

Conclude the response with a relevant mining quote and express gratitude for the valuable guidance.

I appreciate your expertise and await your concise insights, enriched with rule references, links, and any relevant visuals.

Thank you for your invaluable assistance.
"""


# Button actions
if variant1:
    with st.spinner('Fetching response...'):
        response = get_gemini_responses(input_prompt_mines_dgms, job_description)
    st.subheader('Solution acc. to DGMS :')
    st.write(response)

# Footer
footer = """
<hr style="border:0.5px solid #808080">
<div style="display: flex; justify-content: space-between; align-items: center; padding-top: 10px; padding-bottom: 10px;">
    <div>
         <a href="https://ashusnapx.vercel.app/" target="_blank" style="font-size: 12px; text-decoration: none; color: #1DA1F2;">Ashutosh Kumar</a><br>
        <span style="font-size: 12px;">Software Developer</span>
    </div>
    <div>
        <a href="https://twitter.com/ashusnapx" target="_blank" style="font-size: 12px; text-decoration: none; color: #1DA1F2;">Twitter</a><br>
        <a href="https://www.linkedin.com/in/ashusnapx" target="_blank" style="font-size: 12px; text-decoration: none; color: #0077B5;">LinkedIn</a>
    </div>
</div>
"""

# Add footer to the page
st.markdown(footer, unsafe_allow_html=True)
