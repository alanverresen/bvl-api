#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file contains all exceptions raised by this package.

from pytz import timezone


# Base API
API_BASE_URL = "https://vblcb.wisseq.eu/VBLCB_WebService/data/"

# Timezone
TIMEZONE = timezone("Europe/Brussels")

# default time
DEFAULT_TIME = (0, 0)

# default date
DEFAULT_DATE = (1980, 1, 1)
