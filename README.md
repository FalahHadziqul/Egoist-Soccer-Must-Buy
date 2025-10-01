# TUGAS 5

## Questions

### 1. Urutan prioritas pengambilan CSS selector

Asumsikan kita ingin men-style element HTML :

```html
<p id="intro" class="text">Hello CSS!</p>
```

Jika terdapat beberapa CSS Selector untuk element HTML tersebut maka berikut adalah urutan prioritas dari TERENDAH hingga TERTINGGI untuk nantinya yang akan benar-benar akan diterapkan pada hasil akhir styling element HTML tersebut.

- Selector universal

```css
* {
  color: blue;
}
```

- Selector class

```css
.text {
  color: blue;
}
```

- Selector ID

```css
#intro {
  color: red;
}
```

- Inline style

```html
<!-- in the HTML File. -->
<p id="intro" class="text" style="color: red;">Hello CSS!</p>
```

- !important rule

```css
.text {
  color: blue !important;
}
```

- !important rule (inline style)

```html
<p id="intro" class="text" style="color: red !important;">Hello CSS!</p>
```

### 2. Responsive Design

Responsive Design menjadi konsep yang penting dalam pengembangan aplikasi web, karena beberapa hal seperti

- Mampunya app untuk ditampilkan di semua ukuran device.
- Optimisasi SEO; Google memberi peringkat lebih tinggi pada situs yang _mobile-friendly_.
- Efisiensi Pengembangan; satu kode basis untuk semua perangkat → tidak perlu membuat versi mobile dan desktop terpisah.
- Meningkatkan Konversi; membuat semua pengguna dapat dengan mudah melakukan transaksi atau aktivitas yang dilakukan pada web app kita.

Contoh aplikasi yang sudah menerapkan responsive design:

- Youtube : UI/UX dan penggunaan yang straight-forward di semua device. Adanya hamburger button untuk endpoint lain dan lain sebagainya.
- Tokopedia : Merupakan salah satu E-Commerce dengan UX dan responsive design terbaik menurut banyak pendapat orang. Sudah pasti bahwa baik di web dan mobile App Tokopedia sudah mengintegrasikan pengalaman pengguna yang baik seperti jumlah kolom grid berbeda di web vd mobile App dan kelebihan lain sebagainya.

Contoh aplikasi yang BELUM sudah menerapkan responsive design:

Sebenarnya pertanyaan ini merujuk ke pendapat subjektif karena 99% web app terkenal sudah mengintegrasikan responsive design. Tapi bila dipersilahkan kepada saya untuk memberikan contoh maka menurut saya web-web app standard akademik yang targetnya untuk mahasiswa setempat. Contoh di lingkungan terdekat kita adalah SCELE, SIAK, dan EMAS. Contoh yang saya berikan misalnya SCELE untuk Upcoming Events, Recent Activity yang harus kita akses dengan scroll sampai ujung bawah di mobile view , sedangkan di ukuran desktop dapat kita lihat di sidebar kanan kita dan tidak berubah seiring kita scroll bagian main page.

### 3. Margin, border, padding

Margin, border, dan padding merupakan bagian dari konsep besar yang disebut CSS Box Model.
Ketiga ini sama-sama akan memberikan **jarak** pada elemen html kita. Berikut adalah perbedaannya:

- Margin : Memisahkan elemen dari elemen lain
- Border : Menentukan kebetalan dari batas elemen.
- Padding : Memberi ruang di dalam kotak elemen.

Contoh Implementasi Ketiga-tiganya:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Box Model Example</title>
    <style>
      .box {
        background-color: lightblue;
        color: #333;

        /* Padding: jarak di dalam box */
        padding: 20px;

        /* Border: garis tepi box */
        border: 3px solid blue;

        /* Margin: jarak di luar box */
        margin: 30px;
      }
    </style>
  </head>
  <body>
    <div class="box">Ini adalah konten di dalam box</div>
    <div class="box">Box kedua</div>
  </body>
