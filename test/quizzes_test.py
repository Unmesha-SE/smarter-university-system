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
        

if __name__ == '__main__':
    unittest.main()