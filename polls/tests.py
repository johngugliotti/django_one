from django.test import TestCase
import datetime
from django.utils import timezone
from polls.models import Question


from django.core.urlresolvers import reverse

class QuestionMethodTests(TestCase) :
    def test_was_published_recently_with_future_question(self) :

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)




def create_question(question_text , days ) : 
    time=timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text = question_text, pub_date = time ) 

class QuestionViewTests(TestCase) :
    def test_index_view_with_no_questions(self) :
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])    
    def test_index_view_with_a_past_question(self) :
        create_question("Past Question.",-30) 
        response =self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Past Question.>'] )
    
    
    def test_index_view_with_a_future_question(self) :     
        create_question("Future Question", 30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.", status_code = 200) 
        self.assertQuerysetEqual(response.context['latest_question_list'],[]) 
    
    def test_index_view_with_future_question_and_past_question(self) :
        create_question("Past question 1." , -30)
        create_question("Future question 2.", 30) 
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 1.>']
        )
    def test_index_view_with_two_past_questions (self) : 
        create_question("Past Question 1", -30)
        create_question("Past Question 2", -5) 
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual( response.context['latest_question_list'], ['<Question: Past Question 2>', '<Question: Past Question 1>']) 
        
class QuestionIndexDetailTests(TestCase) :
    def test_detail_view_with_a_future_question(self) :
        future_question = create_question('Future question.',5)
        response = self.client.get(reverse('polls:detail',args = (future_question.id,)))
        self.assertEqual(response.status_code, 404)
    def test_detail_view_with_a_past_question(self) :
        past_question = create_question('Past Question',-5) 
        response = self.client.get(reverse('polls:detail',args = (past_question.id,))) 
        self.assertContains(response, past_question.question_text, status_code = 200)

