import pandas as pd
import graphviz as graphviz

about_me = {'para_1' : '''Embarking on a transformative journey after completing my Bachelor's 🎓, 
            I began my professional tenure at Bharat Sanchar Nigam Ltd.💼 This pivotal experience fueled my 
            fascination with technology, setting the stage for an enriching career trajectory. 🚀''',
            
            'para_2': '''Following my tenure, I pursued a Master's degree at IIT Roorkee 🏛, a pivotal juncture that deepened my 
            passion for Data Science and its myriad applications. Equipped with this prestigious education 
            and bolstered by hands-on experience, I ventured into the vibrant realm of Machine Learning, 
            Deep Learning, and Generative AI. 🤖''',
            
            'para_3': '''My expertise spans across Natural Language Processing (NLP), Deep Learning, 
            Generative AI, Machine Learning, and Statistics 📈. I adeptly merge linguistic intricacies with 
            data-driven methodologies. With a robust foundation in statistical principles, I specialize in 
            orchestrating end-to-end Data Science projects, crafting innovative solutions that deliver measurable outcomes.            
            ''',
            
            'para_4' : '''My journey 🛤️ spans years of honing expertise across diverse projects, 
            leveraging data-driven methodologies to unearth actionable insights and craft sophisticated solutions. 
            Fueled by a relentless pursuit of excellence, I'm passionate about leveraging cutting-edge technologies 💻 to 
            tackle complex challenges head-on'''}


edu = [['B.Tech','CSE','2020','IIIT Jabalpur','8.1 CGPA'],['12th','Science','2016','Bhavan\'s KDKVM', '94.2%'],['10th','-','2012','Bhavan\'s KDKVM','10 CGPA']]

info = {'name':'Mehul Gupta', 'Brief':'Associate Data Scientist @ DBS Bank with 4+ years of professional experience looking out to solve complex business problems using AI; Experienced in developing data-driven solutions for automating digitalization of health documents reducing manual efforts by 100% for lab reports & 50% for prescriptions; Love to learn new things. Building NLP pipelines for Financial articles at DBS Bank right now !! ','photo':{'path':'abc.jpg','width':150}, 'Mobile':'8103795345','Email':'mehulgupta2016154@gmail.com','Medium':'https://medium.com/@mehulgupta_7991/about','City':'Nagda, Madhya Pradesh','Stackoverflow_flair':'''<a href="https://stackoverflow.com/users/8422170/mehul-gupta"><img src="https://stackoverflow.com/users/flair/8422170.png?theme=clean" width="250" height="70"  alt="profile for Mehul Gupta at Stack Overflow, Q&amp;A for professional and enthusiast programmers" title="profile for Mehul Gupta at Stack Overflow, Q&amp;A for professional and enthusiast programmers"></a>''','edu':pd.DataFrame(edu,columns=['Qualification','Stream','Year','Institute','Score']),'skills':['Data Science','RDBMS','Cassandra','AWS Athena','Snowflake','Comet-ML','Python','Java','C++','Airflow','AWS S3','Tableau','Metabase','Thoughtspot','Streamlit','PySpark','Tensorflow','Neo4j'],'achievements':['Top AI writer @ Medium with 100+ blogs','1.8k+ reputation points on Stackoverflow','Guest speaker, Neo4j','TCS humAIn Finalist,2019','Shikshan Bharati Kulapati K.M. Munshi Award in Mathematics,2014','Bharatiya Vidya Bhavan Shri C. Subramaniam Award for excellence in character, 2009 & 2012','Certificate of Merit(Proficiency in Co-curricular activities) for Declamation and Extempore'],'youtube_url':'https://www.youtube.com/channel/UCQoNosQTIxiMTL9C-gvFdjA','youtube_about':'https://www.youtube.com/@datascienceinyourpocket/about','publication_url':'https://medium.com/data-science-in-your-pocket/tagged/beginner'}

paper_info = {'name':['Attended RPA of prescriptions','Algorithms for rapid digitalization of prescriptions'],'publication':['Elsevier','Elsevier'],'journal':['Smart Health','Visual Informatics'],'year':['2021','2021'],'role':['Co-Author','Author'],'Summary':['The paper revolves around the Prescription/Rx digitization pipeline deployed at Tata 1mg assisting the digitizer to fasten up the entire Rx validation process by ~5 seconds/Rx. As the platform recieves ~10k Rx, this solution saves nearly 14 hours of human labour daily !!','This is about a couple of algorithms namely, C-Cube (Capture-Cluster-Clean) & 3 Step Filtering helping in unassisted digitization of prescrptions (no human support required). Regarding latencies, we found that the C-Cube and the 3-Step Filtering algorithms were 588 and 231 times faster than the brute-force approach. In terms of accuracies, we found that the F-score of the C-cube algorithm was 90% higher than the F-score of the brute-force approach whereas the F-score for the 3-Step filtering algorithm was found to be 8600% higher.'],'file':['attented_rpa_of_prescriptions.pdf','algorithms_for_rapid_digitzation_of_prescriptions.pdf'],'images':{'0':[{'path':'images/rpa1.PNG','caption':'Digitization pipeline','width':600}],'1':[[{'path':'images/pr1.PNG','caption':'Capture seed words'},{'path':'images/pr2.PNG','caption':'cluster words using seed words'},{'path':'images/pr3.PNG','caption':'clean junk words'}],[{'path':'images/hw1.PNG','caption':'Filter 1'},{'path':'images/hw2.PNG','caption':'Filter 2'},{'path':'images/hw3.PNG','caption':'Filter 3'}]]}}

