




# # from django.shortcuts import render
# # import os
# # import openai

# # # Create your views here.

# # def fun():
# #   openai.api_key ="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"

# #   response = openai.Completion.create(
# #     model="text-davinci-003",
# #     prompt=f"Govardhana K Senior Software Engineer  Bengaluru, Karnataka, Karnataka - Email me on Indeed: indeed.com/r/Govardhana-K/ b2de315d95905b68  Total IT experience 5 Years 6 Months Cloud Lending Solutions INC 4 Month \\u2022 Salesforce Developer Oracle 5 Years 2 Month \\u2022 Core Java Developer Languages Core Java, Go Lang Oracle PL-SQL programming, Sales Force Developer with APEX.  Designations & Promotions  Willing to relocate: Anywhere  WORK EXPERIENCE  Senior Software Engineer  Cloud Lending Solutions -  Bangalore, Karnataka -  January 2018 to Present  Present  Senior Consultant  Oracle -  Bangalore, Karnataka -  November 2016 to December 2017  Staff Consultant  Oracle -  Bangalore, Karnataka -  January 2014 to October 2016  Associate Consultant  Oracle -  Bangalore, Karnataka -  November 2012 to December 2013  EDUCATION  B.E in Computer Science Engineering  Adithya Institute of Technology -  Tamil Nadu  September 2008 to June 2012  https://www.indeed.com/r/Govardhana-K/b2de315d95905b68?isid=rex-download&ikw=download-top&co=IN https://www.indeed.com/r/Govardhana-K/b2de315d95905b68?isid=rex-download&ikw=download-top&co=IN   SKILLS  APEX. (Less than 1 year), Data Structures (3 years), FLEXCUBE (5 years), Oracle (5 years), Algorithms (3 years)  LINKS  https://www.linkedin.com/in/govardhana-k-61024944/  ADDITIONAL INFORMATION  Technical Proficiency:  Languages: Core Java, Go Lang, Data Structures & Algorithms, Oracle PL-SQL programming, Sales Force with APEX. Tools: RADTool, Jdeveloper, NetBeans, Eclipse, SQL developer, PL/SQL Developer, WinSCP, Putty Web Technologies: JavaScript, XML, HTML, Webservice  Operating Systems: Linux, Windows Version control system SVN & Git-Hub Databases: Oracle Middleware: Web logic, OC4J Product FLEXCUBE: Oracle FLEXCUBE Versions 10.x, 11.x and 12.x  https://www.linkedin.com/in/govardhana-k-61024944/\n\nextract name, skills, location, email address, companies worked at, Degree, graduation year, designation, phone, college, and year of experience\n\n\nName: Govardhana K\nSkills: Core Java, Go Lang, Data Structures & Algorithms, Oracle PL-SQL programming, Sales Force with APEX.,RADTool, Jdeveloper, NetBeans, Eclipse, SQL developer, PL/SQL Developer, WinSCP, Putty, JavaScript, XML, HTML, Webservice\nLocation: Bengaluru, Karnataka, Karnataka\nEmail address: indeed.com/r/Govardhana-K/b2de315d95905b68\nCompanies worked at: Cloud Lending Solutions INC, Oracle\nDegree: B.E in Computer Science Engineering\nGraduation year: June 2012\nDesignation: Senior Software Engineer\nPhone: N/A\nCollege: Adithya Institute of Technology\nYear of experience: 5 Years 6 Months\n\n{var}\n\nextract name, skills, location, email address, companies worked at, Degree, graduation year, designation, phone, college, and year of experience",
# #     temperature=0.7,
# #     max_tokens=256,
# #     top_p=1,
# #     frequency_penalty=0,
# #     presence_penalty=0
# #   )

# from django.shortcuts import render
# import os
# import openai
# import PyPDF2

