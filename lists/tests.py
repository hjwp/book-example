from django.test import TestCase


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_post_saves_items(self):
        self.client.post("/", data={"item_text": "onions"})
        response1 = self.client.get("/")
        self.assertContains(response1, "onions")

    def test_multiple_posts_save_all_items(self):
        self.client.post("/", data={"item_text": "onions"})
        self.client.post("/", data={"item_text": "carrots"})
        response = self.client.get("/")
        self.assertContains(response, "onions")
        self.assertContains(response, "carrots")

    def test_no_items_by_default(self):
        response = self.client.get("/")
        self.assertContains(
            response,
            '<table id="id_list_table"></table>',
            html=True,
        )
