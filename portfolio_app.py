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

# # Skills 
# with st.container():
#     st.header('Skills & Tools 🛠️')
#     col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
#     with col1:
#         st_lottie(load_lottieurl(lottie_logo['python_lottie']), height=125,width=125, key="python", speed=2.5)
#     with col2:
#         st_lottie(load_lottieurl(lottie_logo['tensorflow_lottie']), height=125,width=125, key="java", speed=2.5)
#     with col3:
#         st_lottie(load_lottieurl(lottie_logo['github_lottie']),height=125,width=125, key="mysql", speed=2.5)
#     with col4:
#         st_lottie(load_lottieurl(lottie_logo['git_lottie']),height=125,width=125, key="git", speed=2.5)
#     with col1:
#         st_lottie(load_lottieurl(lottie_logo['docker_lottie']),height=125,width=125, key="github", speed=2.5)
#     with col2:
#         st_lottie(load_lottieurl(lottie_logo['mongodb_lottie']),height=125,width=125, key="docker", speed=2.5)
#     with col3:
#         st_lottie(load_lottieurl(lottie_logo['mysql_lottie']),height=125,width=125, key="figma", speed=2.5)
#     with col4:
#         st_lottie(load_lottieurl(lottie_logo['rstudio_lottie']),height=125,width=125, key="js", speed=2.5)
        
# Skills      
# with st.container():
#     st.header('Skills & Tools 🛠️')
#     col1, col2, col3, col4, col5, col6, col7, col8= st.columns([1, 1, 1, 1, 1, 1 ,1 ,1])
    
#     ## 1st row
#     with col1:
#         st.markdown(badge_html['Python_badge'], unsafe_allow_html=True)
#     with col2:
#         st.markdown(badge_html['R_badge'], unsafe_allow_html=True)
#     with col3:
#         st.markdown(badge_html['pandas_badge'], unsafe_allow_html=True)
#     with col4:
#         st.markdown(badge_html['numpy_badge'], unsafe_allow_html=True)
#     with col5:
#         st.markdown(badge_html['sklearn_badge'], unsafe_allow_html=True)
#     with col6:
#         st.markdown(badge_html['tensorflow_badge'], unsafe_allow_html=True)
#     with col7:
#         st.markdown(badge_html['pytorch_badge'], unsafe_allow_html=True)
#     with col8:
#         st.markdown(badge_html['keras_badge'], unsafe_allow_html=True)
        
#     ## 2nd row
#     with col1:
#         st.markdown(badge_html['matplotlib_badge'], unsafe_allow_html=True)
#     with col2:
#         st.markdown(badge_html['plotly_bage'], unsafe_allow_html=True)
#     with col3:
#         st.markdown(badge_html['mlflow_badge'], unsafe_allow_html=True)
#     with col4:
#         st.markdown(badge_html['cassandra_badge'], unsafe_allow_html=True)
#     with col5:
#         st.markdown(badge_html['mongodb_badge'], unsafe_allow_html=True)
#     with col6:
#         st.markdown(badge_html['musql_badge'], unsafe_allow_html=True)
#     with col7:
#         st.markdown(badge_html['postgrey_badge'], unsafe_allow_html=True)
#     with col8:
#         st.markdown(badge_html['chatgpt_badge'], unsafe_allow_html=True)
    
        
#     ## 3rd row
#     with col1:
#         st.markdown(badge_html['fastapi_badge'], unsafe_allow_html=True)
#     with col2:
#         st.markdown(badge_html['flask_badge'], unsafe_allow_html=True)
#     with col3:
#         st.markdown(badge_html['aws_badge'], unsafe_allow_html=True)
#     with col4:
#         st.markdown(badge_html['heroku_badge'], unsafe_allow_html=True)
#     with col5:
#         st.markdown(badge_html['atom_badge'], unsafe_allow_html=True)
#     with col6:
#         st.markdown(badge_html['jupyter_badge'], unsafe_allow_html=True)
#     with col7:
#         st.markdown(badge_html['anaconda_badge'], unsafe_allow_html=True)
#     with col8:
#         st.markdown(badge_html['pycharm_badge'], unsafe_allow_html=True)
        
#     ## 4th row
#     with col1:
#         st.markdown(badge_html['rstudio_badge'], unsafe_allow_html=True)
#     with col2:
#         st.markdown(badge_html['spyder_badge'], unsafe_allow_html=True)
#     with col3:
#         st.markdown(badge_html['gcp_badge'], unsafe_allow_html=True)
#     with col4:
#         st.markdown(badge_html['sublime_badge'], unsafe_allow_html=True)
#     with col5:
#         st.markdown(badge_html['vscode_badge'], unsafe_allow_html=True)
#     with col6:
#         st.markdown(badge_html['markdown_badge'], unsafe_allow_html=True)
#     with col7:
#         st.markdown(badge_html['bitbucket_badge'], unsafe_allow_html=True)
#     with col8:
#         st.markdown(badge_html['git_badge'], unsafe_allow_html=True)
        
#     ## 5th row
#     with col1:
#         st.markdown(badge_html['github_badge'], unsafe_allow_html=True)
#     with col2:
#         st.markdown(badge_html['kubernetes_badge'], unsafe_allow_html=True)
#     with col3:
#         st.markdown(badge_html['docker_badge'], unsafe_allow_html=True)
#     with col4:
#         st.markdown(badge_html['jira_badge'], unsafe_allow_html=True)
#     with col5:
#         st.markdown(badge_html['notion_badge'], unsafe_allow_html=True)
#     with col6:
#         st.markdown(badge_html['postman_badge'], unsafe_allow_html=True)
#     with col7:
#         st.markdown(badge_html['powerbi_badge'], unsafe_allow_html=True)
#     with col8:
#         st.markdown(badge_html['jenkins_badge'], unsafe_allow_html=True)
 
 
# Skills 
# Initialize a list to store sublists
all_lists = []

# Create sublists of 8 keys each
keys_list = list(badge_html.keys())  # Get all keys from the dictionary
num_keys = len(keys_list)

for i in range(0, num_keys, 8):
    sublist = keys_list[i:i+8]  # Slice 8 keys at a time
    all_lists.append(sublist)   # Add sublist to the main list
 
with st.container():
    st.header('Skills & Tools 🛠️')
    
    for row in all_lists:
        cols = st.columns(len(row))
        for col_num, col_name in enumerate(row):
            with cols[col_num]:
                st.markdown(badge_html[col_name], unsafe_allow_html=True)