# # Create your views here.
from django.shortcuts import render
import pdfplumber
import sys
sys.path.append('Text-Analytics')
from .credential import client
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# def skill_matcher(set1, set2):
def skill_matcher(resume_skill, skill_list):
    vectorizer = TfidfVectorizer()
    user_feature_matrix = vectorizer.fit_transform(resume_skill)
    job_feature_matrix = vectorizer.transform(skill_list)
    # Get feature names for user and job feature matrices
    user_feature_names = vectorizer.get_feature_names_out()
    job_feature_names = vectorizer.get_feature_names_out()
    # Find matching words
    matching_words = []
    non_matching_words = []
    for score in cosine_similarity(job_feature_matrix, user_feature_matrix):
        for i,j in enumerate(score):
            if j>0:
                matching_words.append(resume_skill[i])   
    return list(set(matching_words))


# # Create your views here.

def extract_resume_data(file_path, a):
    with pdfplumber.open(file_path) as pdf_file:
        resume_text = ''
        for page in pdf_file.pages:
            resume_text += page.extract_text()

    client = a
    
    # Split the resume text into smaller chunks
    text_chunks = [resume_text[i:i+5120] for i in range(0, len(resume_text), 5120)]
    
    new_list = []
    
    for chunk in text_chunks:
        response = client.recognize_entities(documents=[chunk])
    
        for index, result in enumerate(response):
            for entity in result.entities:
                if entity.category == 'Skill' or entity.category == 'Product':
                    new_list.append(entity.text)
    
    return new_list


def extract_resume_data(file_path, a):
    with pdfplumber.open(file_path) as pdf_file:
        resume_text = ''
        for page in pdf_file.pages:
            resume_text += page.extract_text()
    client = a

    text_chunks = [resume_text[i:i+5120] for i in range(0, len(resume_text), 5120)]

    response = client.recognize_entities(documents=[resume_text])
    new_list=[]

    for chunk in text_chunks:
        response = client.recognize_entities(documents=[chunk])

        for index,result in enumerate(response):
            for entity in result.entities:
                if entity.category=='Skill' or entity.category=='Product':
                    # print('Entity text: {0}'.format(entity.text))
                    new_list.append(entity.text)
                else:
                    pass
    new_list = list(set([i.title() for i in new_list]))
    # print
    return skill_matcher(new_list,lis)



