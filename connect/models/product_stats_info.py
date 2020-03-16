# -*- coding: utf-8 -*-

# This file is part of the Ingram Micro Cloud Blue Connect SDK.
# Copyright (c) 2020 Ingram Micro. All Rights Reserved.

from .base import BaseModel
from .schemas import ProductStatsInfoSchema


class ProductStatsInfo(BaseModel):
    _schema = ProductStatsInfoSchema()

    distribution = None  # type: int
    """ (int) Number of distributions related to the product. """

    sourcing = None  # type: int
    """ (int) Number of sourcings related to the product. """
