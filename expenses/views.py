from django.shortcuts import render
from rest_framework.response import Response
from django.db.models import Sum 
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import ExpenseSerializer, UserSerializer, CategorySerializer

from.models import Expense, User, Category

# Create your views here.
class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    @action(detail=False, methods=['get'])
    def list_by_date_range(self, request):
        user_id = request.query_params.get('user_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if user_id and start_date and end_date:
            try:
                expenses = self.get_queryset().filter(date__range= [start_date, end_date])
                serializer = self.get_serializer(expenses, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=500)
        else:
            return Response({'error': 'All parameters are required'}, status=400)
        
    @action(detail=False, methods=['get'])
    def category_summary(self, request):
        user_id = request.query_params.get('user_id')
        month = request.query_params.get('month') #format YYYY-MD

        if user_id and month:
            try:
                year, month = month.split('-')
                expenses = self.get_queryset().filter(user_id=user_id, date__year=year, date__month=month)
                summary = expenses.values('category').annotate(total=Sum('amount'))
                return Response(summary, status=200)

            except Exception as e:
                return Response({'error': str(e)}, status=500)
        else:
            return Response({'error': 'All parameters are required'}, status=400)





class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer