import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smarthire.settings')
django.setup()

from jobs.models import Job
from users.models import User

def create_sample_data():
    # 1. Create a sample employer if not exists
    employer, created = User.objects.get_or_create(
        username='google_recruiter',
        email='recruiter@google.com',
        is_employer=True,
        is_job_seeker=False
    )
    if created:
        employer.set_password('password123')
        employer.save()

    # 2. Sample Jobs
    jobs_data = [
        {
            'title': 'Senior Python Developer',
            'location': 'Bangalore, India',
            'category': 'IT & Software',
            'salary': '₹15L - ₹25L',
            'description': 'We are looking for a Python expert with 5+ years of experience in Django and FastAPI. You will be building scalable backend systems for our cloud infrastructure.'
        },
        {
            'title': 'Frontend React Engineer',
            'location': 'Remote / USA',
            'category': 'Web Development',
            'salary': '$80k - $120k',
            'description': 'Join our creative team to build stunning user interfaces using React, Tailwind CSS, and Framer Motion.'
        },
        {
            'title': 'Digital Marketing Specialist',
            'location': 'New Delhi, India',
            'category': 'Marketing',
            'salary': '₹6L - ₹10L',
            'description': 'Handle SEO, SEM, and social media campaigns for top-tier clients in the e-commerce sector.'
        },
        {
            'title': 'Graphic Designer',
            'location': 'Mumbai, India',
            'category': 'Design',
            'salary': '₹4L - ₹8L',
            'description': 'Creative designer needed for branding, UI icons, and marketing collateral. Must be proficient in Adobe Creative Suite.'
        },
        {
            'title': 'Data Scientist',
            'location': 'Hyderabad, India',
            'category': 'Data Science',
            'salary': '₹12L - ₹20L',
            'description': 'Work with massive datasets to build predictive models and extract business insights using Machine Learning.'
        }
    ]

    for job in jobs_data:
        Job.objects.get_or_create(
            employer=employer,
            title=job['title'],
            defaults={
                'location': job['location'],
                'category': job['category'],
                'salary': job['salary'],
                'description': job['description']
            }
        )

    print("✅ Sample data added successfully!")
    print(f"Username: {employer.username}")
    print("Password: password123")

if __name__ == '__main__':
    create_sample_data()
