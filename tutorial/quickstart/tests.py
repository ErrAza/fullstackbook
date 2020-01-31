from rest_framework.test import APITestCase


class ProjectsTestCase(APITestCase):

    def simple_projects_test(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, 200)