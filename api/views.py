import random
import string

from rest_framework.response import Response
from rest_framework.decorators import api_view
from moflow.mflow.generate import get_mols

@api_view(['POST'])
def generate_with_keyword(request):
    content = {}
    random_formulae = []
    if request.data and request.data['keyword']:
        # moflow 실행
        mols = get_mols()
        content['keyword'] = request.data['keyword']
        random_formulae = mols
    content['data'] = random_formulae
    return Response(content)
    
