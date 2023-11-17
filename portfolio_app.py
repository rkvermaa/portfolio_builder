import streamlit as st 
import streamlit.components.v1 as components
from constant import *
import json
from streamlit_lottie import st_lottie
import requests
from streamlit_timeline import timeline

st.set_page_config(page_title='Ravi Kumar Verma\'s portfolio' ,
                   layout="wide",
                   page_icon='🧑‍💻')

st.image('./images/banner_4.png', use_column_width=True)
# st.markdown(
#     f'<img src="./images/banner.png" width="600" height="300">',
#     unsafe_allow_html=True
# )
with st.sidebar:
    components.html(embed_component['linkedin'], height = 310)
    
# load Lottie animation from filepath
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
# Load a Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Set up Streamlit layout with two columns
col1, col2 = st.columns([3,1])


# Add content to the columns
with col1:
    # Column for text about yourself
    st.title("Ravi Kumar Verma 👋😊")
    st.header("About Me 🙋‍♂️")
    st.write(about_me['para_1'])
    st.write(about_me['para_2'])
    # You can add more text or information about yourself

st.write(about_me['para_3'])
st.write(about_me['para_4'])
    
# Load the Lottie animation file
#lottie_coding = load_lottiefile("./images/hello_boy.json")  # replace link to local lottie file
lottie_coding = load_lottiefile(lottie_logo['lottie_gif'])
with col2:
    # Column for Lottie animation
    # st.markdown("## Lottie Animation")
    st_lottie(lottie_coding,
              speed=1,
              reverse=False,
              loop=True,
              quality="low", # medium ; high
              height=300,
              width=300,
              key=None,
              )
    
# Creating time line

st.header('Timeline ⌚ ―')
with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = json.load(f)

    # Modify the data to use local file paths
    for event in data['events']:
        image_path = event['media']['file_path']        
        event['media']['url'] = image_path  # Update 'url' to refer to local path

    timeline(data, height=500)
    
# with st.spinner(text="Building line"):
#     with open('timeline.json', "r") as f:
#         data = f.read()
#         timeline(data, height=500)

# Skills 
with st.container():
    st.header('Skills & Tools 🛠️')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(load_lottieurl(lottie_logo['python_lottie']), height=125,width=125, key="python", speed=2.5)
    with col2:
        st_lottie(load_lottieurl(lottie_logo['tensorflow_lottie']), height=125,width=125, key="java", speed=2.5)
    with col3:
        st_lottie(load_lottieurl(lottie_logo['github_lottie']),height=125,width=125, key="mysql", speed=2.5)
    with col4:
        st_lottie(load_lottieurl(lottie_logo['git_lottie']),height=125,width=125, key="git", speed=2.5)
    with col1:
        st_lottie(load_lottieurl(lottie_logo['docker_lottie']),height=125,width=125, key="github", speed=2.5)
    with col2:
        st_lottie(load_lottieurl(lottie_logo['mongodb_lottie']),height=125,width=125, key="docker", speed=2.5)
    with col3:
        st_lottie(load_lottieurl(lottie_logo['mysql_lottie']),height=125,width=125, key="figma", speed=2.5)
    with col4:
        st_lottie(load_lottieurl(lottie_logo['rstudio_lottie']),height=125,width=125, key="js", speed=2.5)
        
        
badge_html = '''
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)](https://pytorch.org/)
'''

st.markdown(badge_html, unsafe_allow_html=True)
