# from django.shortcuts import render
# import os
# import openai

# # Create your views here.

# def fun():
#   openai.api_key ="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"

#   response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt=f"Govardhana K Senior Software Engineer  Bengaluru, Karnataka, Karnataka - Email me on Indeed: indeed.com/r/Govardhana-K/ b2de315d95905b68  Total IT experience 5 Years 6 Months Cloud Lending Solutions INC 4 Month \\u2022 Salesforce Developer Oracle 5 Years 2 Month \\u2022 Core Java Developer Languages Core Java, Go Lang Oracle PL-SQL programming, Sales Force Developer with APEX.  Designations & Promotions  Willing to relocate: Anywhere  WORK EXPERIENCE  Senior Software Engineer  Cloud Lending Solutions -  Bangalore, Karnataka -  January 2018 to Present  Present  Senior Consultant  Oracle -  Bangalore, Karnataka -  November 2016 to December 2017  Staff Consultant  Oracle -  Bangalore, Karnataka -  January 2014 to October 2016  Associate Consultant  Oracle -  Bangalore, Karnataka -  November 2012 to December 2013  EDUCATION  B.E in Computer Science Engineering  Adithya Institute of Technology -  Tamil Nadu  September 2008 to June 2012  https://www.indeed.com/r/Govardhana-K/b2de315d95905b68?isid=rex-download&ikw=download-top&co=IN https://www.indeed.com/r/Govardhana-K/b2de315d95905b68?isid=rex-download&ikw=download-top&co=IN   SKILLS  APEX. (Less than 1 year), Data Structures (3 years), FLEXCUBE (5 years), Oracle (5 years), Algorithms (3 years)  LINKS  https://www.linkedin.com/in/govardhana-k-61024944/  ADDITIONAL INFORMATION  Technical Proficiency:  Languages: Core Java, Go Lang, Data Structures & Algorithms, Oracle PL-SQL programming, Sales Force with APEX. Tools: RADTool, Jdeveloper, NetBeans, Eclipse, SQL developer, PL/SQL Developer, WinSCP, Putty Web Technologies: JavaScript, XML, HTML, Webservice  Operating Systems: Linux, Windows Version control system SVN & Git-Hub Databases: Oracle Middleware: Web logic, OC4J Product FLEXCUBE: Oracle FLEXCUBE Versions 10.x, 11.x and 12.x  https://www.linkedin.com/in/govardhana-k-61024944/\n\nextract name, skills, location, email address, companies worked at, Degree, graduation year, designation, phone, college, and year of experience\n\n\nName: Govardhana K\nSkills: Core Java, Go Lang, Data Structures & Algorithms, Oracle PL-SQL programming, Sales Force with APEX.,RADTool, Jdeveloper, NetBeans, Eclipse, SQL developer, PL/SQL Developer, WinSCP, Putty, JavaScript, XML, HTML, Webservice\nLocation: Bengaluru, Karnataka, Karnataka\nEmail address: indeed.com/r/Govardhana-K/b2de315d95905b68\nCompanies worked at: Cloud Lending Solutions INC, Oracle\nDegree: B.E in Computer Science Engineering\nGraduation year: June 2012\nDesignation: Senior Software Engineer\nPhone: N/A\nCollege: Adithya Institute of Technology\nYear of experience: 5 Years 6 Months\n\n{var}\n\nextract name, skills, location, email address, companies worked at, Degree, graduation year, designation, phone, college, and year of experience",
#     temperature=0.7,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
#   )

from django.shortcuts import render
import os
import openai
import PyPDF2

# Create your views here.

from django.shortcuts import render
import os
import openai
import pdfplumber

# Create your views here.

