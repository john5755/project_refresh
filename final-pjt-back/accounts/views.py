from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import HistorySerializer, ProfileSerializer
from accounts import serializers
from .models import History


User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)

    return Response(serializer.data)
    
@api_view(['GET'])
def update_history(request, user_pk, partner_pk):

    user = get_object_or_404(User,pk=user_pk)
    partner = get_object_or_404(User, pk=partner_pk)

    history = History(user_1=user, user_2=partner)
    history.save()
    
    #user 모델에 partner_id 넣어주기
    user.partner_id = partner_pk
    partner.partner_id = user_pk
    user.save()
    partner.save()


    # history2 = get_list_or_404(History, user_1=user)
    # serializer = HistorySerializer(history2)

    sibal = {'a': '아아아ㅣ아아ㅏ아아아아아아아아ㅏㅇ'}

    return Response(sibal)

@api_view(['POST'])
def reset_history(request, user_pk, partner_pk ):
    user = get_object_or_404(User,pk=user_pk)
    partner = get_object_or_404(User, pk=partner_pk)
    try:
        #날짜 먼저 찾기
        first_date = (History.objects.filter(user_1 = user, user_2 = partner) | History.objects.filter(user_1 = partner, user_2 = user)).order_by('login_date')[0].login_date
        
        # partner와 첫 데이트 이후 partner가 영화본 횟수
        partner_count = (History.objects.filter(user_1 = partner) | History.objects.filter(user_2 = partner,)).filter(login_date__gte=first_date).count()
        
        # 탈퇴하려는 'user'의 전체 기록 삭제
        user_history = (History.objects.filter(user_1 = user) | History.objects.filter(user_2 = user,))
        user_history.delete()

        # user partner 같이 영화본 횟수
        together_count = (History.objects.filter(user_1 = user, user_2 = partner) | History.objects.filter(user_1 = partner, user_2 = user)).count()
    except:
        partner_count = 0
        together_count = 0
    
    context = {
        'partner_count':partner_count,
        'together_count':together_count
    }
    
    return Response(context)

#user 탈퇴(삭제)
@api_view(['DELETE'])
def delete_user(request,user_pk):
    user = get_object_or_404(User, pk=user_pk)
    user.delete()

    context = {
        'message' : user_pk
        }
    return Response(context)