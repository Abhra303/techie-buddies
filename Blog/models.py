from django.db import models
from django.utils import timezone
from ckeditor import fields
import datetime

# Create your models here.
COUNTRY_CHOICES = [('1','Afghanistan'),('2','Albania'),('3','Algeria'),('4','Andorra'),('5','Angola'),('6','Antigua and Barbuda'),('7','Argentina'),('8','Armenia'),('9','Australia'),('10','Austria'),('11','Azerbaijan'),
('12','Bahamas'),('13','Bahrain'),('14','Bangladesh'),('15','Barbados'),('16','Belarus'),('17','Belgium'),('18','Belize'),('19','Benin'),('20','Bhutan'),('21','Bolivia'),('22','Bosnia and Herzegovina'),('23','Botswana'),
('24','Brazil'),('25','Brunei'),('26','Bulgaria'),('27','Burkina Faso'),('28','Burundi'),('29','Côte d"Ivoire'),('30','Cabo Verde'),('31','Cambodia'),('32','Cameroon'),('33','Canada'),('34','CentralAfricanRepublic'),('35','Chad'),
('36','Chile'),('37','China'),('38','Colombia'),('39','Congo'),('40','Costa Rica'),('41','Croatia'),('42','Cuba'),('43','Cyprus'),('44','Czechia (Czech Republic)'),('45','Democratic Republic of the Congo'),('46','Denmark'),
('47','Djibouti'),('48','Dominica'),('49','Dominican Republic'),('50','Ecuador'),('51','Egypt'),('52','El Salvador'),('53','Equatorial Guinea'),('54','Eritrea'),('55','Estonia'),('56','Eswatini (fmr. "Swaziland")'),
('57','Ethiopia'),('58','Fiji'),('59','Finland'),('60','France'),('61','Gabon'),('62','Gambia'),('63','Georgia'),('64','Germany'),('65','Ghana'),('66','Greece'),('67','Grenada'),('68','Guatemala'),('69','Guinea'),
('70','Guinea-Bissau'),('71','Guyana'),('72','Haiti'),('73','Holy See'),('74','Honduras'),('75','Hungary'),('76','Iceland'),('77','India'),('78','Indonesia'),('79','Iran'),('80','Iraq'),('81','Ireland'),('82','Israel'),
('83','Italy'),('84','Jamaica'),('85','Japan'),('86','Jordan'),('87','Kazakhstan'),('88','Kenya'),('89','Kuwait'),('90','Kyrgyzstan'),('91','Laos'),('92','Latvia'),('93','Zimbabwe'),('94','Kazakhstan'),('95','Kenya'),
('96','Kiribati'),('97','North Korea'),('98','South Kosovo'),('99','South Korea'),('100','Kyrgyzstan'),('101','Lebanon'),('102','Lesotho'),('103','Liberia'),('104','Libya'),('105','Liechtenstein'),('106','Lithuania'),
('107','Luxembourg'),('108','Madagascar'),('109','Malawi'),('110','Malaysia'),('111','Maldives'),('112','Mali'),('113','Malta'),('114','Marshall Islands'),('115','Mauritania'),('116','Mauritius'),('117','Mexico'),
('118','Micronesia'),('119','Federated States of Moldova'),('120','Monaco'),('121','Mongolia'),('121','Montenegro'),('122','Morocco'),('123','Mozambique'),('124','Myanmar (Burma)'),('125','Namibia'),('126','Nauru'),
('127','Nepal'),('128','Netherlands'),('129','New Zealand'),('130','Nicaragua'),('131','Niger'),('132','Nigeria'),('133','North Macedonia'),('134','Norway'),('135','Oman'),('136','Pakistan'),('137','Panama'),
('138','Papua New Guinea'),('139','Paraguay'),('140','Peru'),('141','Philippines'),('142','Poland'),('143','Portugal'),('144','Qatar'),('145','Romania'),('146','Russia'),('147','Rwanda'),('148','Saint Kitts and Nevis'),
('149','Saint Lucia'),('150','Saint Vincent and the Grenadines'),('151','Samoa'),('152','San Marino'),('153','Sao Tome and Principe'),('154','Saudi Arabia'),('155','Senegal'),('156','Serbia'),('157','Seychelles'),
('158','Sierra Leone'),('159','Singapore'),('160','Slovakia'),('161','Slovenia'),('162','Solomon Islands'),('163','Somalia'),('164','South Africa'),('165','Spain'),('166','Sri Lanka'),('167','Sudan'),('168',' South Suriname'),
('169','Sweden'),('170','Switzerland'),('171','Syria'),('172','Taiwan'),('173','Tajikistan'),('174','Tanzania'),('175','Thailand'),('176','Togo'),
('177','Tonga'),('178','Trinidad and Tobago'),('179','Tunisia'),('180','Turkey'),('181','Turkmenistan'),('182','Tuvalu'),('183','Uganda'),('184','Ukraine')]

class Author(models.Model):

    name = models.CharField(max_length = 45)
    country = models.CharField(max_length = 45,choices=COUNTRY_CHOICES)
    works_at = models.CharField(max_length=48)
    description = fields.RichTextField(blank=True,null=True)
    image = models.ImageField(blank = True,upload_to='Blog/images',null = True)
    email = models.EmailField(blank=True,null=True)
    facebook_url = models.URLField(blank=True,null=True)
    instagram_url = models.URLField(blank=True,null=True)
    twitter_url = models.URLField(blank=True,null=True)
    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    heading = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    content = fields.RichTextField()
    author = models.ForeignKey(Author,on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tag,related_name='blogs')
    read = models.IntegerField(default=0,editable=False)
    # like = models.ManytoManyField(User,related_name='like_users')
    front_img = models.ImageField(blank=True,upload_to='Blog/images',null = True)
    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days= 2)
    
    class Meta:
        ordering=['-id']
    
    def __str__(self):
        return self.heading

# class User(models.Model):
#     name = models.CharField(max_length=50)
#     username = models.CharField(max_length=20)
#     email_id = models.EmailField(unique=True)
#     phone_num = models.PositiveIntegerField()
#     description = fields.RichTextField(blank = True)
#     password = models.CharField(max_length=15)

#     def __str__(self):
#         return self.name

