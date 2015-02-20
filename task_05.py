#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""
ReturnStr = 'Your status is currently: {status}'
BP_STATUS = int(raw_input('What your blood pressure? ' ))
if BP_STATUS <= 89:
    print ReturnStr.format(status = 'Low')
elif BP_STATUS >= 90 and BP_STATUS <= 119:
     print ReturnStr.format(status = 'Ideal')
elif BP_STATUS >= 120 and BP_STATUS <= 139:
     print ReturnStr.format(status = 'Warning')
elif BP_STATUS >= 140 and BP_STATUS <= 159:
    print ReturnStr.format(status = 'High')
elif BP_STATUS >= 160:
    print ReturnStr.format(status = 'Emergency')