</html>
```

### 4. Flex box dan grid layout

Flexbox adalah sistem layout yang digunakan untuk melakukan penyusunan/penumpukan elemen secara horizontal atau vertikal dengan fleksibel. Sistem layout flexbox akan banyak memakai istilah parent dan child container. Flexbox banyak memiliki cara penyusunan, contohnya kita ingin melakukan penumpukan elemen pada baris (flex-row) atau penumpukan elemen pada col (flex-col).Lalu misal pada flex-row kita ingin meng-adjust elemen-elemen yang dibuat agar berada di tengah (align-center).

Contoh Kode :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Flexbox Center Example</title>
    <style>
      .container {
        /* Aktifkan flexbox */
        display: flex;
        /* Arah utama: horizontal */
        flex-direction: row;
        /* Pusatkan secara horizontal */
        justify-content: center;
        /* Pusatkan secara vertikal */
        align-items: center;
        /* Supaya terlihat tengah vertikalnya */
        height: 200px;
        background-color: #f0f0f0;
        /* Jarak antar elemen */
        gap: 10px;
      }

      .item {
        background-color: lightblue;
        padding: 20px 40px;
        border-radius: 8px;
        font-weight: bold;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="item">Box 1</div>
      <div class="item">Box 2</div>
      <div class="item">Box 3</div>
    </div>
  </body>
</html>
```

Grid-layout adalah sistem layout yang bekerja dalam penyusunan elemen dalam dua dimensi. Disini kita bisa mengatur banyaknya elemen pada setiap baris atau kolom. Anggaplah kita ingin membuat jumlah elemen setiap kolom sebanyak lima untuk desktop view dan sebanyak dua untuk mobile view:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Responsive Grid Example</title>
    <style>
      .container {
        display: grid;
        gap: 10px;
        /* Default: 2 kolom (mobile) */
        grid-template-columns: repeat(2, 1fr);
        padding: 10px;
      }

      .item {
        background-color: lightblue;
        padding: 20px;
        text-align: center;
        font-weight: bold;
        border-radius: 8px;
      }

      /* 🔹 Untuk layar besar (desktop) */
      @media (min-width: 768px) {
        .container {
          /* 5 kolom di desktop */
          grid-template-columns: repeat(5, 1fr);
        }
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="item">1</div>
      <div class="item">2</div>
      <div class="item">3</div>
      <div class="item">4</div>
      <div class="item">5</div>
      <div class="item">6</div>
      <div class="item">7</div>
      <div class="item">8</div>
      <div class="item">9</div>
      <div class="item">10</div>
    </div>
  </body>
</html>
```

## Implementasi CheckList

### Membuat Fitur Edit dan Delete Product

Disini cukup straight forward seperti penambahan fitur-fitur sebelumnya, yaitu dengan membuat dua fungsi baru di view.py (main) yaitu edit_product dan delete_product.

```python
...
@login_required(login_url='/login')
def edit_product(request, id):
    # Serupa dengan create_product, tetapi karena product sudah ada maka kita retrieve dulu sebelum melakukan POST request.
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
...
```

Setelah itu kita lakukan if block statement pada main.html (jika sudah authenticate dan product dibuat oleh user yang sama) maka akan muncul tombol edit dan hapus.

Setelah itu tambahkan function pada urls.py (main) dan jangan lupa untuk mensertakan uuid pada path urlspattern.

### Mengimpor Tailwind

Cukup tambahkan

```html
<script src="https://cdn.tailwindcss.com"></script>
```

Di dalam head element base.html
Melalui line ini kita menambahkan tailwind di proyek kita menggunakan Content Delivery Network.

### Konfigurasi Static Files

Di dalam settings.py

```python
...
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
    ...
]
...

STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static' # merujuk ke /static root project pada mode development
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
...
```

### Navbar & Styling

Buatlah file navbar.html di dalam templates root dan kita include di main.html

```html
{% extends 'base.html' %} {% block content %} {% include 'navbar.html' %} ... {%
endblock content%}
```

Lalu berikut adalah styling yang dilakukan di navbar.html

```html
<nav
  class="fixed top-0 left-0 w-full bg-white border-b border-gray-200 shadow-sm z-50"
