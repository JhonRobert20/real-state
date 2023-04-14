# -*- coding: utf-8 -*-
import uuid
from typing import TYPE_CHECKING  # NOQA

from django.db import models
from django.utils.translation import gettext_lazy as _

if TYPE_CHECKING:  # pragma: no cover
    import datetime  # NOQA


class SimpleModel(models.Model):
    """
    An abstract base class model that provides:
    self-updating 'created' and 'modified' fields.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    created = models.DateTimeField(
        verbose_name=_("created date"),
        null=True,
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        verbose_name=_("modified date"), null=True, auto_now=True
    )

    class Meta:
        abstract = True
        ordering = ("-created",)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(SimpleModel, self).save(*args, **kwargs)
