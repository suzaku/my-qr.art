# My-QR.Art - A web app to design QR codes for your URL.
# Copyright (C) 2021 Marien Raat - mail@marienraat.nl

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('qr_template/', views.qr_template, name='qr_template'),
    path('copyright/', views.copyright, name='copyright'),
    path('create_qr/', views.create_qr, name='create_qr'),
    path('create_qr_arr/', views.create_qr_from_array, name='create_qr_from_array'),
]
