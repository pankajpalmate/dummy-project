from django import forms
class Newentryform(forms.Form):
    name=forms.CharField(label="Patient name",max_length=50)
    contact=forms.IntegerField(label="Contact")
    referred_by=forms.CharField(label="Referred by")

    fees=forms.IntegerField(label="Fees")
class Searchentryform(forms.Form):
    name=forms.CharField(label="Patient name",max_length=50)
