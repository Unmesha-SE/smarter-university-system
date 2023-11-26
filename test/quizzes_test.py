import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        This test attempts to add a quiz with multiple titles (list input).
        The program crashes in file 'quizzes_controller.py', line 63 (add_quiz).
        """
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz(["Quiz #1", "Quiz #2"], "This is the first quiz.", 2023-11-24, 2023-11-25)
        quiz = self.ctrl.get_quiz_by_id(quiz_id)
        self.assertIsNone(quiz, 'Expecting no Quiz to be returned.')

    def test_expose_failure_02(self):
        """
        This test attempts to modify a Quiz's 'last_updated' parameter to an invalid value (string) after it has been created.
        The program crashes in file 'quizzes_controller.py' line 66 (add_quiz), and in file 'assignments.py' line 83 (to_json)
        """
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz("Quiz #1", "This is the first quiz.", 2023-11-24, 2023-11-25)
        self.ctrl.quizzes[0].last_updated = 'hi'
        quiz_id2 = self.ctrl.add_quiz("Quiz #2", "This is the second quiz.", 2023-11-25, 2023-11-26)
        quizzes = self.ctrl.get_quizzes()
        self.assertGreater(len(quizzes), 0, 'Expecting one or more Quizzes to be returned.')
        

if __name__ == '__main__':
    unittest.main()