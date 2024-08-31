from django import forms
from .models import  Login , Product
from django.forms import TextInput,  PasswordInput , FileInput ,Select

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username' , 'password']
        widgets = {
            'username':TextInput(
                attrs={
                        "type":"text" ,
                        "class":"form-control" ,
                        "aria-label":"Sizing example input" ,
                        "aria-describedby":"inputGroup-sizing-default",
                        "placeholder" : "ENTER USERNAME & PASSWORD",
                }
            ),
            'password': PasswordInput(
                attrs={
                        "type":"text",
                        "class":"form-control",
                        "aria-label":"Sizing example input", 
                        "aria-describedby":"inputGroup-sizing-default"
                }
            ),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['item' ,'des','price','sales_price','stock', 'img' , 'cate']
        widgets = {
            'item' : TextInput(
                attrs={
                    "type":"text",
                    "class":"form-control",
                    "placeholder":"Item",
                    "aria-label":"Username",
                    "aria-describedby":"basic-addon1"
                }
            ),
            'des' : TextInput(
                attrs={
                    "class":"form-control" ,
                    "placeholder":"Description",
                    "aria-label":"With textarea"
                }
            ),
            'price' : TextInput(
                attrs={
                    "type":"text",
                    "placeholder":"PRICE",
                    "class":"form-control",
                    "aria-label":"Amount (to the nearest dollar)"
                }
            ),
            'sales_price' : TextInput(
                attrs = {
                    "type":"text",
                    "placeholder":"Sale Price",
                    "class":"form-control",
                    "aria-label":"Amount (to the nearest dollar)"
                }
            ),
            'stock' : TextInput(
                attrs={
                    "type":"text",
                    "placeholder":"Stock",
                    "class":"form-control",
                    "aria-label":"Server"
                }
            ),
            'img' : FileInput(
                attrs={
                    "class":"form-control",
                    "name":"email",
                    "placeholder":"Upload Image",
                    "type":"file"
                }
            ),
            'cate' :  Select(
               attrs={
                   "name":"doctors",
                   "class":"form-select"
               }
            )
        }
        