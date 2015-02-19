from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Question(models.Model):
    question_title = models.CharField(max_length=200)
    question_description = models.TextField(max_length=5000,default='No decription.')
    pub_date = models.DateTimeField('date published')
    
    CHOICE_TEXT = (['YES','NO','ABSTAIN'])
    vote_count_YES = models.IntegerField(default=0,db_column=CHOICE_TEXT[0])
    vote_count_NO = models.IntegerField(default=0,db_column=CHOICE_TEXT[1])
    vote_count_ABSTAIN = models.IntegerField(default=0,db_column=CHOICE_TEXT[2])
    
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    #stub test
#     def __init__(self):
#         self.a_stub = StubClass
#         self.a_stub.someMethod()
    
    def __str__(self):              # __unicode__ on Python 2
        return self.question_title

# class StubClass(models.Model):
#     SOME_TEXT = ['abc','123']
#     def someMethod(self):
#         print('Oh my goodness!')

# class Choice(models.Model):
#     question = models.ForeignKey(Question) #models.ForeignKey(X) implies each CHOICE is corresponded to one X
#      
#     CHOICE_TEXT = (['YES','NO','ABSTAIN'])
#     vote_count_YES = models.IntegerField(default=0,db_column=CHOICE_TEXT[0])
#     vote_count_NO = models.IntegerField(default=0,db_column=CHOICE_TEXT[1])
#     vote_count_ABSTAIN = models.IntegerField(default=0,db_column=CHOICE_TEXT[2])
#             
#     def __str__(self):              # __unicode__ on Python 2
#         return "-".join(self.CHOICE_TEXT)
        
