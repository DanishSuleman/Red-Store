from django.http import HttpResponse
from django.shortcuts import render
# Products Model
from apps.products.models import Product
# Brands Model
from apps.brands.models import Brand
# Testimonials Model
from apps.testimonials.models import Testimonial
# Team Members Model
from apps.team_members.models import Team_Member
# Contact Form
from .forms import ContactForm
# Send Mails and Render To String
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Paginator
from django.core.paginator import Paginator
from django.db.models import Q


#All Products
all_products = Product.objects.all()

# HomePage
def index(req):
    data = {
        'title': 'Home - RedStore'
    }
    brands = Brand.objects.all()
    testimonials = Testimonial.objects.all()
    products = all_products.filter(isFeatured=0)[:8]
    featured_product = all_products.filter(isFeatured=1)
    data['products'] = products
    data['brands'] = brands
    data['testimonials'] = testimonials
    data['featured_product'] = featured_product
    return render(req, 'homepage/index.html', data)

# Products Listing Page
def productListingPage(req):

    data = {
        'title': 'All Products - RedStore'
    }
    paginator = Paginator(all_products, per_page=12) # Show 12 products per page.
    page_number = req.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    data['products'] = page_obj.object_list
    data['paginator'] = paginator
    data["page_number"] = int(page_number)
    data['page_obj'] = page_obj

    return render(req, "products/products.html", data)

# About Page
def about(req):
    data = {
        'title': 'About - RedStore'
    }

    all_team_members = Team_Member.objects.all()

    data['all_team_members'] = all_team_members

    return render(req, 'about/about.html', data)

# Contact Page
def contact(req):

    contactForm = ContactForm()
        
    return render(req, 'contact/contact.html', {
        'contactForm': contactForm,
        'title': 'Contact - RedStore'
    })

# Submit Contact Page 
def contactSubmit(req):

    if req.method == 'POST':
        form = ContactForm(req.POST)

        if form.is_valid():
            emailData = {
                'full_name': req.POST['full_name'],
                'email': req.POST['email'],
                'message': req.POST['message']
            }

            email_html = render_to_string('emails/contact.html', emailData)

            send_mail(
                'Contact Form',
                'Thank you for contacting us',
                'noreply@redstore.com',
                ['danish.sulaiman@outlook.com'],
                fail_silently=False,
                html_message=email_html
            )
            return HttpResponse("<h2>Your Message Has Been Sent Successfully, We Will Get Back To You Soon! </h2> <a href='../'>Go Back</a>")
        else:
            return render(req, 'contact/contact.html', {
                'contactForm': form
            })  
    else:
        return HttpResponse("<h2>Method Not Accepted</h2> <a href='../'>Go Back</a>")


# Product Details Page
def product_details(req, primary_key):
    data = {
        'title': 'Product Details - RedStore'
    }
    each_product = Product.objects.get(id=primary_key)
    similar_products = all_products.filter(category=each_product.category).filter(~Q(id=primary_key))
    data['each_product'] = each_product
    data ['similar_products'] = similar_products
    return render(req, 'product_details/product_details.html', data)
