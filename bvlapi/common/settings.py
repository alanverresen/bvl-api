#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains several settings used by packages.

from pytz import timezone


# base URL of API
API_BASE_URL = "https://vblcb.wisseq.eu/VBLCB_WebService/data/"

# timezone of data retrieved
TIMEZONE = timezone("Europe/Brussels")

# default time
DEFAULT_TIME = (0, 0)

# default date
DEFAULT_DATE = (1980, 1, 1)