def index(request):
    if request.method == 'POST':
        # Get the file from the request
        uploaded_file = request.FILES['pdf_file']
        text_file = request.POST.get('text_file', '')
        # Write the file to the server
        with open('uploaded_resume.pdf', 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        # Extract data from the resume
        resume_data = extract_resume_data('uploaded_resume.pdf',client())
        print(resume_data)

        jd_skill = extract_JD_Skil(text_file)

        dic_all = similiarity_score(resume_data, jd_skill)
        
        # Render the output page with the extracted data
        
        return render(request, 'output.html', {'resume_data': resume_data, 'jd_skill':jd_skill,'dic_all' : dic_all})
    else:
        return render(request, 'index.html')



jd = '''
we required skill python, Tableau,machine learning, sql, power BI, statistics,Flask,VBA,web scraping,
'project management
'
'''
def extract_JD_Skil(jd):
    skills = []
    response = client().recognize_entities(documents= [jd], language="en")
    skill_categories = ['Product', 'Skill']
    for index,result in enumerate(response):
        for entity in result.entities:
            if entity.category in skill_categories:
                skills.append(entity.text)
    skills = list(set([i.title() for i in skills]))
    print(skills)
    skills = skill_matcher(list(set(skills)),lis)
    return skills

### similarity

def similiarity_score(resume_skill, required_skill):
    if len(resume_skill)>len(required_skill):
        big = resume_skill
        small = required_skill
    else:
        big = required_skill
        small = resume_skill
    vectorizer = TfidfVectorizer()
    user_feature_matrix = vectorizer.fit_transform(big)
    job_feature_matrix = vectorizer.transform(small)
    # Get feature names for user and job feature matrices
    user_feature_names = vectorizer.get_feature_names_out()
    job_feature_names = vectorizer.get_feature_names_out()
    # Find matching words
    matching_words = []
    non_matching_words = []
    for score in cosine_similarity(job_feature_matrix, user_feature_matrix):
        for i,j in enumerate(score):
            if j>0:
                matching_words.append(big[i])
    for i in required_skill:
        if i not in matching_words:
            non_matching_words.append(i)    
    len_skills = len(required_skill)
    score = (len(set(matching_words))/len_skills)*100

    ##remove
    new=[]
    for i in range(len(matching_words)):
        for j in matching_words[i+1:]:
            if matching_words[i]+' '+j  in matching_words:
                print('yes')
            elif ' '.join((matching_words[i]+' '+j).split()[::-1]) in matching_words:
                print('yes-2')
                new.append(' '.join((matching_words[i]+' '+j).split()[::-1]))
                
    for i in new:
        for j in i.split():
            matching_words.remove(j) 
            

    dic_all={
        "matching_words":matching_words,
        "non_matching_words":non_matching_words,
        "score":score
    }
    return dic_all
#     if (len(set(matching_words))/len_skills)*100>100:
#         for i,j in enumerate(score):
#             if j>0.9:
#                 matching_words.append(big[i])
#         len_skills = len(required_skill)
#         print("matching skill is :" , set(matching_words))
#         return (len(set(matching_words))/len_skills)*100
#     else:
#         for i,j in enumerate(score):
#             if j>0:
#                 matching_words.append(big[i])
#         len_skills = len(required_skill)
#         print("matching skill is :" ,set(matching_words))
#         return (len(set(matching_words))/len_skills)*100


 






























  
lis = ['Java' ,'Python', 'JavaScript', 'C++', 'C#', 'PHP' ,'Ruby' ,'Swift','Objective-C','Kotlin','TypeScript'
,'SQL','R','MATLAB','Go','Rust','Dart','Lua','Scala','Haskell',"Assembly language", "Visual Basic", "Perl",
 "Cobol", "Fortran", "Lisp", "Prolog", "Ada", "Julia", "Shell script", "Smalltalk", "Tcl", "Groovy", 
 "PowerShell", "Erlang", "F#", "Clojure", "Dart", "Crystal", "Elixir", "Assembly language",   
 "Visual Basic",    "Perl",    "Cobol",    "Fortran",    "Lisp",    "Prolog",    "Ada",    
 "Julia",    "Shell script",    "Smalltalk",    "Tcl",    "Groovy",    "PowerShell",    "Erlang",    
 "F#",    "Clojure",    "Dart",    "Crystal",    "Elixir","Scheme",    "OCaml",    "COQ",    "Idris",
 "Elm",    "ReasonML",    "Dart",    "Kotlin",    "PureScript",    "Crystal",    "Zig",    "Groovy", 
 "Hack",    "CoffeeScript",    "TypeScript",    "JSX",    "Eiffel",    "Groovy",    "LiveScript",   
 "Perl 6", '.NET',  'Node.js',"HTML",    "CSS",    "JavaScript",    "React",    "Angular",    
 "Node.js",    "jQuery",    "Bootstrap",    "Vue.js",    "Django",    "Ruby on Rails",    
 "Express.js",    "Laravel",    "Flask",    "ASP.NET",    "MongoDB",    "MySQL",    "PostgreSQL",    
 "Firebase",    "AWS","Python",    "Java",    "JavaScript",    "C#",    "C++",    "PHP",    
 "Swift",    "Objective-C",    "Kotlin",    "React Native",    "Flutter",    "HTML",    "CSS",   
 "Dart", "Tableau",    "Microsoft Power BI",    "QlikView",    "IBM Cognos Analytics",    
"SAP Lumira",    "TIBCO Spotfire",    "MicroStrategy",    "SAS Visual Analytics",  
"Google Data Studio",    "Oracle Business Intelligence",    "Domo",    "Klipfolio",    "Looker",  
"Sisense",    "Zoho Analytics",    "Chartio",    "Plotly",    "Adobe Analytics",    "Pentaho",  
"Yellowfin", "SAS","Google Sheets",    "LibreOffice Calc",    "Apache OpenOffice Calc",    
"Zoho Sheet",    "Gnumeric",    "OnlyOffice",    "Apple Numbers",    "EtherCalc",    
"FreeOffice PlanMaker",    "Hancom Office Sheet",    "WPS Office Spreadsheets",    "Airtable",   
"Smartsheet",    "CalcTape",    "Quip Spreadsheets",    "EditGrid",    "Coda",    "Datawrapper",    
"Sheetgo",    "Hadoop Office","Amazon Web Services (AWS)",    "Microsoft Azure",    
"Google Cloud Platform",    "IBM Cloud",    "Oracle Cloud",    "Alibaba Cloud",    "Salesforce",  
"Rackspace",    "VMware Cloud",    "DigitalOcean",    "Red Hat OpenShift",    "Heroku",    
"Cloudflare",    "Dropbox",    "Box",    "Adobe Creative Cloud",    "Slack",    "Zoom",    
"Twilio",    "Atlassian","Cisco Cloud",    "Dell Cloud",    "Hewlett Packard Enterprise Cloud",    
 "Nutanix Cloud",    "SAP Cloud Platform",    "ServiceNow Cloud",    "Workday Cloud",    
 "Citrix Cloud",    "CenturyLink Cloud",    "Joyent Cloud",    "OVHcloud",    "Digital Realty Cloud",   
 "Fujitsu Cloud",    "NEC Cloud",    "NTT Cloud","Windows",    "macOS",    "Linux",    "Android",   
 "iOS",    "Chrome OS",    "Unix",  "Solaris",  "FreeBSD",    "OpenBSD",    "NetBSD",    
 "CentOS",    "Ubuntu",    "Fedora",  "Debian", "Red Hat Enterprise Linux",    "Oracle Linux",
 "SUSE Linux Enterprise",    "IBM AIX",    "HP-UX",    "z/OS",    "Android TV",    "Apple TV OS",  
 "watchOS",    "tvOS",    "Chromebook OS",    "Android Wear OS",    "Tizen",    "QNX",    
 "BlackBerry OS",    "Palm OS",    "MS-DOS",    "FreeDOS",    "Windows Server",    
 "Windows Phone OS",    "Windows Embedded",    "BeOS",    "Haiku",    "ReactOS",    "AmigaOS",    
 "Atari TOS",    "CP/M",    "RT-11",    "VMS",    "OS/2",    "OpenVMS",    "Inferno",    "Plan 9", 
 "MINIX",    "MVS",'Programming languages', 'Mathematics', 'Machine Learning algorithms', 
 'Data preprocessing', 'Deep learning algorithms', 'Natural Language Processing', 'Computer Vision',
 'Neural networks', 'Big Data tools', 'Cloud computing', 'Data visualization', 'Model deployment', 
 'Transfer Learning', 'Hyperparameter tuning', 'Ensemble learning', 'Time series forecasting', 
 'Reinforcement learning', 'Image processing', 'Audio processing', 'Speech recognition', 
 'Chatbot development', 'Generative models', 'Optimization techniques', 'Bayesian Statistics', 
 'Decision Trees', 'Support Vector Machines', 'k-Nearest Neighbors', 'Random Forests', 
 'Naive Bayes', 'Logistic Regression', 'Artificial Neural Networks', 'Convolutional Neural Networks', 
 'Recurrent Neural Networks', 'Long Short-Term Memory networks', 'Autoencoders',  'Unsupervised learning algorithms',
 'Dimensionality reduction techniques', 'Recommender systems', 'Collaborative filtering', 
 'Time series analysis', 'Statistical learning', 'Data augmentation', 'Data validation', 
 'Data transformation', 'Natural Language Generation', 'Explainable AI', 'Edge computing', 
 'Federated Learning', 'Cognitive Computing', 'Digital Twin technology', 'GCP', 'AWS','TensorFlow', 
 'PyTorch', 'Keras', 'Caffe', 'Theano', 'MXNet', 'Chainer', 'Scikit-learn', 'H2O', 'DeepLearning4J', 
 'Accord.NET', 'Apache Mahout', 'Torch', 'TensorFlow.js', 'ONNX', 'Microsoft Cognitive Toolkit (CNTK)',
 'Gluon', 'PyBrain', 'Lasagne', 'Neuroph', 'Brainstorm', 'TensorFlow Probability', 'TFLearn', 'Weka',
 'RapidMiner', 'OpenCV', 'Spark MLlib', 'Mxnet-GluonCV', 'CNTK', 'DIGITS','Amazon Web Services (AWS)',
'Microsoft Azure', 'Google Cloud Platform (GCP)', 'IBM Cloud', 'Red Hat OpenShift', 'Docker', 
'Kubernetes', 'Jenkins', 'Ansible', 'Chef', 'Puppet', 'GitLab', 'GitHub', 'CircleCI', 'Travis CI', 
'Atlassian Bamboo', 'TeamCity', 'CodeShip', 'Drone', 'Spinnaker', 'Vagrant', 'Terraform', 'Packer', 
'Consul', 'Vault', 'Prometheus', 'Grafana', 'ELK Stack (Elasticsearch, Logstash, Kibana)', 'Datadog',
'New Relic', 'Sumo Logic', 'Splunk', 'Nagios', 'Zabbix', 'Sensu', 'Graylog', 'Sysdig', 'Dynatrace',
'AppDynamics', 'PagerDuty', 'VictorOps', 'OpsGenie', 'Pingdom', 'Site24x7', 'SolarWinds', 
'ManageEngine', 'Icinga', 'Shippable', 'Wercker', 'Semaphore', 'Asana', 'Trello', 
'Microsoft Project', 'Basecamp', 'Jira', 'Monday.com', 'Wrike', 'Smartsheet', 'Teamwork',
'ClickUp', 'Airtable', 'Notion', 'Zoho Projects', 'Workfront', 'Hive', 'Todoist', 'MeisterTask', 
'Redbooth', 'Podio', 'Clarizen','ANN','CNN','RNN','LSTM','AI','NLP','nlp','Sketch', 'Adobe Photoshop', 
'Adobe Illustrator', 'Figma', 'InVision Studio', 'Axure RP', 'Adobe XD', 'Balsamiq', 'SketchUp', 
'Principle', 'Zeplin', 'Marvel', 'Flinto', 'Proto.io', 'Canva', 'Affinity Designer', 
'Affinity Photo', 'Gravit Designer', 'Blender', 'GIMP', 'CorelDRAW', 'Procreate', 
'Adobe After Effects', 'Adobe Premiere Pro', 'Final Cut Pro X', 'Motion', 'Blender Video Editing',
'Cinema 4D', 'Maya', 'Houdini', 'Substance Designer', 'Substance Painter', 'Unity', 'Unreal Engine',
'Webflow', 'SketchBook', 'Pixelmator', 'Clip Studio Paint', 'Krita', 'Paint Tool SAI', 'ArtRage', 
'Gravit Designer', 'Paper', 'Sketchable', 'Concepts', 'Miro', 'Lucidchart', 'Whimsical', 'Framer',
'Adobe Dreamweaver', 'Recruitment and Talent Acquisition', 'Performance Management', 
'Employee Engagement', 'Compensation and Benefits', 'Training and Development', 'Onboarding', 
'HR Analytics', 'Succession Planning', 'Diversity and Inclusion', 'Employee Relations',
'Compliance and Legal Knowledge', 'HRIS/HRMS', 'HR Strategy', 'Employment Law', 
'Conflict Resolution', 'Change Management', 'Leadership Development', 'HR Administration', 
'Employee Retention', 'Talent Management', 'Coaching and Mentoring', 'Strategic Planning', 
'Organizational Development', 'Project Management', 'Team Building', 'Business Acumen', 
'HR Metrics and Reporting', 'Budget Management', 'Emotional Intelligence', 'Communication Skills', 
'Time Management', 'Decision-Making Skills', 'Problem-Solving Skills', 'Customer Service Skills', 
'Vendor Management', 'Presentation Skills', 'Interviewing Skills', 'Performance Appraisal', 
'Labor Relations', 'Conflict Management', 'Benefits Administration', 'Wellness and Health Promotion',
'Employee Advocacy', 'Employee Benefits', 'Workforce Planning', 'Social Media Management', 
'Employer Branding', 'Strategic Sourcing', 'Cross-functional Collaboration','Risk Management',
'Pytorch','SaaS','Power BI','Data analysis','Data visualization','Data modeling','Data warehousing',
'Business intelligence','Data mining','ETL (Extract, Transform, Load)','Big data','Data science',
'Machine learning','Artificial intelligence','Predictive modeling','Statistical analysis',
'Data engineering','Natural language processing','Database administration','Database management',
'Database design','Data architecture','Data governance','Data quality','Data integration',
'Data security','Cloud data services','NoSQL databases','SQL databases','NoSQL',
'OLAP (Online Analytical Processing)','OLAP','Metadata management','Master data management',
'Data cleansing','Data enrichment','Data profiling','Data transformation','ETL','Communication',
'Active listening', 'Emotional intelligence', 'Collaboration', 'Adaptability', 'Creativity', 
'Problem-solving', 'Decision-making', 'Time management', 'Leadership', 'Interpersonal skills', 
'Empathy', 'Conflict resolution', 'Teamwork', 'Persuasion', 'Negotiation', 'Critical thinking',
'Analytical skills', 'Attention to detail', 'Organization', 'Self-motivation', 'Self-discipline',
'Positive attitude', 'Initiative', 'Flexibility', 'Stress management', 'Patience', 'Tolerance', 
'Diplomacy', 'Cultural awareness', 'Networking', 'Coaching and mentoring', 'Customer service', 
'Sales skills', 'Public speaking', 'Presentation skills', 'Writing skills', 'Conflict management', 
'Relationship building', 'Change management', 'Resilience', 'Accountability', 'Delegation', 
'Decision-making', 'Multitasking', 'Time management', 'Emotional control', 'Ethics', 'Dependability',
'Innovation','PL/SQL', 'T-SQL', 'Python', 'Bash/Shell scripting', 'Java', 'PowerShell', 'Perl', 'Ruby',
'Wireshark', 'Nagios', 'SolarWinds', 'PRTG', 'Zabbix', 'Ansible', 'Puppet', 'Chef', 'Nmap',
'Cisco Prime', 'HP Network Node Manager', 'OpenNMS', 'Cacti', 'Rancid', 'PingPlotter', 'Netcat', 
'TCPDump', 'NetFlow Analyzer', 'Splunk', 'Graylog','Wireshark', 'Nmap', 'tcpdump', 'Netcat', 'PuTTY', 
'SecureCRT', 'SolarWinds', 'PRTG', 'Zabbix', 'Ansible', 'Puppet', 'Chef', 'Cisco Prime', 'HP Network Node Manager',
'OpenNMS', 'Cacti', 'Rancid', 'PingPlotter', 'NetFlow Analyzer', 'Splunk', 'Graylog',
'Python', 'Bash', 'PowerShell', 'JavaScript', 'Ruby', 'Perl', 'C/C++', 'Java', 'PHP',
'Amazon Web Services', 'Microsoft Azure', 'Google Cloud Platform', 'Kubernetes', 'Docker', 'Terraform', 
'Ansible', 'Chef', 'Puppet', 'Jenkins', 'Git', 'Grafana', 'Prometheus', 'ELK Stack', 'Nagios', 
'Zabbix', 'Python', 'Java', 'JavaScript', 'Go', 'Ruby', 'SQL', 'Bash/Shell Scripting', 'HTML/CSS',
'PHP', 'R', 'Scala', 'Swift', 'Objective-C', 'TypeScript', 'Perl', 'C', 'C++', 'C#', 'Visual Basic',
'Visual Basic .NET', 'Groovy', 'Dart', 'Assembly language', 'MATLAB', 'Lua', 'Kotlin', 'PHPMyAdmin', 
'Apache', 'Nginx', 'MySQL', 'PostgreSQL', 'MongoDB', 'Oracle Cloud Infrastructure', 'Firebase', 
'PowerShell', 'Kubernetes', 'Docker', 'Terraform', 'Ansible', 'Chef', 'Puppet', 'Jenkins', 'Git', 
'GitHub', 'GitLab', 'Bitbucket', 'Grafana', 'Prometheus', 'ELK Stack', 'Nagios', 'Zabbix', 'Python',
'Java', 'JavaScript', 'Go', 'Ruby', 'Node.js', 'React', 'Angular', 'Vue.js', 'SQL', 
'Bash/Shell Scripting', 'HTML/CSS', 'PHP', 'R', 'Scala', 'Swift', 'Objective-C', 'TypeScript',
'Perl', 'C', 'C++', 'C#', 'Visual Basic', 'Visual Basic .NET', 'Groovy', 'Dart', 'Assembly language',
'MATLAB', 'Lua', 'Kotlin', 'PHPMyAdmin', 'Apache', 'Nginx', 'MySQL', 'PostgreSQL', 'MongoDB', 
'Oracle Cloud Infrastructure', 'Firebase', 'PowerShell','Metasploit', 'Nmap', 'Wireshark', 
'Burp Suite', 'Kali Linux', 'Snort', 'Suricata', 'Python', 'Java', 'JavaScript', 'Go', 'Ruby', 
'SQL', 'Bash/Shell Scripting', 'HTML/CSS', 'PHP', 'R', 'Scala', 'Swift', 'Objective-C', 
'TypeScript', 'Perl', 'C', 'C++', 'C#', 'Visual Basic', 'Visual Basic .NET', 'Groovy', 'Dart',
'Assembly language', 'MATLAB', 'Lua', 'Kotlin', 'PHPMyAdmin', 'Apache', 'Nginx', 'MySQL', 
'PostgreSQL', 'MongoDB', 'Elasticsearch', 'Logstash', 'Kibana', 'Splunk', 'Graylog', 'OpenVAS',
'Sn1per', 'BeEF', 'SQLMap', 'Aircrack-ng', 'John the Ripper', 'Hashcat', 'Maltego', 'Recon-ng',
'Osquery','Wireshark', 'Nmap', 'Metasploit', 'Burp Suite', 'Kali Linux', 'Snort', 'Suricata',
'Python', 'JavaScript', 'Go', 'Ruby', 'SQL', 'Bash/Shell Scripting', 'HTML/CSS', 'PHP', 'C',
'C++', 'C#', 'Java', 'Perl', 'Scala', 'Swift', 'Objective-C', 'TypeScript', 'Visual Basic', 
'Visual Basic .NET', 'Groovy', 'Dart', 'Assembly language', 'MATLAB', 'Lua', 'Kotlin', 'PHPMyAdmin',
'Apache', 'Nginx', 'MySQL', 'PostgreSQL', 'MongoDB', 'Elasticsearch', 'Logstash', 'Kibana', 'Splunk',
'Graylog', 'OpenVAS', 'Sn1per', 'BeEF', 'SQLMap', 'Aircrack-ng', 'John the Ripper', 'Hashcat',
'Maltego', 'Recon-ng', 'Osquery','Microsoft Word', 'Adobe Acrobat', 'Markdown', 'Git', 'HTML', 
'CSS', 'JavaScript', 'Python', 'Java', 'C++', 'C#', 'PHP', 'Ruby', 'SQL', 'Bash/Shell Scripting',
'XML', 'JSON', 'YAML', 'Tomcat', 'Apache', 'Nginx', 'AWS', 'Azure', 'Google Cloud', 'Docker', 
'Kubernetes', 'JIRA', 'Confluence', 'GitHub', 'Bitbucket', 'GitLab', 'Linux', 'Windows', 'MacOS',
'VMware', 'Hyper-V', 'Salesforce', 'Zendesk', 'Freshdesk', 'Slack', 'Zoom', 'Microsoft Teams', 
'Trello', 'Asana', 'Zendesk', 'GIMP', 'Inkscape', 'Snagit', 'Camtasia', 'Adobe Photoshop',
'Jira', 'Trello', 'Asana', 'AgileCraft', 'Rally', 'VersionOne', 'Scrumwise', 'Monday.com', 'Wrike',
'Agile Central', 'LeanKit', 'Kanbanize', 'Miro', 'Smartsheet', 'Planview','Microsoft Visio', 
'Sparx Enterprise Architect', 'ArchiMate', 'UML', 'BPMN', 'Zachman Framework', 'TOGAF', 
'MagicDraw', 'IBM Rational System Architect', 'ARIS', 'ERwin', 'CA ERwin Data Modeler',
'ABACUS', 'Troux', 'Orbus iServer','Java', 'Python', 'C#', 'JavaScript', 'TypeScript',
'Hadoop','statistics','PowerPoint','marketing','Docker','data structures',
 'deep learning','SQL', 'ASP','.NET', 'C#', '.NET', 'vba','numpy', 'pandas', 'matplotlib', 'scipy',
'scikit-learn', 'seaborn', 'tensorflow', 'keras', 'pytorch', 'opencv-python', 'pillow', 
'beautifulsoup4', 'requests', 'pyyaml', 'tqdm', 'networkx', 'gensim', 'nltk', 'spacy', 'textblob', 
'flask', 'django', 'fastapi', 'pyramid', 'sqlalchemy', 'mongoengine', 'redis', 'celery',
'pyinstaller', 'pytest', 'unittest', 'selenium', 'beatifulsoup4', 'lxml', 'html5lib', 'openpyxl', 
'xlrd', 'xlsxwriter', 'docx', 'python-docx', 'reportlab', 'pyPDF2', 'weasyprint', 'pyjwt', 'bcrypt',
'passlib', 'pycrypto', 'cryptography', 'paramiko', 'fabric','Django',    'Flask',    'Pyramid',
'TurboGears','Bottle','CherryPy','Dash','FastAPI','Hug','Quart','Sanic','Tornado','web2py','web.py',
"Spring","Hibernate","Struts","Apache Wicket","Dropwizard","Vert.x","MyBatis","Guava","Apache Commons","Log4j",
"JUnit","Mockito","Selenium","TestNG","Jackson","Gson","JAXB","Apache POI","Apache Kafka","Netty",
"Laravel","Symfony","CodeIgniter","CakePHP","Zend","Slim","Doctrine","Twig","PHPUnit","Mockery","PHPMailer",
"Guzzle","Monolog","Carbon","Faker","Phinx","PHPExcel","PHPWord","PHPMailer","TCPDF""Ruby on Rails",
"Sinatra","Padrino","Hanami","Sequel","ActiveRecord","Devise","Capybara","RSpec","FactoryBot","CarrierWave",
"Fog","DelayedJob","Sidekiq","Puma","Unicorn","Grape","Goliath","GraphQL","Apollo Server"]
       


