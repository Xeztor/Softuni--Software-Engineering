import unittest

# from student.project.student import Student
# For Judge
from project.student import Student


class StudentTest(unittest.TestCase):
    def setUp(self):
        self.student = Student('pesho')

    def test_student_enroll_when_course_name_not_in_courses_list_and_not_adding_notes__expect_to_add_course_to_list_of_courses_with_blank_notes_and_return_msg(
            self):
        msg = self.student.enroll('Python OOP', [], 'N')
        self.assertEqual({'Python OOP': []}, self.student.courses)
        self.assertEqual("Course has been added.", msg)

    def test_student_enroll_when_course_name_not_in_courses_list_and_adding_notes__expect_to_add_course_to_list_of_courses_with_notes_and_return_msg(
            self):
        # Test for add_course_notes = "Y"
        msg = self.student.enroll('Python OOP', ['note'], 'Y')
        self.assertEqual({'Python OOP': ['note']}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", msg)

        # Test for add_course_notes = ""
        msg = self.student.enroll('Python Advanced', ['second'], '')
        self.assertEqual({'Python OOP': ['note'], 'Python Advanced': ['second']}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", msg)

    def test_student_enroll_when_course_name_in_courses_list_and_adding_notes__expect_to_add_notes_list_and_return_msg(
            self):
        self.student.courses = {'Python OOP': []}
        msg = self.student.enroll('Python OOP', ['note'])

        self.assertEqual({'Python OOP': ['note']}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", msg)

    def test_student_add_notes_when_course_name_in_courses_list__expect_to_add_notes_list_and_return_msg(self):
        self.student.enroll('Python OOP', [])
        msg = self.student.add_notes('Python OOP', 'notes')
        self.assertEqual(self.student.courses, {'Python OOP': ['notes']})
        self.assertEqual("Notes have been updated", msg)

    def test_student_add_notes_when_course_name_not_in_courses_list__expect_exception(self):
        with self.assertRaises(Exception) as exc:
            self.student.add_notes('Python OOP', 'notes')

        self.assertEqual("Cannot add notes. Course not found.", str(exc.exception))

    def test_student_leave_course_when_course_in_courses_list__expect_to_remove_course_from_course_list_and_return_msg(
            self):
        self.student.enroll('Python OOP', [])
        msg = self.student.leave_course('Python OOP')
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", msg)

    def test_student_leave_course_when_course_not_in_courses_list__expect_exception(self):
        with self.assertRaises(Exception) as exc:
            self.student.leave_course('Python OOP')

        self.assertEqual("Cannot remove course. Course not found.", str(exc.exception))


if __name__ == '__main__':
    unittest.main()
