from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from peliculas.models import ComentarioJoker

class JokerListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_comment = 13

        for com_id in range(number_of_comment):
            ComentarioJoker.objects.create(
                descripcion=f'descripcion',
                comentario=f'comentario',
                fecha=f'2020-01-01',
            )
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('comentariojoker'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('comentariojoker'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peliculas/comentariojoker_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('comentariojoker'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['comentariojoker_list']) == 10)

    def test_lists_all_comments(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('comentariojoker')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['comentariojoker_list']) == 3)



    
        
    

