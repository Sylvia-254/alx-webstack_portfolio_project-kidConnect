from django.test import TestCase

# Create your tests here.
class SimpleTests(TestCase):
    def test_report_page_status_code(self):
        responseReport = self.client.get('/report/')
        self.assertEqual(responseReport.status_code, 200)
    def test_reported_page_status_code(self):
        responseReported = self.client.get('/reported/')
        self.assertEqual(responseReported.status_code, 200)
    def test_base_page_status_code()