from api.models import WildfireReport
import unittest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
import json
from django.core.exceptions import ObjectDoesNotExist

class TestWildfireReports(unittest.TestCase):

    def setUp(self):
        self.client = APIClient()
        self.test_id = None

    def a_test_create_report(self):
        url = reverse('WildfireReport')
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        report_data = '{"town":"TESTTOWN", "reported_by":"TESTREPORT", "contact_number":"540-867-5309"}'
        response = self.client.post(url, data=json.loads(report_data), headers=headers)
        response_data = json.loads(response.content)
        self.test_id = response_data['id']
        self.assertIn(b'id', response.content)  # id was returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def b_test_get_report(self):
        report = WildfireReport.objects.get(reported_by="TESTREPORT")
        url = reverse('WildfireReportParams', args=(report.id,))
        response = self.client.get(url)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['contact_number'], report.contact_number)

    def c_test_update_report(self):
        before_report = WildfireReport.objects.get(reported_by="TESTREPORT")

        url = reverse('WildfireReportParams', args=(before_report.id,))
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        report_data = '{"town":"TESTTOWN", "reported_by":"TESTREPORT", "contact_number":"changed"}'
        response = self.client.post(url, data=json.loads(report_data), headers=headers)

        after_report = WildfireReport.objects.get(reported_by="TESTREPORT")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("changed", after_report.contact_number)

    def d_test_delete_report(self):
        before_report = WildfireReport.objects.get(reported_by="TESTREPORT")

        url = reverse('WildfireReportParams', args=(before_report.id,))
        response = self.client.delete(url)

        exists = False
        if WildfireReport.objects.filter(reported_by="TESTREPORT").exists():
            exists = True

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(exists, False)
