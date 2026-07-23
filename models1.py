from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    attendances = db.relationship(
        "Attendance",
        back_populates="student"
    )


class Lecture(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    subject = db.Column(db.String(100), nullable=False)

    attendances = db.relationship(
        "Attendance",
        back_populates="lecture"
    )


class Attendance(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("student.id")
    )

    lecture_id = db.Column(
        db.Integer,
        db.ForeignKey("lecture.id")
    )

    status = db.Column(db.String(20))

    student = db.relationship(
        "Student",
        back_populates="attendances"
    )

    lecture = db.relationship(
        "Lecture",
        back_populates="attendances"
    )