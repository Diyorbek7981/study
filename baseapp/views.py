from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from .form import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Function basic
def index(request):
    cats = Category.objects.all()[:3]
    rms = RommModel.objects.all()
    msg = Messages.objects.filter(res_active=True)[:4]
    if request.GET.get('search'):
        rms = RommModel.objects.filter(
            Q(title__icontains=request.GET.get('search')) |
            Q(content__icontains=request.GET.get('search')) |
            Q(category__cat_name__icontains=request.GET.get('search')))

    contex = {"rms": rms, 'cats': cats, 'msg': msg, 'cnt': rms.count}
    return render(request, 'theme/index.html', contex)


def room_detail(request, pk):
    rm = RommModel.objects.get(id=pk)
    messages = Messages.objects.filter(room_id=rm.pk).order_by('-created')
    participants = rm.participants.all()
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.user = request.user
            msg.room = rm
            msg.save()
            rm.participants.add(request.user)
            return redirect('room-detail', rm.pk)

    contex = {'rm': rm, 'messages': messages, 'ptns': participants, 'form': form}
    return render(request, 'theme/room.html', contex)


@login_required(login_url='login')
def create_room(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.user = request.user
            room.save()
            return redirect('home')

    contex = {'form': form}
    return render(request, "theme/create-room.html", contex)


@login_required(login_url='login')
def update_room(request, pk):
    room = RommModel.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    contex = {'form': form}
    return render(request, "theme/edit-room.html", contex)


@login_required(login_url='login')
def delete_room(request, pk):
    room = RommModel.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'theme/delete.html', {'obj': room.title})


def delete_msg(request, pk):
    message = Messages.objects.get(id=pk)

    if request.method == 'POST':
        message.delete()

        return redirect('room-detail', message.room.pk)

    return render(request, 'theme/delete.html', {'obj': message.message})


def categories(request):
    cats = Category.objects.all()[:6]
    rms = RommModel.objects.all()

    if s := request.GET.get('catsearch'):
        cats = Category.objects.filter(cat_name__icontains=s)

    contex = {'cats': cats, 'cnt': rms.count}
    return render(request, 'theme/topics.html', contex)


@login_required(login_url='login')
def category_room(request):
    form = CategoryForm

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    contex = {'form': form}
    return render(request, "theme/create_cat.html", contex)


@login_required(login_url='login')
def update_cat(request, pk):
    room = Category.objects.get(id=pk)
    form = CategoryForm(instance=room)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    contex = {'form': form}
    return render(request, "category_room.html", contex)


@login_required(login_url='login')
def delete_cat(request, pk):
    room = Category.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'delete_cat.html', {'obj': room})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    form = UserForm()
    contex = {'form': form}
    return render(request, 'theme/login.html', contex)


def logout_user(request):
    logout(request)
    return redirect('home')


def registration(request):
    form = CustumeUserForm()

    if request.method == 'POST':
        form = CustumeUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')

    contex = {'form': form}
    return render(request, 'theme/signup.html', contex)


def profile(request, pk):
    rms = RommModel.objects.filter(user_id=pk)
    cats = Category.objects.all()[:3]
    owner = User.objects.get(id=pk)
    msg = Messages.objects.filter(res_active=True)[:4]

    contex = {'owner': owner, 'cats': cats, 'msg': msg, 'cnt': rms.count, 'rms': rms}
    return render(request, 'theme/profile.html', contex)


def recent_active(request):
    rms = RommModel.objects.all()
    cats = Category.objects.all()
    user = User.objects.all()
    msg = Messages.objects.filter(res_active=True)[:4]

    contex = {'user': user, 'cats': cats, 'msg': msg, 'cnt': rms.count, 'rms': rms}
    return render(request, 'theme/activity.html', contex)


def settings(request, pk):
    user = User.objects.get(id=pk)
    form = UpdateUserForm(instance=user)

    if request.method == 'POST':
        form = CustumeUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

            return redirect('profile', user.pk)

    contex = {'user': user, 'form': form}
    return render(request, 'theme/settings.html', contex)


def active(request, pk):
    msg = Messages.objects.get(id=pk)

    msg.res_active = 'False'
    msg.save()
    return redirect('home')

    contex = {'msg': msg}
    return render(request, 'theme/index.html')
