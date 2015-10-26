from django.db import models

CROP_NAME = [
  '',
  'Corn',  # 1
  'Cotton',
  'Rice',
  'Sorghum',
  'Soybeans',
  'Sunflower',
  '',
  '',
  '',
  'Peanuts', # 10
  'Tobacco',
  'Sweet Corn',
  'Pop or Ornamental Corn',
  'Mint',
  '',
  '',
  '',
  '',
  '',
  '', # 20
  'Barley',
  'Durum Wheat',
  'Spring Wheat',
  'Winter Wheat',
  'Other Small Grains',
  'Double Crop - Winter Wheat / Soybeans',
  'Rye',
  'Oats',
  'Millet',
  'Spelt', # 30
  'Canola',
  'Flaxseed',
  'Safflower',
  'Rape Seed',
  'Mustard',
  'Alfalfa',
  'Other Hay (non-alfalfa)',
  'Camelina',
  'Buckwheat',
  '', # 40
  'Sugarbeets',
  'Dry Beans',
  'Potatoes',
  'Other Crops',
  'Sugarcane',
  'Sweet Potatoes',
  'Misc Vegs & Fruits',
  'Watermelons',
  'Onions',
  'Cucumbers', # 50
  'Chick Peas',
  'Lentils',
  'Peas',
  'Tomatoes',
  'Caneberries',
  'Hops',
  'Herbs',
  'Clover/Wildflowers',
  'Sod/Grass Seed',
  'Switchgrass', # 60
  '', # 'Fallow/Idle Cropland',
  'Pasture/Grass',
  '', # 'Forest',
  '', # 'Shrubland',
  'Barren',
  'Cherries',
  'Peaches',
  'Apples',
  'Grapes',
  'Christmas Trees', # 70
  'Other Tree Crops',
  'Citrus',
  '',
  'Pecans',
  'Almonds',
  'Walnuts',
  'Pears',
  '',
  '',
  '', # 80
  '', # 'Clouds/No Data',
  '', # 'Developed',
  '', # 'Water',
  '',
  '',
  '',
  '', # 'Wetlands',
  'Non-ag/Undefined',
  '',
  '', # 90
  '',
  'Aquaculture',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '', # 100
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '', # 110
  '', # 'Open Water',
  '', # 'Perennial Ice/Snow',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '', # 120
  '', # 'Developed - Open Space',
  '', # 'Developed - Low Intensity',
  '', # 'Developed - Medium Intensity',
  '', # 'Developed - High Intensity',
  '',
  '',
  '',
  '',
  '',
  '', # 130
  '', # 'Barren',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '', # 140
  '', # 'Deciduous Forest',
  '', # 'Evergreen Forest',
  '', # 'Mixed Forest',
  '',
  '',
  '',
  '',
  '',
  '',
  '', # 150
  '',
  '', # 'Shrubland',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '', # 160
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '', # 170
  '', # 'Herbaceous Grassland',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '', # 180
  'Pasture/Hay',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '', # 'Woody Wetlands', # 190
  '',
  '',
  '',
  '',
  '', # 'Herbaceous Wetlands',
  '',
  '',
  '',
  '',
  '', # 200
  '',
  '',
  '',
  'Pistachios',
  'Triticale',
  'Carrots',
  'Asparagus',
  'Garlic',
  'Cantaloupes',
  'Prunes', # 210
  'Olives',
  'Oranges',
  'Honeydew Melons',
  'Broccoli',
  '',
  'Peppers',
  'Pomegranates',
  'Nectarines',
  'Greens',
  'Plums', # 220
  'Strawberries',
  'Squash',
  'Apricots',
  'Vetch',
  'Double Crop - Winter Wheat/Corn',
  'Double Crop - Oats/Corn',
  'Lettuce',
  '',
  'Pumpkins',
  'Double Crop - Lettuce/Durum Wheat', # 230
  'Double Crop - Lettuce/Cantaloupe',
  'Double Crop - Lettuce/Cotton',
  'Double Crop - Lettuce/Barley',
  'Double Crop - Durum Wheat/Sorghum',
  'Double Crop - Barley/Sorghum',
  'Double Crop - Winter Wheat/Sorghum',
  'Double Crop - Barley/Corn',
  'Double Crop - Winter Wheat/Cotton',
  'Double Crop - Soybeans/Cotton',
  'Double Crop - Soybeans/Oats', # 240
  'Double Crop - Corn/Soybeans',
  'Blueberries',
  'Cabbage',
  'Cauliflower',
  'Celery',
  'Radishes',
  'Turnips',
  'Eggplants',
  'Gourds',
  'Cranberries', # 250
  '',
  '',
  '',
  'Double Crop - Barley/Soybeans',
  ''
]

class Crop(models.Model):
  name = models.CharField(max_length=200)

class CropPrice(models.Model):
  year = models.PositiveSmallIntegerField()
  location = models.CharField(max_length=80)
  commodity = models.CharField(max_length=40)
  variety = models.CharField(max_length=80)
  price = models.DecimalField(decimal_places=2, max_digits=8)
  util_practice = models.CharField(max_length=80)
  unit = models.CharField(max_length=40)

  class Meta:
    unique_together = ('year', 'location', 'commodity', 'variety', 'util_practice', 'unit')
    # index_together not supported by this django version
    # index_together = ('year', 'location', 'commodity')