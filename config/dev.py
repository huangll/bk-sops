# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2020 THL A29 Limited, a Tencent company. All rights reserved.
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
    from blueapps.patch.settings_paas_services import *  # noqa

# 本地开发环境Å
RUN_MODE = "DEVELOP"

# APP本地静态资源目录
STATIC_URL = "/static/"

# APP静态资源目录url
# REMOTE_STATIC_URL = '%sremote/' % STATIC_URL

# Celery 消息队列设置 RabbitMQ
# BROKER_URL = 'amqp://guest:guest@localhost:5672/'
# Celery 消息队列设置 Redis
BROKER_URL = "redis://localhost:6379/0"

DEBUG = False

# 本地开发数据库设置
# USE FOLLOWING SQL TO CREATE THE DATABASE NAMED APP_CODE
# SQL: CREATE DATABASE `bk_sops` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": APP_CODE,
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "3306",
        "TEST": {"NAME": "test_sops", "CHARSET": "utf8", "COLLATION": "utf8_general_ci"},
    },
}
# 权限中心 SDK 无权限时不返回 499 的请求路径前缀配置
BK_IAM_API_PREFIX = os.getenv("BKAPP_BK_IAM_API_PREFIX", SITE_URL + "apigw")

LOG_PERSISTENT_DAYS = 1

LOGGING["loggers"]["iam"] = {
    "handlers": ["component"],
    "level": "DEBUG",
    "propagate": True,
}

# CELERY_ALWAYS_EAGER = True
# TEST_RUNNER = 'djcelery.contrib.test_runner.' \
#               'CeleryTestSuiteRunnerStoringResult'

# 多人开发时，无法共享的本地配置可以放到新建的 local_settings.py 文件中
# 并且把 local_settings.py 加入版本管理忽略文件中
try:
    from local_settings import *  # noqa
except ImportError:
    pass

LOGGING["handlers"]["engine_component"] = {
    "class": "pipeline.log.handlers.EngineContextLogHandler",
    "formatter": "verbose",
}

LOGGING["loggers"]["component"] = {
    "handlers": ["component", "engine_component"],
    "level": "DEBUG",
    "propagate": True,
}

LOGGING["formatters"]["light"] = {"format": "%(message)s"}

LOGGING["handlers"]["engine"] = {
    "class": "pipeline.log.handlers.EngineLogHandler",
    "formatter": "light",
}

LOGGING["loggers"]["pipeline.logging"] = {
    "handlers": ["engine"],
    "level": "INFO",
    "propagate": True,
}

# 多环境需要，celery的handler需要动态获取
LOGGING["loggers"]["celery_and_engine_component"] = {
    "handlers": ["engine_component", LOGGING["loggers"]["celery"]["handlers"][0]],
    "level": "INFO",
    "propagate": True,
}
