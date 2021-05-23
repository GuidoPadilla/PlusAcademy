from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from ajax_datatable.views import AjaxDatatableView

# Create your views here.
def control_view(request):
    return render(request, 'pagos/control.html')

def ingreso_view(request):
    return render(request, 'pagos/ingresar.html')

class PagosAjaxDatatableView(AjaxDatatableView):

    model = User
    title = 'Usuarios'
    initial_order = [["app_label", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'username', 'visible': True, },
        {'name': 'first_name', 'visible': True, },
        {'name': 'last_name', 'visible': True, },
    ]