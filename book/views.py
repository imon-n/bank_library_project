from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book_Model, PurchaseHistory
from transactions.models import Transaction
from transactions.constants import WITHDRAWAL

@login_required
def profile_history(request):
    purchases = PurchaseHistory.objects.filter(user=request.user)
    return render(request, 'profile_history.html', {'purchases': purchases})

@login_required
def buy_book(request, id):
    book = get_object_or_404(Book_Model, id=id)
    user_account = request.user.account

    if book.quantity > 0:
        amount = book.price
        
        if user_account.balance >= amount:
            user_account.balance -= amount
            user_account.save(update_fields=['balance'])
            
            book.reduce_quantity()
            
            PurchaseHistory.objects.create(
                user=request.user,
                book=book.name,
                category_name=book.category_name.category_name,
                price=book.price
            )
            
            Transaction.objects.create(
                account=user_account,
                amount=amount,
                balance_after_transaction=user_account.balance,
                transaction_type=WITHDRAWAL
            )
            if book.quantity == 0:
                book.delete()
            
            messages.success(request, f"You have successfully borrowed '{book.name}'.")
        else:
            messages.error(request, "Insufficient balance to borrow this book.")
    else:
        messages.error(request, "This book is out of stock.")

    return redirect('profile_history')





# from django.shortcuts import render,redirect, get_object_or_404
# from . import forms, models
# from .models import Book_Model, PurchaseHistory
# from django.urls import reverse_lazy
# from django.views.generic import CreateView, UpdateView,DeleteView,DetailView
# from django.utils.decorators import method_decorator
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from transactions.models import Transaction
# from transactions.constants import WITHDRAWAL

# @login_required
# def profile_history(request):
#     purchases = PurchaseHistory.objects.filter(user=request.user)
#     return render(request, 'profile_history.html', {'purchases': purchases})


# @login_required
# def buy_book(request, id):
#     # book = Book_Model.objects.get(id=id)
#     book = get_object_or_404(Book_Model, id=id)
#     user_account = request.user.account

#     if book.quantity > 0:
#         amount = book.price
        
#         if user_account.balance >= amount:
#             user_account.balance -= amount
#             user_account.save(update_fields=['balance'])

#         book.reduce_quantity()

#         PurchaseHistory.objects.create(
#             user=request.user,
#             book=book.name,
#             category_name=book.category_name.category_name,
#             price=book.price
#         )
#         Transaction.objects.create(
#             account=user_account,
#             amount=amount,
#             balance_after_transaction=user_account.balance,
#             transaction_type=WITHDRAWAL
#         )
#         if book.quantity == 0:
#             book.delete()
#             messages.success(request, f"You have successfully borrowed '{book.name}'.")
#         else:
#             messages.error(request, "Insufficient balance to borrow this book.")
#     else:
#         messages.error(request, "This book is out of stock.")

#     return redirect('profile_history')


