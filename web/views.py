from datetime import datetime
from blog import settings
from django.shortcuts import render, redirect
from web.models import Publication, Message, CommentsPublication, CommentsContacts


def index(request):
    return render(request, 'index.html')


def contacts(request):
    comments_contacts_objects = CommentsContacts.objects.all().order_by('-id')
    if request.method == 'POST':
        user_name = request.POST.get('user_name', '')
        user_phone = request.POST.get('user_phone', '')
        user_text = request.POST.get('user_text', '')

        message = Message(user_name=user_name, user_phone=user_phone, user_text=user_text)
        message.save()

        comment_name_1 = request.POST.get('comment_name_1', '')
        comment_text_1 = request.POST.get('comment_text_1', '')

        if not comment_name_1 or not comment_text_1:
            return render(request, 'contacts.html', context={
                'email': 'wdqd@affew.com',
                'phone': '4567890',
                'server_time': datetime.now(),
                'comments_1': comments_contacts_objects
            })
        comment = CommentsContacts(comment_name_1=comment_name_1, comment_text_1=comment_text_1)
        comment.save()

    return render(request, 'contacts.html', context={
        'email': 'wdqd@affew.com',
        'phone': '4567890',
        'server_time': datetime.now(),
        'comments_1': comments_contacts_objects
    })



def publications(request):
    publications_objects = Publication.objects.all().order_by('-date')
    comments_publication_objects = CommentsPublication.objects.all().order_by('-id')
    if request.method == 'POST':
        comment_name = request.POST.get('comment_name', '')
        comment_text = request.POST.get('comment_text', '')

        if not comment_name or not comment_text:
            return render(request, 'publications.html', context={
                'error': 'Есть пустое поле',
                'publications': publications_objects,
                'comments': comments_publication_objects
            })
        comment = CommentsPublication(comment_name=comment_name, comment_text=comment_text)
        comment.save()
    return render(request, 'publications.html', context={
        'publications': publications_objects,
        'comments': comments_publication_objects
    })


def publication(request, number):
    try:
        publication = Publication.objects.get(id=number)
    except Publication.DoesNotExist:
        return redirect('/publications')
    return render(request, 'publication.html', context={
        'publication': publication
    })


def publish(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        title = request.POST.get('title', '')
        text = request.POST.get('text', '')

        if not password or not title or not text:
            return render(request, 'publish.html', {'error': 'Есть пустое поле'})
        if password != settings.PUBLISH_PASSWORD:
            return render(request, 'publish.html', {'error': 'Неверный пароль'})

        publication = Publication(text=text, title=title)
        publication.save()
        return redirect('/publications/' + str(publication.id))

    return render(request, 'publish.html')

def user_message(request):
    messages = Message.objects.all().order_by('-id')
    return render(request, 'user_message.html', context={
        'messages': messages
    })