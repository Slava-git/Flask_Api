from flask import Flask, request
from flask import current_app as app

from controller.course import *

@app.route("/course", methods=["POST"])
def _add_course():
    return add_course()

@app.route("/courses", methods=["GET"])
def _get_all_courses():
    return get_all_courses()

@app.route("/course", methods=["GET"])
def _get_course_by_id():
    return get_course_by_id()

@app.route("/course_by_name_n_data", methods=["GET"])
def _get_course_by_name_and_date():
    return get_course_by_name_and_date()

@app.route("/course", methods=["PUT"])
def _update_course():
    return update_course()

@app.route("/course", methods=["DELETE"])
def _delete_course():
    return delete_course()