models = ('Fashion MNIST samples using GAN','Cycle GAN for Image Translation')
cycle_models = ('Winter to Summer','Summer to Winter')
cycle_model_url = {cycle_models[0]:['images/winter1.jpg','images/winter2.jpg','images/winter3.jpg'],cycle_models[1]:['images/summer1.jpg','images/summer2.jpg','images/summer3.jpg']}

rpa_metrics = pd.DataFrame([['Overall',66.4, 72.5],['printed rx',54.6, 64.6],['handwritten',67.3,73.3]], columns=['category','ds','non-ds'])
rapid_metrics = pd.DataFrame([['printed',91.6,70,79.4],['handwritten',21.1,34.7,26.2],['Brute-Force_Printed',29.9,82.7,41.8],['Brute-Force_Handwritten',0.2,62,0.3]],columns=['category','precision','recall','f1_score'])
rapid_metrics = rapid_metrics.set_index(['category'])

skill_col_size = 5
embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="ravi-kumar-verma-16837734" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/ravi-kumar-verma-16837734?trk=profile-badge"></a></div>
              """}

time_line = {"high_school": "./images/st_xaviers_school.jpg"}

lottie_logo = {'python_lottie' : "https://lottie.host/5a32b015-a23a-4f30-84c8-74e6cfbf980f/WHiKigNDbr.json",
               'tensorflow_lottie' : "https://lottie.host/138e7d67-5ade-4812-ad24-b79ddcd23f89/RWKYpFiB9W.json",
               'github_lottie' : "https://lottie.host/642c77df-c98f-4112-964a-3463bdb2af41/34vCUFlp2N.json",
               'git_lottie' : "https://lottie.host/988f07f1-f3aa-4447-bbd2-1a2a73113faf/zut12hagpk.json",
               'docker_lottie' : "https://lottie.host/850ead8d-c291-4eda-a984-73ff9de8f0b7/dE76FCynQX.json",
               "mongodb_lottie" : "https://lottie.host/41b24ca0-0fb2-403e-8cdf-697cefff6b8f/81dGEy5Idn.json",
               "mysql_lottie" : "https://lottie.host/52bc7118-7f8c-42b2-bff1-c42fb1715702/yI8p5jWdJf.json",
               "rstudio_lottie" : "https://lottie.host/8f00457f-4748-481b-b4cc-5ec8f1a26b99/eYc8GRu4Oi.json",
               "lottie_gif" : "./images/hello_boy.json"
            }

badge_html =  {"Python_badge": "![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)",
               "R_badge" : "![R](https://img.shields.io/badge/r-%23276DC3.svg?style=for-the-badge&logo=r&logoColor=white)",
               "pandas_badge": "![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)",
               "numpy_badge" : "![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)",
               "sklearn_badge" : "![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)",
               "tensorflow_badge" : "![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)",
               "pytorch_badge" : "![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)",
               "keras_badge": "![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)",
               "matplotlib_badge" : "![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)",
               "plotly_bage" : "![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)",
               "mlflow_badge" : "![mlflow](https://img.shields.io/badge/mlflow-%23d9ead3.svg?style=for-the-badge&logo=numpy&logoColor=blue)",
               "chatgpt_badge" : "![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)",
               "cassandra_badge" : "![ApacheCassandra](https://img.shields.io/badge/cassandra-%231287B1.svg?style=for-the-badge&logo=apache-cassandra&logoColor=white)",
               "mongodb_badge" : "![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)",
               "musql_badge" : "![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)",
               "postgrey_badge" : "![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)",
               "sqlite_badge" : "![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)",
               "kaggle_badge" : "![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)",
               "anaconda_badge" : "![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)",
               "django_framework" : "![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)",
               "fastapi_badge" : "![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)",
               "flask_badge" : "![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)",
               "aws_badge" : "![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)",
               "heroku_badge" : "![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)",
               "atom_badge" : "![Atom](https://img.shields.io/badge/Atom-%2366595C.svg?style=for-the-badge&logo=atom&logoColor=white)",
               "jupyter_badge" : "![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)",
               "pycharm_badge" : "![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)",
               "rstudio_badge" : "![RStudio](https://img.shields.io/badge/RStudio-4285F4?style=for-the-badge&logo=rstudio&logoColor=white)",
               "spyder_badge" : "![Spyder](https://img.shields.io/badge/Spyder-838485?style=for-the-badge&logo=spyder%20ide&logoColor=maroon)",
               "sublime_badge" : "![Sublime Text](https://img.shields.io/badge/sublime_text-%23575757.svg?style=for-the-badge&logo=sublime-text&logoColor=important)",
               "vscode_badge" : "![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)",
               "markdown_badge" : "![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)",
               "bitbucket_badge" : "![Bitbucket](https://img.shields.io/badge/bitbucket-%230047B3.svg?style=for-the-badge&logo=bitbucket&logoColor=white)",
               "git_badge" : "![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)",
               "github_badge" : "![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)",
               "kubernetes_badge" : "![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)",
               "docker_badge" : "![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)",
               "jira_badge" : "![Jira](https://img.shields.io/badge/jira-%230A0FFF.svg?style=for-the-badge&logo=jira&logoColor=white)",
               "notion_badge" : "![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)",
               "postman_badge" : "![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)",
               "powerbi_badge" : "![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)",
               "jenkins_badge" : "![Jenkins](https://img.shields.io/badge/jenkins-%232C5263.svg?style=for-the-badge&logo=jenkins&logoColor=white)",
               "gcp_badge" : "![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)"
               
               }