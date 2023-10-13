from flask import Blueprint, request, jsonify

from server.tasks.generate import generate_cover_letter_task

# constants
model = "gpt-4"
api = Blueprint("api", __name__, url_prefix="/api/v1")

"""
Define a health check endpoint
"""
@api.route("/health", methods=["GET"])
def health():
    return "OK", 200


"""
Define a function to start a task to generate a cover letter given the name of a job description and a resume file
INPUTS: job_description, resume, extra_information
OUTPUTS: task_id
"""
@api.route("/generate_cover_letter", methods=["POST"])
def generate_cover_letter():
    # call the celery task to generate a cover letter
    task = generate_cover_letter_task.delay(request.json["resume"], request.json["job_description"], request.json["extra_information"], request.json["to"])
    # return the task id
    return jsonify({"task_id": task.id})


"""
Define a function to get the status of the task
INPUTS: task_id
OUTPUTS: task_status
"""
@api.route("/generate_cover_letter/<task_id>/status", methods=["GET"])
def generate_cover_letter_status(task_id):
    # get the task result
    result = generate_cover_letter_task.AsyncResult(task_id)
    # return the task status
    return jsonify({"task_status": result.status})


"""
Define a function to get the result of the task
INPUTS: task_id
OUTPUTS: result

check for errors and task status
"""
@api.route("/generate_cover_letter/<task_id>/result", methods=["GET"])
def generate_cover_letter_result(task_id):
    # get the task result
    result = generate_cover_letter_task.AsyncResult(task_id)
    # check for errors
    if result.failed():
        # return the error
        return jsonify({"error": str(result.info)})
    # check for task status
    if result.ready():
        # return the result
        return result.get()
    # return the task status
    return jsonify({"task_status": result.status})