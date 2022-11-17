import random
import string

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def generate_with_keyword(request):
    content = {}
    random_formulae = []
    if request.data and request.data['keyword']:
        # moflow 실행
        content['keyword'] = request.data['keyword']
        random_formulae = [(''.join(random.choice(string.ascii_uppercase) for _ in range(10))) for _ in range(10)]
    content['data'] = random_formulae
    return Response(content)
    
