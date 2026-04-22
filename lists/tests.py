from django.test import TestCase
from django.http import HttpRequest #1
from lists.views import home_page 

# Create your tests here.

class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        #1-We import the HttpRequest class so that we can then create a request object within our test. This is the kind of object that Django will create when a user’s browser asks for a page.
        #2-We pass the HttpRequest object to our home_page view, which gives us a response. You won’t be surprised to hear that the response is an instance of a class called HttpResponse.
        #3-Then, we extract the .content of the response. These are the raw bytes, the ones and zeros that would be sent down the wire to the user’s browser. We call .decode() to convert them into the string of HTML that’s being sent to the user.
        #4-Now we can make some assertions: we know we want an HTML <title> tag somewhere in there, with the words "To-Do lists" in it—​because that’s what we specified in our FT.
        #5-And we can do a vague sense-check that it’s valid HTML by checking that it starts with an <html> tag, which gets closed at the end.
        request = HttpRequest() #1
        response = home_page(request) #2
        html = response.content.decode("utf-8") #3
        self.assertIn("<title>To-Do lists</title>", html) #4
        self.assertTrue(html.startswith("<html>")) #5
        self.assertTrue(html.endswith("</html>")) #5

