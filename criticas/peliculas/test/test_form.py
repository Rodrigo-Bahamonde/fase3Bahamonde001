from django.test import SimpleTestCase
from peliculas.forms import ComentarioForm

class TestForms(SimpleTestCase):

    def test_comentario_form_valid_data(self):
        form = ComentarioForm(data={
            'descripcion': 'Descripcion de prueba',
            'comentario': 'Este es un comentario de prueba',
            'fecha': '2020-01-01',
            'usuario': 'prueba',
        })

        self.assertTrue(form.is_valid())



    def test_comentario_form_no_data(self):
        form = ComentarioForm(data={})


        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),4)