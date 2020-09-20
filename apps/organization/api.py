from post_office import mail

from rest_framework import status, viewsets, views
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import (Organization,)
from .serializers import (OrganizationSerializer, )


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filterset_fields = ('is_active', 'nama')
    pagination_class = None
    permission_classes = (IsAuthenticated,)


class SendEmailViewSet(views.APIView):
    def post(self, request):
        email_to = self.request.data.get('receiver')

        mail.send(
            email_to,  # List of email addresses also accepted
            'azharnian@gmail.com',
            subject='hay',
            message='Welcome home, {{ name }}!',
            html_message='Welcome home, <b>{{ name }}</b>!',
            headers={'Reply-to': 'reply@example.com'},
            # scheduled_time=date(2014, 1, 1),
            context={'name': 'Alice'},
            priority='now',
        )
        return Response(email_to)
