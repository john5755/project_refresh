from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        # 추가 저장 필드: profile_image
        favorite_genre = data.get("favorite_genre")
        if favorite_genre:
            user.favorite_genre = favorite_genre
        
        favorite_season = data.get("favorite_season")
        if favorite_season:
            user.favorite_season = favorite_season



        user.save()
        return user