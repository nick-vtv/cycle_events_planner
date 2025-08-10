from django.db import models


class RouteDifficultyChoices(models.TextChoices):
    BEGINNER = 'beginner', 'Beginner (easy level, best for training)'
    INTERMEDIATE = 'intermediate', 'Intermediate (medium level, lots of fun)'
    ADVANCED = 'advanced', 'Advanced (high level, for skilled raiders)'
    HARD = 'hard', 'Hard (expert level, for bike sports enthusiasts)'
    EXTREME = 'extreme', 'Extreme (extremal level, only top thrill seekers go here)'


class RouteTypeChoices(models.TextChoices):
    ROAD = 'road', 'Road trip (best for road and gravel bike owners)'
    URBAN = 'urban', 'Urban exploring (riding across towns and cities)'
    MIXED = 'mixed', 'Mixed type route (both nature and urban locations)'
    CC = 'crosscountry', 'CrossCountry classic (into the wild)'
    CC_COMPETITION = 'competition', 'CrossCountry competition racetrack (best for CC enthusiasts practicing)'
    AM = 'allmountain', 'AllMountain route type (both uphills and downhills - mountains at its best)'
    TRAIL = 'trail', 'Trail (prepared tracks, mostly downhills)'
    ENDURO = 'enduro', 'Enduro (same as trails, but more technical and extreme)'
    FREERIDE =  'free', 'FreeRide (explore the unexplored)'
    DOWNHILL = 'downhill', 'Downhill (classic DH tracks)'
