from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View  # for the index page
from rest_framework import status
from django.shortcuts import render

from .models import WildfireReport
from .serializers import WildfireReportSerializer


class Index(View):

    def get(self, request):
        return render(request, 'index.html')


class WildfireReportView(APIView):
    """ Manage WildfireReport resources """

    def get(self, request, pk=None):
        """ List all wildfire reports or look up a specific report
            GET /WildfireReport/: returns list of reports
            GET /WildfireReport/<str:pk>/: returns details of selected report
        """
        if pk is None:  # show all reports
            reports = WildfireReport.objects.all()
            serializer = WildfireReportSerializer(reports, many=True)
            return Response(serializer.data)

        else:  # look up specific report
            report = WildfireReport.objects.get(id=pk)
            if report:
                serializer = WildfireReportSerializer(report, many=False)
                return Response(serializer.data)
            else:  # can't find report
                return Response(
                    {"message": f"Wildfire with id: {pk} not found!"})

    def post(self, request, pk=None):
        """ Create / update wildfire reports
                POST /WildfireReport/: create a new report
                POST /WildfireReport/<str:pk>/: update an existing WildfireReport with id = pk
        """
        if pk is None:  # create new report
            if request.data is not None:
                serializer = WildfireReportSerializer(data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:  # JSON couldn't be serialized
                    return Response(
                        {"message": "Data could not be serialized!"},
                        status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            else:  # no JSON data provided
                return Response(
                    {"message": "Report definition not provided!"})

        else:  # pk provided, update existing report
            report = WildfireReport.objects.get(id=pk)

            if not report:  # selected report not found
                return Response(
                    {"message": f"Wildfire report with id: {pk} not found!"})

            if request.data is not None:
                serializer = WildfireReportSerializer(instance=report, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:  # JSON couldn't be serialized
                    return Response(
                        {"message": "Data could not be serialized!"},
                        status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            else:  # no JSON data provided
                return Response(
                    {"message": "Report JSON is missing!"})

    def delete(self, request, pk=None):
        if pk is None:
            return Response(
                {"message": f"Missing report id!"})
        else:
            report = WildfireReport.objects.get(id=pk)
            if not report:
                return Response(
                    {"message": f"Report with id: {pk} not found!"})
            else:
                report.delete()
                return Response({"message": f"Wildfire report {pk} deleted successfully!"})

