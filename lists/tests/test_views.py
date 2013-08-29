from django.test import TestCase
from django.utils.html import escape

from lists.forms import ItemForm
from lists.models import Item, List

class HomePageTest(TestCase):

    def test_home_page_renders_home_template_with_form(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        self.assertIsInstance(response.context['form'], ItemForm)


class NewListTest(TestCase):

    def test_saving_a_POST_request(self):
        self.client.post(
            '/lists/new',
            data={'text': 'A new list item'}
        )
        self.assertEqual(List.objects.all().count(), 1)
        new_list = List.objects.all()[0]
        self.assertEqual(Item.objects.all().count(), 1)
        new_item = Item.objects.all()[0]
        self.assertEqual(new_item.text, 'A new list item')
        self.assertEqual(new_item.list, new_list)


    def test_redirects_after_POST(self):
        response = self.client.post(
            '/lists/new',
            data={'text': 'A new list item'}
        )
        new_list = List.objects.all()[0]
        self.assertRedirects(response, '/lists/%d/' % (new_list.id,))


    def test_validation_errors_sent_back_to_home_page_template(self):
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertEqual(Item.objects.all().count(), 0)
        self.assertTemplateUsed(response, 'home.html')
        expected_error =  escape("You can't have an empty list item")
        self.assertContains(response, expected_error)



class ListViewTest(TestCase):

    def test_list_view_passes_list_to_list_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.get('/lists/%d/' % (correct_list.id,))

        self.assertTemplateUsed(response, 'list.html')
        self.assertEqual(response.context['list'], correct_list)


    def test_list_view_displays_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text='other list item 1', list=other_list)
        Item.objects.create(text='other list item 2', list=other_list)

        response = self.client.get('/lists/%d/' % (correct_list.id,))

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2')


    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            '/lists/%d/' % (correct_list.id,),
            data={'text': 'A new item for an existing list'}
        )

        self.assertEqual(Item.objects.all().count(), 1)
        new_item = Item.objects.all()[0]
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)


    def test_POST_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.post(
            '/lists/%d/' % (correct_list.id,),
            data={'text': 'A new item for an existing list'}
        )
        self.assertRedirects(response, '/lists/%d/' % (correct_list.id,))


    def test_empty_item_validation_errors_end_up_on_lists_page(self):
        listey = List.objects.create()
        response = self.client.post(
            '/lists/%d/' % (listey.id,),
            data={'text': ''}
        )
        self.assertEqual(Item.objects.all().count(), 0)
        self.assertTemplateUsed(response, 'list.html')
        expected_error =  escape("You can't have an empty list item")
        self.assertContains(response, expected_error)


    def test_duplicate_item_validation_errors_end_up_on_lists_page(self):
        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1, text='textey')
        response = self.client.post(
            '/lists/%d/' % (list1.id,),
            data={'text': 'textey'}
        )

        self.assertEqual(Item.objects.all().count(), 1)
        self.assertTemplateUsed(response, 'list.html')
        expected_error =  escape("You've already got this in your list")
        self.assertContains(response, expected_error)

