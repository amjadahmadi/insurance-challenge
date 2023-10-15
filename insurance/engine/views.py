from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserInsuranceSerializer


class UserInsuranceView(APIView):
    def post(self, request):
        obj = UserInsuranceSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        data = obj.save()
        return Response(data=data, status=200)
