#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio ,ORM
logging.basicConfig(level=logging.INFO)
from coroweb import get, post

from models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    users = await User.findAll()
    logging.info('Users: %s' % users)
    return {
        '__template__': 'test.html',
        'users': users
    }
  

# loop = asyncio.get_event_loop()
# asyncio.run(main())