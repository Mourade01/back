from django.shortcuts import render, redirect
from .forms import RegisterForm, NoteForm, KycForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import KycInfo, Note


@login_required(login_url="/login")
def home(request):
    notes = Note.objects.all()

    if request.method == "POST":
        note_id = request.POST.get("note-id")
        user_id = request.POST.get("user-id")

        if note_id:
            note = Note.objects.filter(id=note_id).first()
            if note and (note.author == request.user or request.user.has_perm("main.delete_note")):
                note.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'main/home.html', {"notes": notes})


@login_required(login_url="/login")
@permission_required("main.add_note", login_url="/login", raise_exception=True)
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect("/home")
    else:
        form = NoteForm()

    return render(request, 'main/create_note.html', {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

@login_required(login_url="/login")
@permission_required("main.add_kyc", login_url="/login", raise_exception=True)
def create_ekyc(request):
    if request.method == 'POST':
        form = KycForm(request.POST)
        if form.is_valid():
            KycInfo = form.save(commit=False)
            KycInfo.autheur = request.user
            KycInfo.save()
            return redirect("/profile")
    else:
        form = KycForm()

    return render(request, 'main/create_ekyc.html', {"form": form})

def profile(request):
    kycInfos = KycInfo.objects.all()

    if request.method == "POST":
        kycInfo_id = request.POST.get("kycInfo-id")
        user_id = request.POST.get("user-id")

        if kycInfo_id:
            kycInfo = Note.objects.filter(id=kycInfo_id).first()
            if kycInfo and (kycInfo.autheur == request.user or request.user.has_perm("main.delete_kycInfo")):
                kycInfo.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'main/profile.html', {"kycInfos": kycInfos})
