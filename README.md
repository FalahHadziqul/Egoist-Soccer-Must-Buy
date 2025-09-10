# Egoist Must Buy PBP

## 1. Step-by-Step Implementasi Checklist Tugas 2

### Inisiasi Project
Di awal permulaan project ini, saya menyiapkan folder project yang akan menyimpan keseluruhan project. Di folder tersebut, saya menyiapkan dan mengaktifkan Virtual Environment dengan command:
```bash
python -m venv env
env\Scripts\activate
```

### Dependencies dan Pembuatan Project Django
Masih di dalam Virtual Environment, saya membuat file `requirements.txt` yang berisi kebutuhan library, framework, atau package untuk project Django ini:

```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
python-dotenv
```

Instalasi dependencies dan pembuatan project Django:
```bash
pip install -r requirements.txt
django-admin startproject <nama_project> .
```

### Konfigurasi PWS
Mengkonfigurasi environment variables untuk development dan production di Pacil Web Service. Membuat dan mengatur file `.env` dan `.env.prod`, serta melakukan penyesuaian di `settings.py` (load environment variables, ALLOWED_HOST, PRODUCTION boolean, dan konfigurasi database).

### Pembuatan App `main`
Membuat aplikasi baru:
```bash
python manage.py startapp main
```
Mendaftarkan app `main` di `INSTALLED_APPS` pada `settings.py`. Menyiapkan main page aplikasi dengan membuat folder `templates` dan file `main.html`.

### Kreasi Model dan Migrasi
Contoh model di `models.py`:
```python
import uuid
from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('socks', 'Socks'),
        ('gloves', 'Gloves'),
        ('kPads', 'Knee Pads'),
    ]
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
```
Migrasi database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Integrasi MVT dan Routing
Menambahkan function baru di `views.py`:
```python
def show_main(request):
    context = {
        'shop_name': 'Egoist Must Buy',
        'npm': '2406437432',
        'name': 'Muhammad Hadziqul Falah Teguh',
        'class': 'PBP E'
    }
    return render(request, "main.html", context)
```
Contoh penggunaan context di `main.html`:
```html
<h5>Shop's Identity:</h5>
<p>{{ shop_name }}</p>
<h5>NPM:</h5>
<p>{{ npm }}</p>
<h5>Name:</h5>
<p>{{ name }}</p>
<h5>Class:</h5>
<p>{{ class }}</p>
```
Routing di `urls.py` pada app `main`:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
Integrasi di `urls.py` proyek utama:
```python
urlpatterns = [
    # ...
    path('', include('main.urls')),
    # ...
]
```

### Github
Inisialisasi repository dan push ke Github:
```bash
git init
git remote add origin <github_url>
git branch -M master
git add .
git commit -m "Initial commit"
git push -u origin master
```
Membuat `.gitignore` untuk file yang tidak di-include.

### PWS
Deploy project ke Pacil Web Service:
1. Konfigurasi `.env.prod` sesuai Environs project PWS.
2. Tambahkan URL project ke `ALLOWED_HOSTS` di `settings.py`.
3. Push ke PWS:
    ```bash
    git remote add pws <URL_PWS>
    git branch -M master
    git push pws master
    ```
4. Masukkan username dan password yang diberikan, lalu akses URL PWS untuk melihat hasil deploy.

---

## 2. Bagan Request Client ke Web Aplikasi Django

![Bagan Request Django](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1619466042369%2Fb3LAaF7TO.png)

**Penjelasan Alur:**
1. Client membuka request URL.
2. WSGI mengambil request dan mengubahnya ke Python object, lalu mengirim ke Django.
3. Django mengecek konfigurasi di `settings.py`.
4. Request diarahkan ke `urls.py` untuk mencocokkan URL.
5. Dari `urls.py`, fungsi di `views.py` dipanggil dan me-render HTML dari `templates`. Jika membutuhkan data dari database, `models.py` digunakan.
6. Response diformat sebagai string HTTP dan dikirim ke client melalui WSGI.

---

## 3. Peran `settings.py` dalam Proyek Django

`settings.py` adalah pusat konfigurasi proyek Django. File ini mengatur:
- **ALLOWED_HOSTS**: Daftar domain/IP yang dapat menjalankan proyek.
- **INSTALLED_APPS**: Aplikasi yang didaftarkan sebagai sub-project.
- **DATABASES**: Konfigurasi basis data (SQLite untuk development, PostgreSQL untuk production).
- Berbagai konfigurasi lain terkait keamanan, autentikasi, dan lainnya.

---

## 4. Cara Kerja Migrasi Database di Django

Database didefinisikan di `models.py` setiap app. Migrasi adalah proses memberitahu Django tentang perubahan model:
- Setiap perubahan di `models.py` perlu dijalankan:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
- Migrasi menetapkan perubahan model ke database.

---

## 5. Mengapa Django Cocok untuk Pemula?

Django adalah framework yang lengkap, menyediakan fitur Separation-of-Concerns, backend, dan SSR dengan integrasi Python yang mudah dipelajari.

---

## 6. Feedback untuk Asisten Dosen Tutorial 1

Untuk sementara tidak ada. Terima kasih tim dosen dan asisten dosen atas tutorial yang telah dirancang.