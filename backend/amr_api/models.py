from django.db import models

class LabResult(models.Model):
    patient_id = models.CharField(max_length=100)
    specimen_type = models.CharField(max_length=100)
    organism = models.CharField(max_length=100)
    antibiotic = models.CharField(max_length=100)
    susceptibility = models.CharField(max_length=50)  # S, I, R
    test_date = models.DateField()
    facility = models.CharField(max_length=200)
    patient_age = models.IntegerField(null=True, blank=True)
    patient_sex = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.organism} - {self.antibiotic} - {self.susceptibility}"
    
    class Meta:
        db_table = 'amr_lab_results'
