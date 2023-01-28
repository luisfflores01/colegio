

class MyModelForm(forms.ModelForm):
    other_model = forms.ModelChoiceField(queryset=OtherModel.objects.none())

    class Meta:
        model = MyModel
        fields = ['other_model', 'other_fields']