from django.db import models
from django.db.models.deletion import CASCADE

#데이타베이스 안의 테이블 만들기


#메뉴
class Menu(models.Model):
    name = models.CharField(max_length=20) #db 필드, column
    class Meta:
        db_table = 'menus' # 테이블 이름 - 소문자,복수형으로


# 카테고리 
class Category(models.Model):
    name = models.CharField(max_length=20) 
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE) #menu_id

    class Meta:
        db_table = 'categories' # 테이블 이름

#프로덕트
class Product(models.Model):
    name     = models.CharField(max_length=100) #db 필드 
    korean_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE) #nutrition_id
    category = models.ForeignKey('Category', on_delete=models.CASCADE) #category_id

    class Meta:
            db_table = 'products' # 테이블 이름


#이미지
class Image(models.Model):
    image_url = models.CharField(max_length=300)
    product = models.ForeignKey('Product',on_delete=CASCADE) #product_id

    class Meta:
        db_table = 'images' # 테이블 이름



 #영양소
class Nutrition(models.Model):
    one_serving_kca = models.DecimalField(max_digits=6,decimal_places=2)
    sodium_mg =  models.DecimalField(max_digits=6,decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=6,decimal_places=2)  
    sugars_g  = models.DecimalField(max_digits=6,decimal_places=2)
    protein_g = models.DecimalField(max_digits=6,decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=6,decimal_places=2)
    size_ml = models.CharField(max_length=100)
    size_fluid_ounce = models.CharField(max_length=100)

    class Meta:
        db_table = 'nutritions'
        

# 알러지
class Allergy(models.Model):
    name = models.CharField(max_length=20) 
    
    class Meta:
        db_table = 'allergy' # 테이블이름


# 알러지 - 프로덕트
class Allergyproduct(models.Model):
    allergy = models.ForeignKey('Allergy',on_delete=models.CASCADE) #allergy_id
    Product = models.ForeignKey('Product', on_delete=models.CASCADE) # product_id
    
    class Meta:
        db_table =  'allergy_products' # 테이블 이름


    