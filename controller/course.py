from flask import jsonify, make_response
from controller.parse_request import get_request_data
from settings.constants import Course_fields
from datetime import datetime
from model.сourse import Course

def add_course():
    data = get_request_data()
    try:
        data['start_date'] = datetime.strptime(data['start_date'], '%d.%m.%Y').date()
        data['end_date'] = datetime.strptime(data['end_date'], '%d.%m.%Y').date()
    except:
        err=' Error while converting str to date, check format dd.mm.yyyy'
        make_response(jsonify(error=err), 400)
    try:
        add_record = Course.add(**data)
        print(add_record.__dict__)
        new_course = {k: v for k, v in add_record.__dict__.items() if k in Course_fields}
        return make_response(jsonify(new_course), 200)
    except:
        err = 'Input wrong fields'
        return make_response(jsonify(error=err), 400)

def get_all_courses():
    all_courses = Course.query.all()
    courses = []
    for course in all_courses:
        _course = {k: v for k, v in course.__dict__.items() if k in Course_fields}
        courses.append(_course)
    return make_response(jsonify(courses), 200)

def get_course_by_id():
    data = get_request_data()
    try:
        row_id = int(data['id'])
    except:
        err = 'Id must be integer'
        return make_response(jsonify(error=err), 400)
    try:
        obj = Course.query.filter_by(id=row_id).first()
        course = {k: v for k, v in obj.__dict__.items() if k in Course_fields}
        return make_response(jsonify(course), 200)
    except:
        err = 'Record with such id does not exist'
        return make_response(jsonify(error=err), 400)

def get_course_by_name_and_date():
    data = get_request_data()
    try:
        data['start_date'] = datetime.strptime(data['start_date']+" 00:00:00", '%d.%m.%Y %H:%M:%S')
        data['end_date'] = datetime.strptime(data['end_date']+" 00:00:00", '%d.%m.%Y %H:%M:%S')
    except:
        err = "This is the incorrect date format"
        return make_response(jsonify(error=err), 400)
    name = data['name']
    start_date = data['start_date']
    end_date = data['end_date']
    try:
        obj = Course.query.filter_by(name=name).first()
        course = {k: v for k, v in obj.__dict__.items() if k in Course_fields}
        if course['start_date'] >= start_date and course['end_date'] <= end_date:
            return make_response(jsonify(course), 200)
        else:
            err = 'Record does not approach. Record has another term'
            return make_response(jsonify(error=err), 400)
    except:
        err = 'Record with such name does not exist'
        return make_response(jsonify(error=err), 400)

def update_course():
    data = get_request_data()
    try:
        row_id = int(data['id'])
    except:
        err = 'Id must be integer'
        return make_response(jsonify(error=err), 400)
    if "start_date" in data:
        try:
            data['start_date'] = datetime.strptime(data['start_date']+" 00:00:00", '%d.%m.%Y %H:%M:%S')
        except:
            err = "This is the incorrect date format"
            return make_response(jsonify(error=err), 400)
    if "end_date" in data:
        try:
            data['end_date'] = datetime.strptime(data['end_date']+" 00:00:00", '%d.%m.%Y %H:%M:%S')
        except:
            err = "This is the incorrect date format"
            return make_response(jsonify(error=err), 400)
    try:
        upd_record = Course.update(row_id, **data)
        upd_course = {k: v for k, v in upd_record.__dict__.items() if k in Course_fields}
        return make_response(jsonify(upd_course), 200)
    except:
        err = "Error when you tried update"
        return make_response(jsonify(err), 400)

def delete_course():
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)
    try:
        if (Course.delete(row_id) == 1):
            msg = 'Record successfully deleted'
            return make_response(jsonify(message=msg), 200)
        else:
            err = 'Something is wrong with deleting record'
            return make_response(jsonify(error=err), 400)
    except:
        err = 'Record with such id does not exist'
        return make_response(jsonify(error=err), 400)
