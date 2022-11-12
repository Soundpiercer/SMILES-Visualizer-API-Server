import random
import string

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View

# from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm
# from .models import (
#     Item,
#     OrderItem,
#     Order,
#     Address,
#     Payment,
#     Coupon,
#     Refund,
#     UserProfile,
# )
