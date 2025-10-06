import os
import django
from datetime import datetime, timedelta
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amr_project.settings_production')
django.setup()

from amr_api.models import LabResult

# Sample data
organisms = ['E. coli', 'S. aureus', 'K. pneumoniae', 'P. aeruginosa']
antibiotics = ['Amoxicillin', 'Ciprofloxacin', 'Gentamicin', 'Ceftriaxone', 'Vancomycin']
facilities = ['Central Hospital', 'City Lab', 'Regional Medical Center', 'Community Clinic']
specimen_types = ['Blood', 'Urine', 'Sputum', 'Wound']
susceptibility = ['S', 'I', 'R']  # Susceptible, Intermediate, Resistant

def create_sample_data():
    print("Creating sample lab results...")
    
    # Clear existing data
    LabResult.objects.all().delete()
    
    # Create 20 sample records
    for i in range(1, 21):
        lab_result = LabResult(
            patient_id=f"PAT{1000 + i}",
            specimen_type=random.choice(specimen_types),
            organism=random.choice(organisms),
            antibiotic=random.choice(antibiotics),
            susceptibility=random.choice(susceptibility),
            test_date=datetime.now() - timedelta(days=random.randint(1, 365)),
            facility=random.choice(facilities),
            patient_age=random.randint(18, 80),
            patient_sex=random.choice(['M', 'F'])
        )
        lab_result.save()
        print(f"Created lab result {i}: {lab_result}")
    
    print(f"Sample data created! Total records: {LabResult.objects.count()}")

if __name__ == "__main__":
    create_sample_data()