def extract_resume_data(file_path):
    with pdfplumber.open(file_path) as pdf_file:
        resume_text = ''
        for page in pdf_file.pages:
            resume_text += page.extract_text()

    openai.api_key = "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"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Govardhana K Senior Software Engineer  Bengaluru, Karnataka, Karnataka - Email me on Indeed: indeed.com/r/Govardhana-K/ b2de315d95905b68  Total IT experience 5 Years 6 Months Cloud Lending Solutions INC 4 Month \\u2022 Salesforce Developer Oracle 5 Years 2 Month \\u2022 Core Java Developer Languages Core Java, Go Lang Oracle PL-SQL programming, Sales Force Developer with APEX.  Designations & Promotions  Willing to relocate: Anywhere  WORK EXPERIENCE  Senior Software Engineer  Cloud Lending Solutions -  Bangalore, Karnataka -  January 2018 to Present  Present  Senior Consultant  Oracle -  Bangalore, Karnataka -  November 2016 to December 2017  Staff Consultant  Oracle -  Bangalore, Karnataka -  January 2014 to October 2016  Associate Consultant  Oracle -  Bangalore, Karnataka -  November 2012 to December 2013  EDUCATION  B.E in Computer Science Engineering  Adithya Institute of Technology -  Tamil Nadu  September 2008 to June 2012  https://www.indeed.com/r/Govardhana-K/b2de315d95905b68?isid=rex-download&ikw=download-top&co=IN https://www.indeed.com/r/Govardhana-K/b2de315d95905b68?isid=rex-download&ikw=download-top&co=IN   SKILLS  APEX. (Less than 1 year), Data Structures (3 years), FLEXCUBE (5 years), Oracle (5 years), Algorithms (3 years)  LINKS  https://www.linkedin.com/in/govardhana-k-61024944/  ADDITIONAL INFORMATION  Technical Proficiency:  Languages: Core Java, Go Lang, Data Structures & Algorithms, Oracle PL-SQL programming, Sales Force with APEX. Tools: RADTool, Jdeveloper, NetBeans, Eclipse, SQL developer, PL/SQL Developer, WinSCP, Putty Web Technologies: JavaScript, XML, HTML, Webservice  Operating Systems: Linux, Windows Version control system SVN & Git-Hub Databases: Oracle Middleware: Web logic, OC4J Product FLEXCUBE: Oracle FLEXCUBE Versions 10.x, 11.x and 12.x  https://www.linkedin.com/in/govardhana-k-61024944/\n\nextract name, skills, location, email_address, companies_worked_at, Degree, graduation_year, designation, phone, college, and year_of_experience\n\n\nName: Govardhana K\nSkills: Core Java, Go Lang, Data Structures & Algorithms, Oracle PL-SQL programming, Sales Force with APEX.,RADTool, Jdeveloper, NetBeans, Eclipse, SQL developer, PL/SQL Developer, WinSCP, Putty, JavaScript, XML, HTML, Webservice\nLocation: Bengaluru, Karnataka, Karnataka\nEmail_address: indeed.com/r/Govardhana-K/b2de315d95905b68\nCompanies_worked_at: Cloud Lending Solutions INC, Oracle\nDegree: B.E in Computer Science Engineering\nGraduation_year: June 2012\nDesignation: Senior Software Engineer\nPhone: N/A\nCollege: Adithya Institute of Technology\nYear_of_experience: 5 Years 6 Months\n\n{resume_text}\n\nextract name, skills, location, email_address, companies_worked_at, Degree, graduation_year, designation, phone, college, and year_of_experience",
        temperature=0.6,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extracting the information from the response text
    response_text = response.choices[0].text
    lines = response_text.strip().split('\n')
    extracted_data = {}
    for line in lines:
        line = line.strip()
        if ':' in line:
            key, value = line.split(':')
            extracted_data[key.strip()] = value.strip()

    return extracted_data



def index(request):
    if request.method == 'POST':
        # Get the file from the request
        uploaded_file = request.FILES['document']
        # Write the file to the server
        with open('uploaded_resume.pdf', 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Extract data from the resume
        resume_data = extract_resume_data('uploaded_resume.pdf')
        
        # Render the output page with the extracted data
        
        return render(request, 'output.html', {'resume_data': resume_data})
    else:
        return render(request, 'index.html')
