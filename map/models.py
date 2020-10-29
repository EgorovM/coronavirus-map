import datetime

from django.db import models


class Sick(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    detection_date = models.DateField()
    is_exactly = models.BooleanField(default=False)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.name

    def from_post(post):
        sick = Sick()
        fields = ['name', 'address', 'latitude', 'longitude']

        for field in fields:
            setattr(sick, field, post.get(field))

        sick.is_exactly = False if post.get('is_exactly', None) is None else True
        sick.detection_date = datetime.datetime.strptime(post.get('detection_date'), "%Y-%m-%d").date()

        return sick

    def get_geojson():
        return {
            "type": "FeatureCollection",
            "crs": {
                "type": "name",
                "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
            "features": [{
                    "type": "Feature",
                    "properties": {
                        "id": point.id,
                        "is_exactly": point.is_exactly,
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [point.longitude, point.latitude]

                    }} for point in Sick.objects.all()]}

    def get_points_dict():
        return dict(
            [(point.id, (str(point.longitude), str(point.latitude),
            {
                'is_exactly': point.is_exactly,
                'detection_date': point.detection_date.strftime('%d/%m/%y'),
                'address': point.address,
            }))
            for point in Sick.objects.all()]
        )
