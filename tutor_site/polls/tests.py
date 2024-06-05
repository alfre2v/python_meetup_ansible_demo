import datetime

from django.utils import timezone

from django.test import TestCase

from .models import Question

# Create your tests here.


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_date(self):
        """
        check was_published_recently() returns False for questions whose pub_date is in the future
        """
        future_time = timezone.now() + datetime.timedelta(days=1)
        future_question = Question(pub_date=future_time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        check was_published_recently() returns False for questions whose pub_date is more than 1 day old
        """
        old_time = timezone.now() - datetime.timedelta(days=2)
        old_question = Question(pub_date=old_time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_new_question(self):
        """
        check was_published_recently() returns True for questions whose pub_date is less than 1 day old
        """
        recent_time = timezone.now() - datetime.timedelta(days=0.5)
        recent_question = Question(pub_date=recent_time)
        self.assertIs(recent_question.was_published_recently(), True)

