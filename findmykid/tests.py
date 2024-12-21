from django.test import TestCase
from .models import Report
from django.core.files import File

# Create your tests here.
class SimpleStatusCodesTests(TestCase):
    def test_report_page_status_code(self):
        responseReport = self.client.get('/report/')
        self.assertEqual(responseReport.status_code, 200)
    def test_reported_page_status_code(self):
        responseReported = self.client.get('/reported/')
        self.assertEqual(responseReported.status_code, 200)
    def test_base_page_status_code(self):
        responseBase = self.client.get('/base/')
        self.assertEqual(responseBase.status_code, 200)


class ReportModelTest(TestCase):
    def setUp(self):
        Report.objects.create(firstName="Sila", age=5, height=1)
         
    def test_firstName_content(self):
        report = Report.objects.get(id=1)
        expectedFirstName = f'{report.firstName}'
        self.assertEqual(expectedFirstName, "Sila")
    def test_Height_content(self):
        report = Report.objects.get(id=1)
        expected_height = f"{report.height}"
        self.assertEqual = (expected_height, 5)