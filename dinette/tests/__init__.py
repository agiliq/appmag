from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import Group, User
from django.core.urlresolvers import reverse

import urlparse

from .. import models
from dinette.models import SuperCategory


class Testmaker(TestCase):
    fixtures = ['test_data']

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        """Check if the homepage is accessible by all"""
        r = self.client.get(reverse('dinette_category'), {})
        self.assertEqual(r.status_code, 200)

    def test_index_page_visible_super_categories(self):
        sup_category_creator = User.objects.create_user(
                username='test', password='123', email='test@test.com')
        general = Group.objects.create(name='general')
        ordinary = Group.objects.create(name='ordinary')
        special = Group.objects.create(name='special')
        sup_category1 = SuperCategory.objects.create(
                name='super1', posted_by=sup_category_creator)
        sup_category1.accessgroups.add(general)
        sup_category2 = SuperCategory.objects.create(
                name='super2', posted_by=sup_category_creator)
        sup_category2.accessgroups.add(ordinary, special)
        sup_category3 = SuperCategory.objects.create(
                name='super3', posted_by=sup_category_creator)

        r = self.client.get(reverse('dinette_category'), {})
        self.assertContains(r, "super1")
        self.assertNotContains(r, "super2")

        user = User.objects.create_user(
                username='user', password='pass')
        user.groups.add(ordinary)
        self.client.login(username='user', password='pass')
        r = self.client.get(reverse('dinette_category'))
        self.assertContains(r, "super1")
        self.assertContains(r, "super2")
        self.assertNotContains(r, "super3")

    def test_new_topics(self):
        r = self.client.get(reverse('dinette_new_for_user'))
        #check for redirection for guest users
        self.assertEqual(r.status_code, 302)
        #check for results in case of loggedin users
        r = self.client.login(username='plaban', password='plaban') #this is in test fixture
        self.assertEqual(r, True)
        r = self.client.get(reverse('dinette_new_for_user'))
        self.assertEqual( len(r.context['new_topic_list']), 0) # as there are no entry in the db


    def test_dinette_active(self):
        r = self.client.get(reverse('dinette_active'))
        self.assertEqual(r.status_code, 200)

    def test_subscribe_to_digest(self):
        r = self.client.get(reverse('dinette_subscribe_to_digest'))
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r['location'].split("=")[1],
                reverse('dinette_subscribe_to_digest'))

        r = self.client.login(username='plaban',password='plaban') #this is in test fixture
        self.assertEqual(r, True)

        r = self.client.get(reverse('dinette_subscribe_to_digest'))
        self.assertEqual(r.status_code, 302)
        self.assertEqual(urlparse.urlparse(r['location']).path, reverse('dinette_user_profile',
            args=['plaban']))



    def test_unsubscribe_from_digest(self):
        r = self.client.get(reverse('dinette_unsubscribe_from_digest'))
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r['location'].split("=")[1],
                reverse('dinette_unsubscribe_from_digest'))

        r = self.client.login(username='plaban',password='plaban') #this is in test fixture
        self.assertEqual(r, True)

        r = self.client.get(reverse('dinette_subscribe_to_digest'))
        self.assertEqual(r.status_code, 302)
        self.assertEqual(urlparse.urlparse(r['location']).path, reverse('dinette_user_profile',
            args=['plaban']))


    def test_unanswered_topics(self):
        r = self.client.get(reverse('dinette_unanswered'))
        topic =  r.context['new_topic_list'][0]
        self.assertEqual(topic.subject,'Details about the Django design patterns')


    def test_user_profile(self):
        response = self.client.get(reverse('dinette_user_profile', kwargs={'slug':'plaban'}))
        user =  response.context['user_profile']
        self.assertEqual(user.email,'plaban.nayak@gmail.com')

    def test_category(self):
        response = self.client.get(reverse('dinette_index', kwargs={'categoryslug':'dinette'}))
        category =  response.context['category']
        self.assertEqual(category.name,"Dinette")
        self.assertEqual(category.description,"Dinette is the best forum app for Django, Period. You are using it right now.")
        supercategory = category.super_category
        self.assertEqual(supercategory.name,"Python and Django")

    def test_post_topic(self):
        self.client.login(username='plaban', password='plaban')
        response = self.client.post(reverse('dinette_posttopic'),
            {'subject':'python','message':'this is python',
            'message_markup_type':'plain', 'authenticated':'true',
            'categoryid':'1'})
        response = self.client.get(reverse('dinette_active'))
        topic = response.context['new_topic_list'][0]
        self.assertEqual(topic.subject, 'python')

    def test_post_reply(self):
        response = self.client.login(username='plaban', password='plaban')
        response = self.client.post(reverse('dinette_postreply'), {'message':'this is good', 'message_markup_type':'plain',
                                                         'authenticated':'True', 'topicid':'1'})
	self.assertEqual(response.status_code, 200)


    def test_edit_reply(self):
        response = self.client.login(username = "plaban", password = "plaban")
        response = self.client.get(reverse('dinette_editreply', kwargs={'reply_id': '1'}))
        self.assertEqual(response.status_code, 200)
        reponse = self.client.post(reverse('dinette_editreply', kwargs={'reply_id': '1'}), {'message':'this is the edit reply', 'message_markup_type':'plain'})
        self.assertEqual(response.status_code, 200)
        reply = models.Reply.objects.all()[0]
        self.assertEqual(str(reply),'<p>this is the edit reply</p>')
