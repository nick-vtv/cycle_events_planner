from django.db import models


class BikeTypeChoices(models.TextChoices):
    CITY = 'city', 'City Bike'
    GRAVEL = 'gravel', 'Gravel Bike'
    HYBRID = 'hybrid', 'Hybrid Bike'
    MTB = 'mtb', 'Mountain Bike (MTB)'
    ROAD = 'road', 'Road Bike'
    TOURING = 'touring', 'Touring Bike'


class BikeGeometryChoices(models.TextChoices):
    RIGID = 'rigid', 'Rigid Frame (no suspension)'
    HARDTAIL = 'hardtail', 'Hardtail Frame (front suspension)'
    FULL = 'full', 'Full Suspension Frame (front and rear suspension)'
