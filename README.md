# Coverlettergen : Personalized Cover Letter API

### What is this?
**CoverLetterGen**: Elevate Your Job Hunt Like Never Before 🚀

- 🤖 **AI-Driven Precision**: Tailored cover letters from your resume and desired job description.
- 📈 **Unparalleled Scalability & Concurrency**: Craft up to 1000s of cover letters in a flash.
- 🚀 **One-Click Deployment**: Set up a production-grade API on AWS effortlessly.
- 🔧 **Customizable Core**: Extend and adapt the API to fit your unique needs.



### Installation and Quickstart
1. Before diving in, ensure you peek into the `.env.example` file. Create a corresponding `.env` file with your configurations.
2. Then get the entire project up and running with a simple

```
docker-compose up --build
```

### Usecases
This project can be used in multiple ways:

- Use as a self-hosted cover letter generator (personal use)
- Use as a component of a broader system (e.g. Automated Job Application Software)
- Use as a microservice/backend API for a web/mobile application

The possiblities are endless!

### API
The server has the following API endpoints:

##### `POST /generate_cover_letter`
```
{
    "resume": "sample resume",
    "job_description": "sample job description",
    "extra_information": "sample extra information",
    "to": "john.doe@email.com"
}
```
returns
```
{
    "task_id": "2982028d-6883-4acc-a34a-fd9661a536a8"
}
```

##### `GET /generate_cover_letter/<task_id>/status`
returns
```
{
    "task_status": "<PENDING | FAILURE | SUCCESS>"
}
```

##### `GET /generate_cover_letter/<task_id>/result`
returns
```
<html>
...
<EMAIL BODY IN HTML FORMAT HERE>
...
</html>
```

### Deployment
🚧 **Under Construction**: The deployment section is currently in the works and is experimental. However, I'm excited to share that Coverlettergen will be fully deployable on AWS right out-of-the-box using Terraform! After your successful deployment, locate the server URL in the `api.txt` file.


___

Star this repository and contribute to making Coverlettergen the best open-source cover letter API out there! 🌟💌🚀