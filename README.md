# Flask Api
## General info
I built a CRUD (Create, Read, Update, Delete) courses management app.
Flask is used in project for creating endpoints. I used a pattern MVC. Project is without a view 'cause it is not necessary.
App has the following features:
* create course;
* get course by id or name and date;
* get all courses;
* delete course;
* update course;
## Technologies
List is shown below:
* python 3.7
* Flask-SQLAlchemy 2.4.4
* SQLAlchemy 1.3.13
* SqLite3
## How to run project
If you already installed requirements, the next step will be execute run.py. I used postman for sending requests.
## Some tests
Get all courses
![get_list_courses](images/get_list_courses.png)

Add course 

![add_course](images/add_course.png)

Erorr while adding course

![error_add_course](images/error_add_course.png)

Get course by id

![get_course_by_id](images/get_course_by_id.png)

Error with wrong id

![error_get_course_by_id](images/error_get_course_by_id.png)

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
