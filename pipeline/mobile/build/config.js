/**
* Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
* Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
* Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
* http://opensource.org/licenses/MIT
* Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
*/
import path from 'path'
import prodEnv from './prod.env'
import devEnv from './dev.env'

export default {
    build: {
        env: prodEnv,
        assetsRoot: path.resolve(__dirname, '../dist'),
        assetsSubDirectory: 'static',
        assetsPublicPath: '/',
        productionSourceMap: true,
        productionGzip: false,
        productionGzipExtensions: ['js', 'css'],
        bundleAnalyzerReport: process.env.npm_config_report
    },
    dev: {
        env: devEnv,
        host: 'dev.paas-bkyovole.cloud.yovole.com',
        port: 9001,
        assetsSubDirectory: 'static',
        assetsPublicPath: '/',
        proxyTable: {
            '/ajax': { // 需要代理的路径
                target: 'http://dev.paas-bkyovole.cloud.yovole.com:8000/', // 目标服务器host
                secure: false,
                pathRewrite: {
                    '^/ajax': ''
                },
                headers: {
                    referer: 'dev.paas-bkyovole.yovole.com' // 目标服务器host
                }
            }
        },
        cssSourceMap: false,
        autoOpenBrowser: false
    }
}
