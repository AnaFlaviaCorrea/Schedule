from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacts
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def index(request):
    contacts = Contacts.objects.all().order_by("-id")
    return render(request, "pages/index.html", {"contacts": contacts})


def search(request):
    busca = request.GET.get("search")

    contacts = Contacts.objects.filter(name__icontains=busca)
    return render(request, "pages/index.html", {"contacts": contacts})


def details(request, id):
    # contacts = Contacts.objects.get(id=id)
    contacts = get_object_or_404(Contacts, id=id)
    return render(request, "pages/details.html", {"contacts": contacts})


def delete(request, id):
    contacts = Contacts.objects.get(id=id)
    refazer = contacts
    contacts.delete()
    return redirect("home")


def add(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        cpf = request.POST.get("CPF")
        email = request.POST.get("Email")
        phone = request.POST.get("Phone")
        height = request.POST.get("Height")
        description = request.POST.get("Description")
        date_birth = request.POST.get("Birthday")
        image = request.FILES.get("image")

        novo_contato = Contacts(
            name=name,
            cpf=cpf,
            email=email,
            phone=phone,
            height=height,
            description=description,
            date_birth=date_birth,
            image=image,
            active=True,
        )
        novo_contato.save()
        return redirect("home")
    else:
        return render(request, "pages/add.html")


def edit(request, id):
    contacts = Contacts.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("Name")
        cpf = request.POST.get("CPF")
        email = request.POST.get("Email")
        phone = request.POST.get("Phone")
        height = request.POST.get("Height")
        description = request.POST.get("Description")
        image = request.FILES.get("image")
        check = request.POST.get("check")
        if check == None:
            check = False
        else:
            check = True
        date_birth = request.POST.get("Birthday")
        print(check)

        contacts.name = name
        contacts.cpf = cpf
        contacts.email = email
        contacts.phone = phone
        contacts.height = height
        contacts.description = description
        contacts.date_birth = date_birth
        contacts.active = check
        if image != None:
            contacts.image = image
        contacts.save()

        return redirect("home")

    else:
        return render(request, "pages/edit.html", {"contacts": contacts})


def filter_contacts(request):
    filter_option = request.GET.get("filter", "")

    if filter_option == "ativo":
        contacts = Contacts.objects.filter(active=True)
    elif filter_option == "inativo":
        contacts = Contacts.objects.filter(active=False)
    else:
        contacts = Contacts.objects.all()

    return render(request, "pages/index.html", {"contacts": contacts})


def image_url(contacts):
    if contacts.image and hasattr(contacts.image, "url"):
        return contacts.image.url


# def edit_contact(request, id):
#     contacts =get_object_or_404(Contacts, id=id)

#     if request.method == "POST":
#         form = Contacts(request.POST, request.FILES, instance=contacts)

#         if form.is_valid():
#             contacts = form.save(commit=False)

#             if "image" in request.FILES:
#                 contacts.image = request.FILES["image"]

#             contacts.save()

#             return redirect("home")
#     else:
#         form = Contacts(instance=contacts)

#     return render(request, "pages/edit.html", {"form": form, "contacts": contacts})


# HttpResponse('Olá mundo')
