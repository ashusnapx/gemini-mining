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

# Input prompts
# Input prompt for mines according to DGMS rules and regulations
input_prompt_mines_dgms = """
As a dedicated professional in the field of mining, I come seeking profound insights and guidance in accordance with the rules and regulations set forth by the Directorate General of Mines Safety (DGMS). My inquiry is rooted in a commitment to uphold the highest standards of safety, efficiency, and ethical practices in mining operations.

The specific area of focus for my query relates to [insert your specific question or topic related to mines]. I kindly request you to provide a detailed and comprehensive response that encompasses the following:

1. **DGMS Guidelines and Regulations**: Delve into the specific DGMS guidelines and regulations that are relevant to [insert your specific question or topic]. Provide a thorough explanation of the key provisions and requirements set by DGMS to ensure compliance in mining activities.

2. **Safety Protocols and Best Practices**: Share insights on the safety protocols and best practices endorsed by DGMS to mitigate risks and enhance safety measures in mining operations. Elaborate on any recent updates or advancements in safety standards.

3. **Environmental Compliance**: Discuss DGMS regulations pertaining to environmental sustainability in mining. Highlight any measures or guidelines aimed at minimizing the environmental impact of mining activities.

4. **Technological Innovations**: Explore technological innovations and advancements encouraged or mandated by DGMS in the mining sector. Include information on modern tools, equipment, and practices that align with DGMS standards.

5. **Diagrams and Visual Aids**: If possible, supplement the response with relevant diagrams or visual aids that illustrate key concepts, processes, or safety measures outlined by DGMS.

In addition to the detailed response, kindly conclude with a poignant and relevant quote or principle from the field of mining that reflects the ethos of DGMS.

I express my sincere appreciation for your expertise, and I eagerly await your comprehensive insights, enriched with references, links, and any available diagrams related to my query.

Thank you in advance for your invaluable guidance.
"""

# Now, you can use this prompt in your application for the specific mining-related queries.


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
