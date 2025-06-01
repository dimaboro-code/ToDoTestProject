from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

from .models import TechParkCompany
from .serializers import TechParkCompanySerializer
from .utils import parse_techpark_table


class TechParkParseView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        data = parse_techpark_table(limit=10)
        created = 0

        for item in data:
            obj, created_flag = TechParkCompany.objects.get_or_create(
                certificate_number=item["certificate_number"], defaults=item
            )
            if created_flag:
                created += 1

        return Response(
            {"message": f"Импортировано {created} компаний."},
            status=status.HTTP_201_CREATED,
        )


class TechParkCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TechParkCompany.objects.all().order_by("certificate_number")
    serializer_class = TechParkCompanySerializer
    permission_classes = [permissions.IsAuthenticated]
