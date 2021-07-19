from django import forms
LC = [('Dynamic Programming','Dynamic Programming') ,
('Greedy','Greedy') ,
('Ad-hoc','Ad-hoc')]
company = [('Google' , 'Google'),
('Microsoft','Microsoft'),
('Apple','Apple')]
class questionadd(forms.Form):
    qname = forms.CharField()
    qtype = forms.CharField()
    qdescrip =forms.CharField()
    qtopic = forms.CharField(widget=forms.Select(choices=LC))
    qlink = forms.URLField()
class queryhandle(forms.Form):
    handle = forms.CharField()
class experienceadd(forms.Form):
    companyexp=forms.CharField(widget = forms.Select(choices=company))
    nameofperson = forms.CharField()
    nameofcollege = forms.CharField()
    typeofrole = forms.CharField()
    experience = forms.CharField()
