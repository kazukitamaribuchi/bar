<template>
    <v-app>
        <!-- <Header
            v-if="isAuth"
        /> -->
        <router-view/>
        <v-overlay
            :value="humMenu"
            :zIndex="0"
        ></v-overlay>
    </v-app>
</template>

<script>
import Header from '@/components/account/Header'
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'KitchenItem',
    data: () => ({
        humMenu: false,
    }),
    components: {
        Header,
    },
    computed: {
        ...mapGetters([
            'isAuth',
        ])
    },
    beforeCreate () {
    },
    created () {
    },
    beforeMount () {
    },
    mounted () {
        if (!this.isAuth) {
            this.$router.push({ name: 'KitchenLogin' })
        }

        const scheme = window.location.protocol === 'https:' ? 'wss' : 'ws'
        const hostName = process.env.NODE_ENV !== 'production' ? process.env.VUE_APP_BASE_URL : window.location.host
        // const hostName = 'localhost:8000'
        console.log('process.env.NODE_ENV', process.env.NODE_ENV)
        console.log('window.location.host', window.location.host)
        console.log('process.env.VUE_APP_BASE_URL', process.env.VUE_APP_BASE_URL)
        const url = scheme + '://' + hostName + '/ws/order/' + this.$store.state.loginUser + '/'

        if (this.ws === undefined || this.ws.readyState !== 1) {
            this.ws = new WebSocket(url)
            console.log('this.ws', this.ws)
        }

        this.ws.onmessage = e => {
            var receiveData = JSON.parse(e.data)
            console.log('ソケット結果受信', receiveData)
            switch (receiveData.type) {
                case 0:
                    // 新規オーダー
                    this.$eventHub.$emit('addNewOrder', receiveData.content)
                    break
                case 99:
                    // 伝票締め
                    this.$eventHub.$emit('closeSalesHeader', receiveData.content)
                    break
                default:
                    break
            }
        }
    },
    beforeUpdate () {
    },
    update () {
    },
    beforeDestroy () {
        this.closeWs()
    },
    destoryd () {
    },
    methods: {
        closeWs () {
            if (this.ws !== undefined && this.ws.readyState !== 3) {
                this.ws.close()
            }
        }
    }
}
</script>

<style lang="scss">
    html.overflow-y-hidden {
        overflow-y: auto !important;
    }

    // .humActive {
    //     background: yellow;
    //     z-index: 9999;
    // }
</style>
