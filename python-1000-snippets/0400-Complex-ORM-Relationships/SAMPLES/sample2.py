# sample2.py
# Demonstrates a many-to-many relationship using SQLAlchemy.

import subprocess
import sys


def ensure_sqlalchemy():
    try:
        import sqlalchemy  # type: ignore
        return sqlalchemy
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "sqlalchemy"])  # nosec
        import sqlalchemy  # type: ignore
        return sqlalchemy


def main() -> None:
    sqlalchemy = ensure_sqlalchemy()
    from sqlalchemy import Column, Integer, String, Table, ForeignKey
    from sqlalchemy.orm import declarative_base, relationship, Session

    Base = declarative_base()

    association = Table(
        "association",
        Base.metadata,
        Column("student_id", Integer, ForeignKey("student.id")),
        Column("course_id", Integer, ForeignKey("course.id")),
    )

    class Student(Base):
        __tablename__ = "student"
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        courses = relationship("Course", secondary=association, back_populates="students")

        def __repr__(self):
            return f"<Student(id={self.id}, name={self.name})>"

    class Course(Base):
        __tablename__ = "course"
        id = Column(Integer, primary_key=True)
        title = Column(String, nullable=False)
        students = relationship("Student", secondary=association, back_populates="courses")

        def __repr__(self):
            return f"<Course(id={self.id}, title={self.title})>"

    engine = sqlalchemy.create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        alice = Student(name="Alice")
        bob = Student(name="Bob")
        math = Course(title="Math")
        science = Course(title="Science")

        alice.courses.append(math)
        alice.courses.append(science)
        bob.courses.append(science)

        session.add_all([alice, bob, math, science])
        session.commit()

        for student in session.query(Student).all():
            print(student, "courses:", [c.title for c in student.courses])


if __name__ == "__main__":
    main()
