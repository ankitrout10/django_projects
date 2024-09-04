from django import forms

class Feedback(forms.Form):
    sid=forms.IntegerField()
    name=forms.CharField(max_length=20)
    branch=forms.CharField(max_length=20)
    comment=forms.CharField()

    def clean_name(self):
        user_name=self.cleaned_data['name']
        if len(user_name)<2:
            raise forms.ValidationError('Name must be atleast two characters long')
        return user_name
    
    def clean_comment(self):
        user_comment=self.cleaned_data['comment']
        if len(user_comment)<20:
            raise forms.ValidationError('Comment must be atleast twenty or more characters long')
        return user_comment
    