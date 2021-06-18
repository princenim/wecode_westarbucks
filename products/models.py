from django.db import models
from django.db.models.deletion import CASCADE


#데이타베이스 안의 테이블 만들기
class Menu(models.Model):
    name = models.CharField(max_length=20) #db 필드 , column
    class Meta:
        db_table = 'menus' # 테이블 이름 

class Category(models.Model):
    name = models.CharField(max_length=20) 
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE) #menu_id

    class Meta:
        db_table = 'categories' # 테이블 이름

class Product(models.Model):
    name     = models.CharField(max_length=100) #db 필드 
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
            db_table = 'products' # 테이블 이름

# ------------------------------------------

# 알러지
class Allergy(models.Model):
    name = models.CharField(max_length=20) # 알러지 테이블 추가
    class Meta:
        db_table = 'allergy' # 테이블이름


# 드링크
class Drink(models.Model):
    name =  models.CharField(max_length=100)git
    category = models.ForeignKey('Category', on_delete=models.CASCADE) #category_id

    class Meta:
        db_table = 'drink' # 테이블 이름


# 알러지드링크 
class Allergydrink(models.Model):
    allergy = models.ForeignKey('Allergy',on_delete=models.CASCADE) #allergy_id
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE) # drink_id
    
    class Meta:
        db_table =  'allergydrink' # 테이블 이름

#이미지
class Image(models.Model):
    image_url =  models.CharField(max_length=300)
    drink = models.ForeignKey('Drink',on_delete=CASCADE) #drink_id

    class Meta:
        db_table = 'image' # 테이블 이름

#영양소
class Nutritions(models.Model):
    one_serving_kca = models.CharField(max_length=100)
    
    sodium_mg = models.CharField(max_length=100)
    saturated_fat_g = models.CharField(max_length=100)
    