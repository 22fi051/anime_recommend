from django import forms

class AnimeSearchForm(forms.Form):
    genres = forms.ChoiceField(choices=[('Action', 'Action'),
                                        ('Adventure', 'Adventure'),
                                        ('Comedy', 'Comedy'),
                                        ('Drama', 'Drama'),
                                        ('Fantasy', 'Fantasy'),
                                        ('Magic', 'Magic'),
                                        ('Mystery', 'Mystery'),
                                        ('Psychological', 'Psychological'),
                                        ('Romance', 'Romance'),
                                        ('Sci-Fi', 'Sci-Fi'),
                                        ('Sports', 'Sports'),
                                        ('Horror', 'Horror'),
                                        ('Military', 'Military'),
                                        ('Historical', 'Historical'),
                                        ('Kids', 'Kids'),
                                        ('Music', 'Music'),
                                        ('Samurai', 'Samurai'),
                                        ('School', 'School'),
                                        ('Game', 'Game')],label='好きなジャンル', required=False)
    episodes = forms.ChoiceField(choices=[('物語は長いほうが好き', '物語は長いほうが好き'),
                                            ('物語は短いほうが好き', '物語は短いほうが好き')], label='エピソード数', required=False, widget=forms.RadioSelect)
    start_date = forms.ChoiceField(choices=[('2010年代', '2010年代'),('2000年代', '2000年代'), ('1990年代', '1990年代')], label='放送開始年代', required=False, widget=forms.RadioSelect)
    
    