>
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <div class="flex items-center">
        <h1 class="text-xl font-semibold text-gray-900">
          <span class="text-blue-800 font-bold">Egoist </span> Must Buy
        </h1>
      </div>

      <!-- Tampilan Navigasi untuk Desktop -->
      <div class="hidden md:flex items-center space-x-8">
        <a
          href="/"
          class="text-gray-600 hover:text-gray-900 font-medium transition-colors"
        >
          Home
        </a>
        <a
          href="{% url 'main:create_product' %}"
          class="text-gray-600 hover:text-gray-900 font-medium transition-colors"
        >
          Create Product
        </a>
      </div>

      <!-- Tampilan User Section untuk Desktop -->
      <div class="hidden md:flex items-center space-x-6">
        {% if user.is_authenticated %}
        <div class="text-right">
          <div class="text-sm font-medium text-gray-900">
            {{ name|default:user.username }}
          </div>
          <div class="text-xs text-gray-500">
            {{ npm|default:"Student" }} - {{ class|default:"Class" }}
          </div>
        </div>
        <a
          href="{% url 'main:logout' %}"
          class="text-red-600 hover:text-red-700 font-medium transition-colors"
        >
          Logout
        </a>
        {% else %}
        <a
          href="{% url 'main:login' %}"
          class="text-gray-600 hover:text-gray-900 font-medium transition-colors"
        >
          Login
        </a>
        <a
          href="{% url 'main:register' %}"
          class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded font-medium transition-colors"
        >
          Register
        </a>
        {% endif %}
      </div>

      <!-- Mobile Menu Button -->
      <div class="md:hidden flex items-center">
        <button
          class="mobile-menu-button p-2 text-gray-600 hover:text-gray-900 transition-colors"
        >
          <span class="sr-only">Open menu</span>
          <div class="w-6 h-6 flex flex-col justify-center items-center">
            <span
              class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm"
            ></span>
            <span
              class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm my-0.5"
            ></span>
            <span
              class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm"
            ></span>
          </div>
        </button>
      </div>
    </div>
  </div>
  <!-- Mobile Menu -->
  <div class="mobile-menu hidden md:hidden bg-white border-t border-gray-200">
    <div class="px-6 py-4 space-y-4">
      <!-- Mobile Navigation Links -->
      <div class="space-y-1">
        <a
          href="/"
          class="block text-gray-600 hover:text-gray-900 font-medium py-3 transition-colors"
        >
          Home
        </a>
        <a
          href="{% url 'main:create_product' %}"
          class="block text-gray-600 hover:text-gray-900 font-medium py-3 transition-colors"
        >
          Create Product
        </a>
      </div>

      <!-- Mobile User Section -->
      <div class="border-t border-gray-200 pt-4">
        {% if user.is_authenticated %}
        <div class="mb-4">
          <div class="font-medium text-gray-900">
            {{ name|default:user.username }}
          </div>
          <div class="text-sm text-gray-500">
            {{ npm|default:"Student" }} - {{ class|default:"Class" }}
          </div>
        </div>
        <a
          href="{% url 'main:logout' %}"
          class="block text-red-600 hover:text-red-700 font-medium py-3 transition-colors"
        >
          Logout
        </a>
        {% else %}
        <div class="space-y-3">
          <a
            href="{% url 'main:login' %}"
            class="block text-gray-600 hover:text-gray-900 font-medium py-3 transition-colors"
          >
            Login
          </a>
          <a
            href="{% url 'main:register' %}"
            class="block bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-4 rounded text-center transition-colors"
          >
            Register
          </a>
        </div>
        {% endif %}
      </div>
    </div>
  </div>
  <script>
    const btn = document.querySelector("button.mobile-menu-button");
    const menu = document.querySelector(".mobile-menu");

    btn.addEventListener("click", () => {
      menu.classList.toggle("hidden");
    });
  </script>
</nav>
```

Disini kita memanfaatkan styling 'hidden' untuk adaptasi perpindahan mobile dan desktop.

### Styling Halaman Login

Berikut styling yang kita lakukan di login.html

```html
{% extends 'base.html' %} {% block meta %}
<title>Login - Egoist Must Buy</title>
{% endblock meta %} {% block content %}
<div
  class="bg-gray-50 w-full min-h-screen flex items-center justify-center p-8"
