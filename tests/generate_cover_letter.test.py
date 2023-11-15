import requests
import json

# Define a list of requests
requests_data = [
    {
        "url": "http://localhost:8080/api/v1/generate_cover_letter",
        "headers": {
            'Content-Type': 'application/json'
        },
        "data": json.dumps({
            "to": "John Smith",
            "resume": "123 MAIN STREET, MELBOURNE, VIC 3000 (0412) 345-678 JOHN.SMITH@EMAIL.COM JOHN SMITH https://github.com/johnsmithdev www.linkedin.com/in/john-smith-dev Experienced software developer with a focus on web technologies and cloud solutions. Proven track record of delivering high-quality software solutions on time and within budget. Strengths include: Web Development: ● Proficient in HTML, CSS, JavaScript, and modern frameworks ● Experience with responsive design and mobile-first principles Cloud Solutions: ● Expertise in AWS, Azure, and Google Cloud ● Familiar with containerization and orchestration tools like Docker and Kubernetes EXPERIENCE WebTech Solutions (January 2022 - September 2023) Melbourne ● Led a team of developers to deliver web solutions for clients across various industries. ● Implemented CI/CD pipelines to streamline deployment processes. PROJECTS WebPortal ● Developed a portal for clients to manage their accounts and view analytics. ● Integrated third-party APIs to enhance functionality. CERTIFICATIONS AWS Certified Developer Associate Gained hands-on experience with AWS services and best practices for developing cloud-native applications. Google Cloud Professional Developer Acquired knowledge on building scalable and reliable applications using Google Cloud. SKILLS Languages: JavaScript, Python, Ruby, Go Frameworks: React, Vue, Angular, Express EDUCATION Monash University, Melbourne — Bachelor of Computer Science Graduated December 2022 - Achieved High Distinction in Advanced Web Development.",
            "job_description": "We are seeking a Senior Web Developer to join our dynamic team. The ideal candidate will have a strong background in web development and be familiar with the latest trends and technologies in the industry. Responsibilities include developing and maintaining our company website, integrating third-party APIs, and collaborating with the design team to ensure a seamless user experience. Requirements: ● 3+ years of web development experience ● Proficiency in JavaScript, HTML, and CSS ● Familiarity with modern web frameworks like React or Vue ● Experience with cloud platforms like AWS or Azure ● Strong problem-solving skills and attention to detail.",
            "extra_information": ""
        })
    },
    {
        "url": "http://localhost:8080/api/v1/generate_cover_letter",
        "headers": {
            'Content-Type': 'application/json'
        },
        "data": json.dumps({
            "to": "Jane Doe",
            "resume": "456 HIGH STREET, PERTH, WA 6000 (0413) 789-012 JANE.DOE@EMAIL.COM JANE DOE https://github.com/janedoedev www.linkedin.com/in/jane-doe-dev Passionate backend developer with expertise in database design and optimization. Adept at creating scalable and efficient systems. Strengths include: Backend Development: ● Proficient in Node.js, Django, and Ruby on Rails ● Experience with database design and optimization using SQL and NoSQL databases Cloud Solutions: ● Expertise in serverless architectures and microservices ● Familiar with deployment and monitoring tools EXPERIENCE BackendTech Solutions (February 2021 - August 2023) Perth ● Designed and implemented scalable backend systems for various clients. ● Optimized database queries to improve system performance. PROJECTS DataHub ● Developed a centralized data hub for clients to store and retrieve data efficiently. ● Implemented caching mechanisms to reduce database load. CERTIFICATIONS Node.js Certified Developer Demonstrated proficiency in building scalable applications using Node.js. MongoDB Certified Developer Acquired skills in designing and optimizing MongoDB databases. SKILLS Languages: JavaScript, Python, Ruby Frameworks: Express, Django, Ruby on Rails EDUCATION University of Western Australia, Perth — Bachelor of Software Engineering Graduated November 2021 - Specialized in Database Systems and Backend Development.",
            "job_description": "We are looking for a Backend Developer to join our team. The candidate will be responsible for designing and implementing backend systems, optimizing database queries, and ensuring high availability of our services. Requirements: ● 2+ years of backend development experience ● Proficiency in Node.js or Django ● Experience with SQL and NoSQL databases ● Familiarity with cloud platforms and serverless architectures ● Strong analytical and debugging skills.",
            "extra_information": ""
        })
    },
    {
        "url": "http://localhost:8080/api/v1/generate_cover_letter",
        "headers": {
            'Content-Type': 'application/json'
        },
        "data": json.dumps({
            "to": "Alice Williams",
            "resume": "789 PARK AVENUE, ADELAIDE, SA 5000 (0414) 123-456 ALICE.WILLIAMS@EMAIL.COM ALICE WILLIAMS https://github.com/alicewilliamsdev www.linkedin.com/in/alice-williams-dev Mobile app developer with a flair for creating intuitive and user-friendly applications. Skilled in both iOS and Android development. Strengths include: Mobile App Development: ● Proficient in Swift, Kotlin, and Flutter ● Experience with app store optimization and deployment Cloud Solutions: ● Expertise in Firebase and AWS Amplify ● Familiar with mobile backend services and APIs EXPERIENCE MobileAppTech Solutions (March 2022 - October 2023) Adelaide ● Developed mobile apps for clients in various industries including finance, healthcare, and e-commerce. ● Collaborated with UX/UI designers to ensure a seamless user experience. PROJECTS FinTrack ● Developed a financial tracking app with features like expense tracking, budgeting, and financial forecasting. ● Integrated third-party payment gateways for in-app purchases. CERTIFICATIONS Google Associate Android Developer Demonstrated proficiency in building Android apps using Kotlin. Apple Certified iOS Developer Acquired skills in developing iOS apps using Swift and Objective-C. SKILLS Languages: Swift, Kotlin, Dart Frameworks: Flutter, React Native, Xamarin EDUCATION University of Adelaide, Adelaide — Bachelor of Information Technology Graduated December 2022 - Specialized in Mobile App Development and Cloud Computing.",
            "job_description": "We are on the hunt for a talented Mobile App Developer to join our team. The ideal candidate will have experience in developing mobile apps for both iOS and Android platforms. Responsibilities include designing and developing mobile apps, collaborating with the design team, and ensuring the apps meet quality standards. Requirements: ● 3+ years of mobile app development experience ● Proficiency in Swift or Kotlin ● Experience with cross-platform frameworks like Flutter or React Native ● Familiarity with cloud platforms and mobile backend services ● Strong problem-solving skills and attention to detail.",
            "extra_information": ""
        })
    },
    {
        "url": "http://localhost:8080/api/v1/generate_cover_letter",
        "headers": {
            'Content-Type': 'application/json'
        },
        "data": json.dumps({
            "to": "Bob Martin",
            "resume": "101 SUNSET BOULEVARD, BRISBANE, QLD 4000 (0415) 654-321 BOB.MARTIN@EMAIL.COM BOB MARTIN https://github.com/bobmartindev www.linkedin.com/in/bob-martin-dev Data scientist with a knack for extracting meaningful insights from large datasets. Experienced in machine learning and statistical analysis. Strengths include: Data Analysis: ● Proficient in Python, R, and SQL ● Experience with data visualization tools like Tableau and PowerBI Machine Learning: ● Expertise in supervised and unsupervised learning algorithms ● Familiar with deep learning frameworks like TensorFlow and PyTorch EXPERIENCE DataScienceTech Solutions (April 2021 - September 2023) Brisbane ● Conducted data analysis for clients in various industries including retail, finance, and healthcare. ● Developed machine learning models to predict customer behavior and sales trends. PROJECTS SalesPredictor ● Developed a machine learning model to predict sales trends based on historical data. ● Achieved an accuracy of 95% in predicting future sales. CERTIFICATIONS Data Science Professional Certification Demonstrated proficiency in data analysis and machine learning techniques. TensorFlow Developer Certification Acquired skills in developing deep learning models using TensorFlow. SKILLS Languages: Python, R, SQL Frameworks: TensorFlow, PyTorch, Scikit-learn EDUCATION Queensland University of Technology, Brisbane — Master of Data Science Graduated November 2021 - Specialized in Machine Learning and Big Data Analytics.",
            "job_description": "We are seeking a Data Scientist to join our analytics team. The candidate will be responsible for analyzing large datasets, developing machine learning models, and presenting insights to stakeholders. Requirements: ● 2+ years of data science experience ● Proficiency in Python or R ● Experience with machine learning algorithms and frameworks ● Familiarity with data visualization tools like Tableau or PowerBI ● Strong analytical and communication skills.",
            "extra_information": ""
        })
    },
    {
        "url": "http://localhost:8080/api/v1/generate_cover_letter",
        "headers": {
            'Content-Type': 'application/json'
        },
        "data": json.dumps({
            "to": "Charlie Brown",
            "resume": "303 RIVER ROAD, HOBART, TAS 7000 (0416) 987-654 CHARLIE.BROWN@EMAIL.COM CHARLIE BROWN https://github.com/charliebrowndev www.linkedin.com/in/charlie-brown-dev DevOps engineer with a focus on automating deployment processes and ensuring high system availability. Experienced in infrastructure as code and container orchestration. Strengths include: DevOps Practices: ● Proficient in Jenkins, Travis CI, and CircleCI ● Experience with infrastructure as code tools like Terraform and Ansible Cloud Solutions: ● Expertise in AWS, Azure, and Google Cloud ● Familiar with container orchestration tools like Kubernetes and Docker Swarm EXPERIENCE DevOpsTech Solutions (May 2022 - October 2023) Hobart ● Implemented CI/CD pipelines for clients to streamline deployment processes. ● Managed cloud infrastructure and ensured high system availability. PROJECTS CloudDeploy ● Developed a cloud deployment solution using Terraform and Ansible. ● Achieved a deployment time reduction of 50% for client projects. CERTIFICATIONS AWS Certified DevOps Engineer Demonstrated proficiency in AWS DevOps practices and tools. Kubernetes Certified Administrator Acquired skills in managing Kubernetes clusters and workloads. SKILLS Tools: Jenkins, Travis CI, CircleCI Frameworks: Terraform, Ansible, Docker, Kubernetes EDUCATION University of Tasmania, Hobart — Bachelor of Computer Systems Engineering Graduated December 2022 - Specialized in Cloud Computing and DevOps Practices.",
            "job_description": "We are looking for a DevOps Engineer to join our team. The candidate will be responsible for implementing CI/CD pipelines, managing cloud infrastructure, and ensuring high system availability. Requirements: ● 3+ years of DevOps experience ● Proficiency in Jenkins or Travis CI ● Experience with infrastructure as code tools like Terraform or Ansible ● Familiarity with cloud platforms like AWS or Azure ● Strong problem-solving skills and attention to detail.",
            "extra_information": ""
        })
    },
]

# Initialize an empty list to store task_ids
task_ids = []

# Loop through each request, send it, extract the task_id, and save it to the list
for i, request_data in enumerate(requests_data):
    print(f"Executing request {i+1}...")
    response = requests.post(request_data["url"], headers=request_data["headers"], data=request_data["data"])
    response_json = response.json()
    task_id = response_json.get("task_id", "")
    task_ids.append(task_id)
    print(f"Saved task_id of request {i+1}")

# Save all task_ids to responses.txt
with open("responses.txt", "w") as f:
    for task_id in task_ids:
        f.write(f"{task_id}\n")

print("All task_ids saved successfully!")
