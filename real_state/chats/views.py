from uuid import UUID

from chats import openai_utils
from chats.models import Chat, Message
from django.shortcuts import redirect, render
from django.urls import reverse


def new_chat_request(request):
    if not request.user.is_authenticated:
        return redirect("users:home")
    if request.method == "POST":
        chat = Chat.objects.create(user=request.user)
        return redirect("chats", chat_id=chat.id)


def chat_page(request):
    if not request.user.is_authenticated:
        return redirect("users:home")
    try:
        chat_id = UUID(request.GET.get("chat_id"))
        chat = Chat.objects.filter(id=chat_id, user=request.user).first()
        if not chat:
            return redirect("users:home")

    except (ValueError, TypeError):
        return redirect("users:home")

    content_messages = list(
        Message.objects.filter(chat=chat).values_list("content", flat=True)
    )
    return render(
        request=request,
        template_name="chat.html",
        context={"chat": chat, "content_messages": content_messages},
    )


def chat_home_page(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request=request, template_name="chat_home.html", context={})


def new_message_request(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        import json

        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        content = body["content"]
        chat_id = body["chat_id"]
        chat = Chat.objects.filter(id=chat_id, user=request.user).first()

        openai_utils.new_message_in_chat(chat, content)
        return reverse("chat", kwargs={"chat_id": chat_id})