>
  <div class="max-w-md w-full">
    <div
      class="bg-white rounded-lg border border-gray-200 p-6 sm:p-8 form-style"
    >
      <div class="text-center mb-8">
        <h1 class="text-2xl font-bold text-gray-900 mb-2">Sign In</h1>
        <p class="text-gray-600">Welcome back to Egoist Must Buy</p>
      </div>

      <!-- Form Errors Display -->
      {% if form.non_field_errors %}
      <div class="mb-6">
        {% for error in form.non_field_errors %}
        <div
          class="px-4 py-3 rounded-md text-sm border bg-red-50 border-red-200 text-red-700"
        >
          {{ error }}
        </div>
        {% endfor %}
      </div>
      {% endif %} {% if form.errors %}
      <div class="mb-6">
        {% for field, errors in form.errors.items %} {% if field != '__all__' %}
        {% for error in errors %}
        <div
          class="px-4 py-3 rounded-md text-sm border bg-red-50 border-red-200 text-red-700 mb-2"
        >
          <strong>{{ field|title }}:</strong> {{ error }}
        </div>
        {% endfor %} {% endif %} {% endfor %}
      </div>
      {% endif %}

      <form method="POST" action="" class="space-y-6">
        {% csrf_token %}

        <div>
          <label
            for="username"
            class="block text-sm font-medium text-gray-700 mb-2"
            >Username</label
          >
          <input
            id="username"
            name="username"
            type="text"
            required
            class="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 transition-colors"
            placeholder="Enter your username"
          />
        </div>

        <div>
          <label
            for="password"
            class="block text-sm font-medium text-gray-700 mb-2"
            >Password</label
          >
          <input
            id="password"
            name="password"
            type="password"
            required
            class="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 transition-colors"
            placeholder="Enter your password"
          />
        </div>

        <button
          type="submit"
          class="w-full bg-blue-800 text-white font-medium py-3 px-4 rounded-md hover:bg-blue-700 transition-colors"
        >
          Sign In
        </button>
      </form>

      <!-- Messages Display -->
      {% if messages %}
      <div class="mt-6">
        {% for message in messages %}
        <div
          class="
                px-4 py-3 rounded-md text-sm border
                {% if message.tags == 'success' %}
                  bg-blue-50 border-blue-200 text-blue-700
                {% elif message.tags == 'error' %}
                  bg-red-50 border-red-200 text-red-700
                {% else %}
                  bg-gray-50 border-gray-200 text-gray-700
                {% endif %}
              "
        >
          {{ message }}
        </div>
        {% endfor %}
      </div>
      {% endif %}

      <div class="mt-6 text-center pt-6 border-t border-gray-200">
        <p class="text-gray-500 text-sm">
          Don't have an account?
          <a
            href="{% url 'main:register' %}"
            class="text-blue-600 hover:text-blue-700 font-medium"
          >
            Register Now
          </a>
        </p>
      </div>
    </div>
  </div>
</div>
{% endblock content %}
```

### Styling Halaman Register
Berikut styling yang kita lakukan di register.html
```html
{% extends 'base.html' %}

{% block meta %}
<title>Register - Egoist Must Buy</title>
{% endblock meta %}

