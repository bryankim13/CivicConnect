import datetime

from django.test import TestCase

from .models import Emailtempalate, Issue, Representative, User
# Create your tests here.

class EmailtemplateModelTests(TestCase):

    def test_was_published_recently_with_future_template(self):
        """
        was_published_recently() returns False for templates whose datecreated
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_template = Emailtempalate(datecreated=time)
        self.assertIs(future_template.was_published_recently(), False)

    def template_has_real_state(self):
        # returns False if the Emailtemplate's State does not exist
        states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
         "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", 
         "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        incorrect_state = Emailtempalate(state=AA)
        self.assertIs((incorrect_state.state in states), False)


class IssueModelTests(TestCase):

    def test_was_published_recently_with_future_issue(self):
        """
        was_published_recently() returns False for issues whose datecreated
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_issue = Issue(datecreated=time)
        self.assertIs(future_issue.was_published_recently(), False)

    def issue_has_real_state(self):
        # returns False if the Issue's State does not exist
        states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
         "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", 
         "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        incorrect_state = Issue(state=AA)
        self.assertIs((incorrect_state.state in states), False)

    def issue_has_real_district(self):
        #returns False if the Issue's District is in the incorrect format
        check = True
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        incorrect_district = Issue(state="VA", district="AA-a0")
        if incorrect_district.district[0:2] != incorrect_district.state:
            check = False
        if incorrect_district.district[2:3] != "-":
            check = False
        if (incorrect_district.district[3:4] not in numbers) or (incorrect_district.district[4:5].district not in numbers):
            check = False
        self.assertIs(check, False)


class RepresentativeModelTests(TestCase):

    def representative_has_real_state(self):
        # returns False if the Representative's State does not exist
        states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
         "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", 
         "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        incorrect_state = Representative(state=AA)
        self.assertIs((incorrect_state.state in states), False)

    def representative_has_real_district(self):
        #returns False if the Representative's District is in the incorrect format
        check = True
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        incorrect_district = Representative(state="VA", district="AA-a0")
        if incorrect_district.district[0:2] != incorrect_district.state:
            check = False
        if incorrect_district.district[2:3] != "-":
            check = False
        if (incorrect_district.district[3:4] not in numbers) or (incorrect_district.district[4:5].district not in numbers):
            check = False
        self.assertIs(check, False)

    def representative_email_is_correct_format(self):
        #returns False if the Representative's email is in the incorrect format
        check = True
        incorrect_email = Representative(email="test.com@gmail")
        atIndex = incorrect_email.email.find("@")
        dotIndex = incorrect_email.email.find(".")
        if atIndex is -1:
            check = False
        if dotIndex is -1:
            check = False
        if atIndex is 0:
            check = False
        if dotIndex = len(incorrect_email.email):
            check = False
        if (dotIndex - atIndex) < 2:
            check = False
        self.assertIs(check, False)
        

class UserModelTests(TestCase):
        
    def user_email_is_correct_format(self):
        #returns False if the User's email is in the incorrect format
        check = True
        incorrect_email = User(email="test.com@gmail")
        atIndex = incorrect_email.email.find("@")
        dotIndex = incorrect_email.email.find(".")
        if atIndex is -1:
            check = False
        if dotIndex is -1:
            check = False
        if atIndex is 0:
            check = False
        if dotIndex = len(incorrect_email.email):
            check = False
        if (dotIndex - atIndex) < 2:
            check = False
        self.assertIs(check, False)