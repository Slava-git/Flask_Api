# Flask Api
## General info
There was built a CRUD courses management app based on MVC pattern.
Flask is used for creating endpoints. Project does not have a view because it is not necessary.  
App has the following features:
* create course;
* get course by id or name and date;
* get all courses;
* delete course;
* update course;
## Technologies
* python 3.7
* Flask-SQLAlchemy 2.4.4
* SQLAlchemy 1.3.13
* SqLite3
## Run project
`python run.py`   
I used postman for sending requests.
## Tests
Get all courses
![get_list_courses](images/get_list_courses.png)

Add course 

![add_course](images/add_course.png)

Erorr when added wrong course

![error_add_course](images/error_add_course.png)

Get course by id

![get_course_by_id](images/get_course_by_id.png)

Get course by name and date

![get_course_by_name_and_date](images/get_course_by_name_and_date.png)

Error with wrong name

![error_get_course_by_name_and_date](images/error_get_course_by_name_and_date.png)

Update operation

![update](images/update_1.png)

After update 

![update_after](images/update_2.png)

Deleting 

![delete](images/delete.png)
