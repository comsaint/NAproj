from django.contrib import admin

# Import your models here.
from vote.models import Question

# Register your models here.
#admin.site.register(Question) #simple

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,                 {'fields':['question_title','question_description']}),
                ('Date information',   {'fields':['pub_date'],'classes':['collapse']}),
                 ('Voting result',   {'fields':['vote_count_YES','vote_count_NO','vote_count_ABSTAIN']}),
            ]
    list_display = ('question_title','pub_date','was_published_recently','vote_count_YES','vote_count_NO','vote_count_ABSTAIN')
    #inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_title']
admin.site.register(Question, QuestionAdmin)

#admin.site.register(Choice)