# from django import forms
# from .models import Product, StoveFeature, WindowFeature

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['stove_feature', 'window_feature', 'sku', 'name', 'description', 'price', 'image_url', 'image']

#     def __init__(self, *args, **kwargs):
#         super(ProductForm, self).__init__(*args, **kwargs)
#         self.fields['stove_feature'].queryset = StoveFeature.objects.all()
#         self.fields['window_feature'].queryset = WindowFeature.objects.all()

#     stove_feature = forms.ModelChoiceField(
#         queryset=StoveFeature.objects.all(),
#         empty_label='Select a Stove Feature',
#         required=False
#     )

#     window_feature = forms.ModelChoiceField(
#         queryset=WindowFeature.objects.all(),
#         empty_label='Select a Window Feature',
#         required=False
#     )