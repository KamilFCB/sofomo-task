from django.db import models


# class Languages(models.Model):
#     code = models.CharField(max_length=5)
#     name = models.CharField(max_length=100)
#     native = models.CharField(max_length=100)
#
#
# class Location(models.Model):
#     geoname_id = models.IntegerField()
#     capital = models.CharField(max_length=100)
#     languages = models.ForeignKey(Languages, on_delete=models.CASCADE)
#     country_flag = models.CharField(max_length=200)
#     country_flag_emoji = models.CharField(max_length=5)
#     country_flag_emoji_unicode = models.CharField(max_length=100)
#     calling_code = models.CharField(max_length=5)
#     is_ue = models.BooleanField()
#
#
# class TimeZone(models.Model):
#     timezone_id = models.CharField(max_length=100)
#     current_time = models.DateTimeField()
#     gmt_offset = models.IntegerField()
#     code = models.CharField(max_length=5)
#     is_daylight_saving = models.BooleanField()
#
#
# class Currency(models.Model):
#     code = models.CharField(max_length=5)
#     name = models.CharField(max_length=100)
#     plural = models.CharField(max_length=100)
#     symbol = models.CharField(max_length=10)
#     symbol_native = models.CharField(max_length=10)
#
#
# class Connection(models.Model):
#     asn = models.IntegerField()
#     isp = models.CharField(max_length=100)
#
#
# class Security(models.Model):
#     is_proxy = models.BooleanField()
#     proxy_type = models.CharField(max_length=100)
#     is_crawler = models.BooleanField()
#     crawler_name = models.CharField(max_length=100)
#     crawler_type = models.CharField(max_length=100)
#     is_tor = models.BooleanField()
#     threat_level = models.CharField(max_length=100)
#     threat_types = models.CharField(max_length=100)


class Geolocation(models.Model):
    ip = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    # continent_code = models.CharField(max_length=5)
    continent_name = models.CharField(max_length=100)
    # country_code = models.CharField(max_length=5)
    country_name = models.CharField(max_length=100)
    # region_code = models.CharField(max_length=5)
    region_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=6)
    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # time_zone = models.ForeignKey(TimeZone, on_delete=models.CASCADE)
    # currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    # connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
    # security = models.ForeignKey(Security, on_delete=models.CASCADE)
