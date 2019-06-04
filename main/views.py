from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'index.html')

def ckd(request):
    return render(request, 'ckd.html')

def register(request):
    form = request.POST
    errors = []

    if len(form['firstName']) < 3:
        errors.append('Name must be 3 at least characters long.')
    if len(form['lastName'])<3:
        errors.append("Alias must be at least 3 characters long.")
    if len(form['password'])<8 or len(form['confirm'])<8:
        errors.append("Password must be at least 8 characters long.")
    if form['password'] != form['confirm']:
        errors.append('Password and password confirmation must match.')
    
    if errors:
        for e in errors:
            messages.error(request, e)
            # .error is not the same as .errors, .error is a method
    else:
        hashedPW = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
        correctHashedPW = hashedPW.decode('utf-8')
        userNew = User.objects.create(firstName=form['firstName'], lastName=form['lastName'], email=form['email'], password=correctHashedPW)
        request.session['userId'] = userNew.id
    return redirect('/ckd')

def login(request):
    try:
        user = User.objects.get(email=request.POST['email'])
    except User.DoesNotExist:
        messages.error(request, 'This email has not been registered.')
        return redirect('/ckd')

    result = bcrypt.checkpw(request.POST['password'].encode(), user.password.encode())

    if result and (user.id == 1):
        request.session['userId'] = user.id
    elif user.id != 1:
        messages.error(request, 'You are not authorized to enter.')
    else:
        messages.error(request, 'Your Email or Password does not match.')
    return redirect('/dashboard')

def createNote(request):
    form = request.POST
    newNote = Note.objects.create(name = form['name'], email=form['email'], message=form['message'])
    # sent = "Your message has been sent."
    return redirect('/')

def dashboard(request):

    if not 'userId' in request.session:
        messages.error(request, 'You need to login.')
        return redirect('/ckd')

    notes = Note.objects.all()
    user = User.objects.get(id=request.session['userId'])
    # myplans = Trip.objects.filter(user=user)
    # presentuserid = request.session['userId']
    # alltrips = Trip.objects.all()
    # alltripsexclude = Trip.objects.exclude(user_id=request.session['userId']).exclude(joiners=request.session['userId'])

    # mytripsnoti = Trip.objects.filter(joiners=user)
    # myusertrips = Trip.objects.filter(id=request.session['userId'])
    
    context = {
        'notes': notes,
        'user': user,
        'array5': [1,2,3,4,5],
        # 'myplans': myplans,
        # 'myusertrips' : myusertrips,
        # 'presentuserid': presentuserid,
        # 'alltrips': alltrips,
        # 'alltripsexclude':alltripsexclude,
        # 'mytripsnoti': mytripsnoti
    }

    return render(request, 'dashboard.html', context)



def logout(request):

    request.session.clear()
    return redirect('/ckd')