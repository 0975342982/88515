# -*- coding: UTF-8 -*-
from django import forms
from web.models import Diary, Money


# 日誌表單
class DiaryForm(forms.ModelForm):
        class Meta:
                model = Diary
                fields = ['memo']
# 帳本表單
class MoneyForm(forms.ModelForm):
        RELEVANCE_CHOICES = (
                (1, "1份"),
                (2, "2份"),
                (3, "3份"),
                (4, "4份"),
                (5, "5份"),
                (6, "6份"),
                (7, "7份"),
                (8, "8份"),
                (9, "9份"),
                (10, "10份"),
                (11, "11份"),
                (12, "12份"),
                (13, "13份"),
                (14, "14份"),
                (15, "15份以上"),
        )
        kind = forms.ChoiceField(choices = RELEVANCE_CHOICES, required=True)

        class Meta:
                model = Money
                fields = ['item', 'kind', 'price']

        def __init__(self, *args, **kwargs):
                super(MoneyForm, self).__init__(*args, **kwargs)
                self.fields['item'].label = "神抹味的嘎理"
                self.fields['kind'].label = "ㄘ了幾份"
                self.fields['price'].label = "費用"
                
# 使用者登入表單
class LoginForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)

        def __init__(self, *args, **kwargs):
                super(LoginForm, self).__init__(*args, **kwargs)
                self.fields['username'].label = "帳號"
                self.fields['password'].label = "密碼"                