from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import User, WaterIntake
from .serializers import UserSerializer, WaterIntakeSerializer
from datetime import date

# API viewsets
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WaterIntakeViewSet(viewsets.ModelViewSet):
    queryset = WaterIntake.objects.all()
    serializer_class = WaterIntakeSerializer

# Views para o frontend
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        weight = request.POST['weight']
        user = User(name=name, weight=weight)
        user.save()
    return render(request, 'register.html')

def daily(request):
    users = User.objects.all()
    current_date = date.today()
    if request.method == 'POST':
        amount = request.POST['amount']
        user_id = request.POST['user']
        user = User.objects.get(id=user_id)
        WaterIntake.objects.create(user=user, amount=amount)
        return redirect('daily')

    daily_intakes = WaterIntake.objects.filter(date=current_date)
    data = []
    for user in users:
        total_intake = sum(intake.amount for intake in daily_intakes if intake.user == user)
        goal = user.weight * 35
        remaining = goal - total_intake
        reached_goal = "Sim" if total_intake >= goal else "Não"
        percentage = (total_intake / goal) * 100 if goal > 0 else 0
        data.append({
            'user': user,
            'total_intake': total_intake,
            'goal': goal,
            'remaining': remaining,
            'percentage': percentage,
            'reached_goal': reached_goal,
        })

    return render(request, 'daily.html', {'data': data, 'current_date': current_date})

def history(request):
    users = User.objects.all()
    return render(request, 'history.html', {'users': users})
