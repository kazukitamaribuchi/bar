const path = require('path')
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,

    outputDir: 'dist',
    assetsDir: 'static',
    indexPath: 'templates/index.html',

    css: {
        loaderOptions: {
            scss: {
                additionalData: `@import "./src/assets/scss/prepends.scss";`,
                // prependData: '@import "./src/assets/scss/prepends.scss";',
            }
        }
    },
    // devServer: {
    //     allowedHosts: ['localhost', '0.0.0.0'],
    //     host: '0.0.0.0',
    //     port: 8080,
    //     hot: true,
    //     headers: {
    //         'Access-Control-Allow-Origin': ['\*']
    //     },
    //     watchFiles: [
    //         'src/**/*.vue',
    //         'src/**/*',
    //     ]
    // },
    configureWebpack: {
        devServer: {
            // allowedHosts: ['localhost', '0.0.0.0'],
            host: '0.0.0.0',
            port: 8080,
            hot: true,
            headers: {
                'Access-Control-Allow-Origin': ['\*']
            },
            // watchFiles: [
            //     'src/**/*.vue',
            //     'src/**/*',
            //     'src/*',
            //     'public/*'
            // ],
            // static: {
            //     directory: path.join(__dirname, 'public'),
            //     watch: {
            //         ignored: '/node_modules/',
            //         usePolling: true,
            //         interval: 100,
            //     }
            // },
        },
        watchOptions: {
            poll: 1000,
            ignored: /node_modules/,
            aggregateTimeout: 300,
        },
        // watch: true,
    }
})
