from django import forms


class userForm(forms.ModelForm):
    #my_choices = forms.MultipleChoiceField(choices=CHOICES)
   
    Search_For_EDV = forms.CharField(max_length=12)

    def __init__(self, *args, **kwargs):       
        super(userForm, self).__init__(*args, **kwargs)
    

    # def clean_lead_fields(self):
    #     return ','.join(self.cleaned_data.get('my_choices', []))

