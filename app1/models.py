from django.db import models
from embed_video.fields import EmbedVideoField



vid_type = (
    ("1", "virals"),
    ("2", "movies"),
    ("3", "shortfilms"),
    ("4", "webshows"),

)


vid_ctg = (
    ("1", "action"),
    ("2", "comedy"),
    ("3", "suspence,drama thrils"),
    ("4", " biopic"),

)


class Home(models.Model):
    video = EmbedVideoField()
    title = models.CharField(max_length=100, default="none")
    vid_type = models.CharField(max_length=20, default="1", choices=vid_type)
    vid_cotegory = models.CharField(
        max_length=20, default="1", choices=vid_ctg)


class Viral(models.Model):
    video = EmbedVideoField()
    title = models.CharField(max_length=100, default="none")
    vid_cotegory = models.CharField(
        max_length=20, default="1", choices=vid_ctg)


class Movie(models.Model):
    video = EmbedVideoField()
    title = models.CharField(max_length=100, default="none")
    vid_cotegory = models.CharField(
        max_length=20, default="1", choices=vid_ctg)


class Shortfilm(models.Model):
    video = EmbedVideoField()
    title = models.CharField(max_length=100, default="none")
    vid_cotegory = models.CharField(
        max_length=20, default="1", choices=vid_ctg)


class Webshow(models.Model):
    video = EmbedVideoField()
    title = models.CharField(max_length=100, default="none")
    vid_cotegory = models.CharField(
        max_length=20, default="1", choices=vid_ctg)