{% block content %}
<div class="form-style">
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-8">
    <div class="max-w-md w-full relative z-10">
      <div class="bg-white border border-gray-200 rounded-lg p-8 shadow-sm">
      <div class="text-center mb-8">
        <h2 class="text-2xl font-semibold text-gray-900 mb-2">Join Us</h2>
        <p class="text-gray-500">Create your account</p>
      </div>

      <!-- Form Errors Display -->
      {% if form.non_field_errors %}
        <div class="mb-6">
          {% for error in form.non_field_errors %}
            <div class="px-4 py-3 rounded text-sm border bg-red-50 border-red-200 text-red-700">
              {{ error }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

      {% if form.errors %}
        <div class="mb-6">
          {% for field, errors in form.errors.items %}
            {% if field != '__all__' %}
              {% for error in errors %}
                <div class="px-4 py-3 rounded text-sm border bg-red-50 border-red-200 text-red-700 mb-2">
                  <strong>{{ field|title }}:</strong> {{ error }}
                </div>
              {% endfor %}
            {% endif %}
          {% endfor %}
        </div>
      {% endif %}

      <form method="POST" action="" class="space-y-5">
        {% csrf_token %}
        
        <div>
          <label for="username" class="block text-sm font-medium text-gray-700 mb-2">Username</label>
          <input 
            id="username" 
            name="username" 
            type="text" 
            required 
            class="w-full px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-blue-500 transition duration-200" 
            placeholder="Choose a username">
        </div>

        <div>
          <label for="password1" class="block text-sm font-medium text-gray-700 mb-2">Password</label>
          <input 
            id="password1" 
            name="password1" 
            type="password" 
            required 
            class="w-full px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-blue-500 transition duration-200" 
            placeholder="Create a password">
        </div>

        <div>
          <label for="password2" class="block text-sm font-medium text-gray-700 mb-2">Confirm Password</label>
          <input 
            id="password2" 
            name="password2" 
            type="password" 
            required 
            class="w-full px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-blue-500 transition duration-200" 
            placeholder="Confirm your password">
        </div>

        <button 
          type="submit" 
          class="w-full bg-blue-600 text-white font-medium py-3 px-4 rounded hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition duration-200">
          Create Account
        </button>
      </form>

      <!-- Messages Display -->
      {% if messages %}
        <div class="mt-6">
          {% for message in messages %}
            <div 
              class="
                px-4 py-3 rounded text-sm border
                {% if message.tags == 'success' %}
                  bg-blue-50 border-blue-200 text-blue-700
                {% elif message.tags == 'error' %}
                  bg-red-50 border-red-200 text-red-700
                {% else %}
                  bg-gray-50 border-gray-200 text-gray-700
                {% endif %}
              ">
              {{ message }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

      <div class="mt-6 text-center">
        <p class="text-gray-500 text-sm">
          Already have an account? 
          <a href="{% url 'main:login' %}" class="text-blue-600 hover:text-blue-700 font-medium">
            Sign In
          </a>
        </p>
      </div>
      </div>
    </div>
  </div>
</div>
{% endblock content %}
```
Disini meng-utilise wanra biru untuk tombol dan warna saat focus berada di input.

### Styling Halaman Home
Karena nanti di halaman utama kita akan menampilkan grid card berisi products.
Maka pertama kita buat cards_product.html, guna untuk menjadi konfigurasi design setiap product yang akan dibuat.

```html
{% load static %}
<article
  class="bg-white rounded-xl shadow-sm hover:shadow-xl transition-all duration-300 overflow-hidden border border-blue-100"
>
  <!-- Thumbnail -->
  <div
    class="aspect-[16/9] relative overflow-hidden bg-gradient-to-br from-blue-50 to-blue-100"
  >
    {% if product.thumbnail %}
    <img
      src="{{ product.thumbnail }}"
      alt="{{ product.title }}"
      class="w-full h-full object-cover hover:scale-105 transition-transform duration-500"
    />
    {% else %}
    <div
      class="w-full h-full bg-gradient-to-br from-blue-100 to-blue-200 flex items-center justify-center"
    >
      <svg
        class="w-20 h-20 text-blue-300"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="1.5"
          d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
        />
      </svg>
    </div>
    {% endif %}
    <!-- Category Badge -->
    <div class="absolute top-3 left-3">
      <span
        class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-blue-600 text-white shadow-lg backdrop-blur-sm"
      >
        {{ product.get_category_display }}
      </span>
    </div>
    <!-- Status Badges -->
    <div class="absolute top-3 right-3 flex gap-2">
      {% if product.is_featured %}
      <span
        class="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-amber-400 text-amber-900 shadow-md"
      >
        ⭐ Featured
      </span>
      {% endif %} {% if product.is_product_hot %}
      <span
        class="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-rose-500 text-white shadow-md"
      >
        🔥 Hot
      </span>
      {% endif %}
    </div>
  </div>
  <!-- Content -->
  <div class="p-6">
    <div class="flex items-center text-xs text-blue-600 font-medium mb-3">
      <time datetime="{{ product.created_at|date:'c' }}">
        {{ product.created_at|date:"M j, Y" }}
      </time>
      <span class="mx-2 text-blue-300">•</span>
      <span class="flex items-center gap-1">
        <svg
          class="w-3.5 h-3.5"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
          />
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
          />
        </svg>
        {{ product.product_views }}
      </span>
    </div>
    <h3 class="text-xl font-bold text-gray-900 mb-3 line-clamp-2 leading-snug">
      <a
        href="{% url 'main:show_product' product.id %}"
        class="hover:text-blue-600 transition-colors duration-200"
      >
        {{ product.title }}
      </a>
    </h3>
    <p class="text-gray-600 text-sm leading-relaxed line-clamp-3 mb-5">
      {{ product.content|truncatewords:20 }}
    </p>
    <!-- Action Buttons -->
    {% if user.is_authenticated and product.user == user %}
    <div class="flex items-center justify-between pt-4 border-t border-blue-50">
      <a
        href="{% url 'main:show_product' product.id %}"
        class="inline-flex items-center text-blue-600 hover:text-blue-700 font-semibold text-sm transition-colors duration-200 group"
      >
        Read more
        <svg
          class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 5l7 7-7 7"
          />
        </svg>
      </a>
      <div class="flex gap-3">
        <a
          href="{% url 'main:edit_product' product.id %}"
          class="text-blue-600 hover:text-blue-700 hover:underline text-sm font-medium transition-colors duration-200"
        >
          Edit
        </a>
        <a
          href="{% url 'main:delete_product' product.id %}"
          class="text-rose-600 hover:text-rose-700 hover:underline text-sm font-medium transition-colors duration-200"
        >
          Delete
        </a>
      </div>
    </div>
    {% else %}
    <div class="pt-4 border-t border-blue-50">
      <a
        href="{% url 'main:show_product' product.id %}"
        class="inline-flex items-center text-blue-600 hover:text-blue-700 font-semibold text-sm transition-colors duration-200 group"
      >
        Read more
        <svg
          class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 5l7 7-7 7"
          />
        </svg>
      </a>
    </div>
    {% endif %}
  </div>
</article>
```
Lalu pada main.html
```html
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>Football product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
<div class="bg-gray-50 w-full pt-16 min-h-screen">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">

    <!-- Header Section -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-900 mb-2">Latest Football product</h1>
      <p class="text-gray-600">Stay updated with the latest football products</p>
    </div>

    <!-- Filter Section -->
    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-8 bg-white rounded-lg border border-gray-200 p-4">
      <div class="flex space-x-3 mb-4 sm:mb-0">
        <a href="?" class="{% if request.GET.filter == 'all' or not request.GET.filter  %} bg-blue-600 text-white{% else %}bg-white text-gray-700 border border-gray-300{% endif %} px-4 py-2 rounded-md font-medium transition-colors hover:bg-blue-600 hover:text-white">
          All product
        </a>
        <a href="?filter=my" class="{% if request.GET.filter == 'my' %} bg-blue-600 text-white{% else %}bg-white text-gray-700 border border-gray-300{% endif %} px-4 py-2 rounded-md font-medium transition-colors hover:bg-blue-600 hover:text-white">
          My product
        </a>
      </div>
      {% if user.is_authenticated %}
        <div class="text-sm text-gray-500">
          Last login: {{ last_login }}
        </div>
      {% endif %}
    </div>

    <!-- product Grid -->
    {% if not product_list %}
      <div class="bg-white rounded-lg border border-gray-200 p-12 text-center">
        <div class="w-32 h-32 mx-auto mb-4">
          <img src="{% static 'images/no-product.png' %}" alt="No product available" class="w-full h-full object-contain">
        </div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">No product found</h3>
        <p class="text-gray-500 mb-6">Be the first to share football product with the community.</p>
        <a href="{% url 'main:create_product' %}" class="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors">
          Create product
        </a>
      </div>
    {% else %}
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {% for product in product_list %}
          {% include 'card_product.html' with product=product %}
        {% endfor %}
      </div>
    {% endif %}
  </div>
</div>
{% endblock content %}
```
### Styling Halaman Product Detail
Untuk tampilan saat mengecek detail dari product pada product_detail.html:
```html
{% extends 'base.html' %} {% load static %} {% block meta %}
<title>{{ product.title }} - Football product</title>
{% endblock meta %} {% block content %}
<div class="bg-gray-50 w-full min-h-screen">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Back Navigation -->
    <div class="mb-6">
      <a
        href="{% url 'main:show_main' %}"
        class="text-gray-600 hover:text-gray-900 font-medium transition-colors"
      >
        ← Back to product
      </a>
    </div>

    <!-- Article -->
    <article class="bg-white rounded-lg border border-gray-200 overflow-hidden">
      <!-- Header -->
      <div class="p-6 sm:p-8">
        <div class="flex flex-wrap items-center gap-2 mb-4">
          <span
            class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-blue-600 text-white"
          >
            {{ product.get_category_display }}
          </span>
          {% if product.is_featured %}
          <span
            class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-yellow-100 text-yellow-800"
          >
            Featured
          </span>
          {% endif %} {% if product.is_product_hot %}
          <span
            class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-red-100 text-red-800"
          >
            Hot
          </span>
          {% endif %}
        </div>

        <h1
          class="text-3xl sm:text-4xl font-bold text-gray-900 leading-tight mb-4"
        >
          {{ product.title }}
        </h1>

        <div class="flex flex-wrap items-center text-sm text-gray-500 gap-4">
          <time datetime="{{ product.created_at|date:'c' }}">
            {{ product.created_at|date:"M j, Y g:i A" }}
          </time>
          <span>{{ product.product_views }} views</span>
        </div>
      </div>

      <!-- Featured Image -->
      {% if product.thumbnail %}
      <div class="px-6 sm:px-8">
        <img
          src="{{ product.thumbnail }}"
          alt="{{ product.title }}"
          class="w-full h-64 sm:h-80 lg:h-96 object-cover rounded-lg"
        />
      </div>
      {% endif %}

      <!-- Content -->
      <div class="p-6 sm:p-8">
        <div class="prose prose-lg max-w-none">
          <div
            class="text-gray-700 leading-relaxed whitespace-pre-line text-base sm:text-lg"
          >
            {{ product.content }}
          </div>
        </div>
      </div>

      <!-- Author Info -->
      <div class="border-t border-gray-200 p-6 sm:p-8 bg-gray-50">
        <div class="flex items-center justify-between">
          <div>
            <div class="font-medium text-gray-900">
              {% if product.user %}
              <p>Author: {{ product.user.username }}</p>
              {% else %}
              <p>Author: Anonymous</p>
              {% endif %}
            </div>
            <p class="text-sm text-gray-500">Author</p>
          </div>
        </div>
      </div>
    </article>
  </div>
</div>
{% endblock content %}

```
### Styling Halaman Create Product
Pada create_product.html:
```html
{% extends 'base.html' %}
{% block meta %}
<title>Create product - Football product</title>
{% endblock meta %}

{% block content %}
<div class="bg-gray-50 w-full min-h-screen">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    
    <!-- Back Navigation -->
    <div class="mb-6">
      <a href="{% url 'main:show_main' %}" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">
        ← Back to product
      </a>
    </div>
    
    <!-- Form -->
    <div class="bg-white rounded-lg border border-gray-200 p-6 sm:p-8 form-style">
      <div class="mb-8">
        <h1 class="text-2xl font-bold text-gray-900 mb-2">Create New product</h1>
        <p class="text-gray-600">Share your football product and stories with the community</p>
      </div>
      
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div>
            <label for="{{ field.id_for_label }}" class="block text-sm font-medium text-gray-700 mb-2">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        
        <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-gray-200">
          <a href="{% url 'main:show_main' %}" class="order-2 sm:order-1 px-6 py-3 border border-gray-300 text-gray-700 rounded-md font-medium hover:bg-gray-50 transition-colors text-center">
            Cancel
          </a>
          <button type="submit" class="order-1 sm:order-2 flex-1 bg-blue-600 text-white px-6 py-3 rounded-md font-medium hover:bg-blue-700 transition-colors">
            Publish product
          </button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endblock %}
```

### Syling Halaman Edit Product
Terakhir untuk halaman edit product di edit_product.html :
```html
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>Edit product - Football product</title>
{% endblock meta %}

{% block content %}
<div class="bg-gray-50 w-full min-h-screen">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    
    <!-- Back Navigation -->
    <div class="mb-6">
      <a href="{% url 'main:show_main' %}" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">
        ← Back to product
      </a>
    </div>
    
    <!-- Form -->
    <div class="bg-white rounded-lg border border-gray-200 p-6 sm:p-8 form-style">
      <div class="mb-8">
        <h1 class="text-2xl font-bold text-gray-900 mb-2">Edit product</h1>
        <p class="text-gray-600">Update your football product and stories</p>
      </div>
      
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div>
            <label for="{{ field.id_for_label }}" class="block text-sm font-medium text-gray-700 mb-2">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        
        <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-gray-200">
          <a href="{% url 'main:show_main' %}" class="order-2 sm:order-1 px-6 py-3 border border-gray-300 text-gray-700 rounded-md font-medium hover:bg-gray-50 transition-colors text-center">
            Cancel
          </a>
          <button type="submit" class="order-1 sm:order-2 flex-1 bg-blue-600 text-white px-6 py-3 rounded-md font-medium hover:bg-blue-700 transition-colors">
            Update product
          </button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endblock %}
```

## Feedback untuk Asisten Dosen Tutorial 3
Mengapa menggunakan CDN Tailwind dibanding meng-install?
