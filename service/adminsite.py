#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2023/03/31 11:44:04
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   admin site
'''
from fastapi_amis_admin.admin.settings import Settings
from fastapi_amis_admin.admin.site import AdminSite
from fastapi_scheduler import SchedulerAdmin
from fastapi.responses import JSONResponse

site = AdminSite(settings=Settings(
    database_url_async='sqlite+aiosqlite:///amisadmin.db'))


# @site.register_admin
# class Admin(admin.IframeAdmin):
    