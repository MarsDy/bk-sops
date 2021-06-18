# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from config import RUN_VER

if RUN_VER == "open":
    from blueapps.patch.settings_open_saas import *  # noqa
else:
    from blueapps.patch.settings_paas_services import *  # noqaJobExecuteTaskComponent

import env


BROKER_URL = "redis://localhost:6379/0"

# stag数据库设置
# USE FOLLOWING SQL TO CREATE THE DATABASE NAMED APP_CODE
# SQL: CREATE DATABASE `bk_sops` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": APP_CODE,
        "USER": "root",
        "PASSWORD": "oF7Df72P_NWs",
        "HOST": "mysql-default.service.consul",
        "PORT": "3306",
        "TEST": {"NAME": "test_sops", "CHARSET": "utf8", "COLLATION": "utf8_general_ci"},
    },
}


# 预发布环境
RUN_MODE = "STAGING"

BK_IAM_SYNC_TEMPLATES = True

BK_IAM_RESOURCE_API_HOST = env.BK_IAM_RESOURCE_API_HOST

CSRF_COOKIE_NAME = APP_CODE + "_csrftoken"

default.logging_addition_settings(LOGGING, environment="stag")
