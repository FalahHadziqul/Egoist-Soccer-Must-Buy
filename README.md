# TUGAS 4
## Questions
### 1. Django AuthenticationForm
Django _AuthenticationForm_ adalah class yang disediakan oleh Django, guna untuk melakukan _autentikasi_ atau bisa dibilang tahap login user.

Kelebihan AuthhenticationForm Django :
- Cepat digunakan, tanpa memikirkan hal complex behind-the-scene.
- Memberikan penanganan autentikasi gagal yang jelas.

Kekurangan AuthhenticationForm Django :
- Secara default hanya berisi kolom-kolom standar seperti username, password. Jika ingin menambahhkan attribute maka perlu adanya kustomisasi.
- Tampilan standar; perlu adanya styling css untuk memberikan UI yang elegan.

### 2. Perbedaan antara Autentikasi dengan Otorisasi, dan Cara Django Mengimplementasikan Kedua Konsep Tersebut.
_Autentikasi_ adalah proses verifikasi user yang ingin mengakses server, sedangkan _otorisasi_ adalah proses pemberian hak akses yang diatur sesuai keinginan project builder. Django menerapkan kedua proses ini dengan implementasi sebagai berikut:

Autentikasi:
- Model User yang memiliki kolom-kolom username, password, email, first_name, last_name.
- Password Hashing untuk keamanan.
- Class AuthenticationForm.

Otorisasi:
- Decorator @login_required().
- Decorator @permission_required().

### 3. Kelebihan dan Kekurangan Session dan Cookies dalam Konteks Menyimpan State 
Kelebihan Cookies :
- Penyimpanan di sisi _client_, memungkinkan data yang tidak kredensial tetapi berguna untuk disimpan oleh user tanpa harus membebani storage pada server.
- Impelentasi mudah.

Kekurangan Cookies :
- Ukuran terbatas, yaitu sekitar 4KB.
- Terbawa pada setiap request yang diberikan ke server, sehingga munculnya _overhead_.

Kelebihan Sessions :
- Disimpan di server sehingga bisa dibilang relatif lebih aman dibanding disimpan di user browser, memungkinkan penyimpanan credential.
- Kapasitas penyimpanan lebih besar dibanding cookies, yaitu sekitar 5 MB.

Kekurangan Sessions :
- Perlu adanya pemahaman mengenai ilmu database agar sewaktu jumlah user meningkat proyek dapat beradaptasi terhadap skalabilitas.

### 4. Apakah Cookies Aman Secara Default? Jika tidak bagaiman Django meng-handle hal tersebut.
Tidak, penggunaan cookies secara default memiliki beberapa _vulnerabilities_ yang harus di-consider seperti penyerangan XSS untuk pencurian cookies, penyerangan CSRF melalui penggunaan cookies dari user yang sedang di sesi login.

Django memiliki beberapa fitur untuk meng-handle ini yaitu:
- csrf_token yang sudah dibahas sebelumnya
- Penggunaan HttpOnly pada Cookies Sessions; cookie session tidak boleh diakses melalui javascript, guna menghindari penyerangan XSS.

## Implementasi CheckList
### Pembuatan Form Registrasi
Dengan menggunakan UserCreationForm dari Django, kita akan membuat form registerasi guna mendaftarkan user yang ingin mengakses web kita.

```python
...
#Import
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
...

# Fungsi register
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
    ...
```

Maka setelah itu kita buat page untuk regsiter (register.html) : 
```html
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div>
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  <!-- Jika adanya message sukses pembuatan untuk case tugas ini-->
  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```

Setelah menambahkan url page pada urls.py, maka kita lanjut ke tahap selanjutnya. 
### Pembuatan Form Login dan opsi Logout
Setelah membuat form register, maka kita tentunya membuat form login dan opsi logout, mulai dengan membuat fungsi baru pemanggilan form page pada views.py.
```python
# Import
...
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
...

# Fungsi baru untuk login dan logout

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')
```
Disini kita menggunakan class dari Django yaitu AuthenticationForm untuk menghandle login oleh setiap user.

Maka kita juga buat page untuk login (login.html) : 
```html
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  <!-- Jika adanya message sukses pembuatan untuk case tugas ini-->
  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

Lalu pada main.html
```html
 <!-- Setelah hyperlink tag Add Product-->
...
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
...
```

urls.py:
```python
from main.views import logout_user, login_user
...

urlpatterns = [
   ...
   path('login/', login_user, name='login'),
   path('logout/', logout_user, name='logout'),
   ...
]
```
### Restriksi Akses Halaman-Halaman Tertentu ( Login Required )
Disini kita akan membatasi user yang bisa mengakses web, yaitu user yang sudah register dan login.

views.py : 
```python
from django.contrib.auth.decorators import login_required
...
```

lalu tambahkan @login_required(login_url='/login') pada fungsi show_main(), create_product(), show_product(), dan keempat fungsi data retrieval (xml dan json).

Maka setelah itu semua fungsi yang disebut diatas membutuhkan login untuk melakukan panggilan request.

### Implementasi Cookies
Disini kita akan mengimplementasikan cookies untuk men-set waktu login terakhir user.
Lakukanlah tambahan import dan modifikasi fungsi login_user, kemudian pada fungsi show_main, kita akan tambahkan context render, terakhir men-modif fungsi logout_user untuk mendelete cookie yang sebelumyna tersimpan sebagai 'last_login'.

views.py:
```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

...
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
...

def show_main(request):
    ...
    context = {
        'shop_name' : 'Egoist Must Buy',
        'npm': '2406437432',
        'name': request.user.username,
        'class': 'PBP E',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    ...
...

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
...
```

Pada main.html :
```html
<!-- Tambahkan setelah tombol logout-->
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

### Pengkaitan Setiap New Product dengan User Pembuat
Di tahap ini, kita akan atur agar setiap product yang dibuat membuat relasi dengan user pembuat.

models.py:
```python
from django.contrib.auth.models import User
...

class Product(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
     ...
...
```
Lakukan migrasi model.

Kemudian modif fungsi create_product(), dan show_main().

views.py:
```python
...
@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context) 
...

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all") 

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'shop_name' : 'Egoist Must Buy',
        'npm': '2406437432',
        'name': request.user.username,
        'class': 'PBP E',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html",context)
...

```
Pada main.html :
```html
<!-- Tambahkan kode ini setealah element h5 sesi terakhir login-->
<hr>
<a href="?filter=all">
    <button type="button">All Articles</button>
</a>
<a href="?filter=my">
    <button type="button">My Articles</button>
</a> 
...
```
Tampilkan nama author di product_detail.html:
```html
<!-- Tambahkan kode setelah product.deescription -->
{% if product.user %}
    <p>Author: {{ product.user.username }}</p>
{% else %}
    <p>Author: Anonymous</p>
{% endif %}

{% endblock content %}
```


## Feedback untuk Asisten Dosen Tutorial 3
CMIIW tapi bukankah create_news(), dan segala view XML JSON secara alami harus memiliki properti @login_required?
Karena di Tutorial 3 sepertinya belum ditambahkan.
Kira-kira itu saja Kak. Terimakasih 🙏

