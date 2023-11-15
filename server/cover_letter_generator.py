import eventlet
# eventlet.monkey_patch()
eventlet.patcher.import_patched('requests.__init__')

import openai
import os

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

# Sample message state
"""
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, who are you?"},
    {"role": "assistant", "content": "I am an AI created by OpenAI. How can I help you today?"},
]
"""

# Define an function that takes a message state and a prompt and returns a new message state
"""
1. The user's message is appended to the chat as follows {"role": "user", "content": message}
2. A ChatCompletion is requested from the API
3. The response is appended to the chat as follows {"role": "assistant", "content": chat_message}
4. The new message state is returned
"""
def update_chat(messages, prompt, model="gpt-3.5-turbo"):
    # Append the user's message to the chat
    messages.append({"role": "user", "content": prompt})
    
    # Request gpt-3.5-turbo for chat completion
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    
    # Append the response to the chat
    chat_message = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": chat_message})
    
    # Return the new message state
    return messages



################---PROMPT 1---###################
"""
Prompt 1: Extract the resume in a generalized format
Check the given resume against the general resume template and prepare a simplified resume

Output: O1
"""
#################################################
# Define an function to extract the resume in a generalized format
"""
1. Call the update_chat function with the resume contents and the prompt
2. Return the response from the update_chat function
"""
def extract_resume(resume, messages, model="gpt-3.5-turbo"):
    # TODO: REMOVE DEBUG
    print("Extracting resume...")
    
    # define the prompt
    prompt = """ 
    {resume}

    Extract the essential data from the given resume and prepare a simplified resume
    """.format(resume= resume)

    # Call the update_chat function with the resume contents and the prompt
    messages = update_chat(messages, prompt, model="gpt-3.5-turbo")
    
    # Return the response from the update_chat function
    return messages


################---PROMPT 2---###################
"""
Prompt 2: Simplify the job description and list only the responsibilities and skills required
[job description]

Output: O2
"""
#################################################
# Define an function to simplify the job description and list only the responsibilities and skills required
"""
1. Call the update_chat function with the job description and the prompt
2. Return the response from the update_chat function
"""
def simplify_job_description(job_description, messages, model="gpt-3.5-turbo"):
    # define the prompt
    prompt = """ 
    {job_description}

    Simplify the job description and list only the responsibilities and skills required
    """.format(job_description= job_description)

    # Call the update_chat function with the job description and the prompt
    messages = update_chat(messages, prompt, model="gpt-3.5-turbo")
    
    # Return the response from the update_chat function
    return messages


################---PROMPT 3---###################
"""
Prompt 3: Cover letter generation
Here is a job description:
[O1]

Here is a resume for a candidate for the job:
[O2]

Create a cover letter for the candidate who is applying for the job.
"""
#################################################
# Define an function to generate a cover letter
"""
1. Call the update_chat function with the job description and the prompt
2. Return the response from the update_chat function
"""
def generate_cover_letter(job_description, resume, messages, model="gpt-3.5-turbo", to="hiring manager"):
    # define the prompt
    prompt = """ 
    Here is a job description:
    {job_description}

    Here is a resume for a candidate for the job:
    {resume}

    Create a cover letter to be mailed to {to} for the candidate who is applying for the job.
    Focus on matching the candidate's skills and experience to the job description.
    Important: Use bullet points wherever possible.
    """.format(job_description=job_description, resume=resume, to=to)

    # Call the update_chat function with the job description and the prompt
    messages = update_chat(messages, prompt, model=model)
    
    # Return the response from the update_chat function
    return messages


################---PROMPT 4---###################
"""
Prompt 3: Extra information
Here are some paragraphs about the candidate:
[paragraphs]

Include the paragraphs in the cover letter.
"""
#################################################
# Define an function to include extra information
"""
1. Call the update_chat function with the job description and the prompt
2. Return the response from the update_chat function
"""
def include_extra_information(paragraphs, messages, model="gpt-3.5-turbo"):
    # define the prompt
    prompt = """ 
    Include this in the cover letter where appropriate:
    {paragraphs}

    Keep everything else same.
    """.format(paragraphs= paragraphs)

    # Call the update_chat function with the job description and the prompt
    messages = update_chat(messages, prompt, model="gpt-3.5-turbo")
    
    # Return the response from the update_chat function
    return messages

# Define an function to generate an HTML version of the given cover letter
def generate_html_cover_letter(messages, model="gpt-3.5-turbo"):
    # define the prompt
    prompt = """ 
    Generate a well formatted HTML version of the given cover letter.
    """

    # Call the update_chat function with the job description and the prompt
    messages = update_chat(messages, prompt, model=model)
    
    # Return the last message content from the update_chat function
    return messages[-1]['content']

#
# Define an function to generate a cover letter given the name of a job description and a resume file
#
def get_cover_letter(job_description, resume, extra_information="", model="gpt-3.5-turbo", to="hiring manager"):
    # Initialize the message state
    messages = [
        {"role": "system", "content": "You are a job recruitment assistant. You excel at writing cover letters for job applicants. For subsequent prompts, please respond only with the output. DON'T respond with something like 'Here is the output:' [output]. DON'T respond inside a code block."},
    ]

    # Extract the resume in a generalized format
    messages = extract_resume(resume, messages, model=model)

    # Simplify the job description and list only the responsibilities and skills required
    messages = simplify_job_description(job_description, messages, model=model)

    # Generate a cover letter
    messages = generate_cover_letter(job_description, resume, messages, model=model, to=to)

    # Include extra information
    if extra_information:
        messages = include_extra_information(extra_information, messages, model=model)

    # HTML version of the cover letter
    html_cover_letter = generate_html_cover_letter(messages, model=model)

    # Return the cover letter
    # return messages
    return html_cover_letter


def test():
    # TODO: REMOVE DEBUG
    print("Reading resume...")

    # extract the resume from the file
    resume = open("resume.txt", "r").read()
    
    # TODO: REMOVE DEBUG
    print("Reading job description...")

    # extract the job description from the file
    job_description = open("job_description.txt", "r").read()

    # extract the extra information from the file
    # extra_information = open("extra_information.txt", "r").read()

    # TODO: REMOVE DEBUG
    print("Generating cover letter...")

    # generate the cover letter
    cover_letter = get_cover_letter(job_description, resume, model="gpt-4")

    # print the cover letter
    print(cover_letter[-1]['content'])


if __name__ == "__main__":
    test()