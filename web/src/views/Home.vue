<template>
    <div
        id="home_wrap"
        fluid
    >
        <div v-if="!initStatus" class="loading">
            <div class="loading_icon">
                <b-spinner
                    style="width: 6rem; height: 6rem; display: block; margin: 0 auto;"
                    label="Large Spinner"
                    variant="light"
                ></b-spinner>
            </div>
        </div>
        <div v-else style="height: 100%;">
            <Header/>
            <b-row class="content_wrap">
                <Sidebar/>
                <div class="content">
                    <div align="right" style="color: white; position: absolute; top: 105px; right: 80px; font-size: 15px; float: right; width: 300px;">
                        システム時刻: {{ currentTime }}
                    </div>
                    <Top/>
                </div>
            </b-row>
        </div>
    </div>
</template>

<script>
import Header from '@/components/common/Header'
import Sidebar from '@/components/common/Sidebar'
import Top from '@/components/page/Top'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'HomeItem',
    components: {
        Header,
        Sidebar,
        Top
    },
    created () {
        if (!this.$store.state.isAuth) {
            this.$router.push('/')
        }

        if (!this.initStatus && this.$store.state.isAuth) {
            this.appInitAction()
            .then(res => {
                this.getCurrentTime()
                this.setInitStatus(true)
            })
            .catch(e => {
                console.log(e)
            })
        }
    },
    computed: {
        ...mapGetters([
            'initStatus',
            'currentTime',
        ])
    },
    methods: {
        ...mapMutations([
            'setInitStatus',
            // 'setProductList',
            // 'setCustomerList',
            // 'setCastList',
            // 'setQuestionList',
            // 'setSalesList',
            // 'setProductByCategoryList',
            // 'setPopularProductList',
        ]),
        ...mapActions([
            'appInitAction',
            'getCurrentTime',
            // 'getProductList',
            // 'getProductByCategoryList',
            // 'getPopularProductList',
            // 'getCustomerList',
            // 'getCastList',
            // 'getQuestionList',
            // 'getSalesList',
        ])
    }
}
</script>

<style lang="scss" scoped>
    #home_wrap {
        // padding: 0;

        background-color: $theme-color;

        height: $home-height;
        .content_wrap {

            background-color: $theme-color2;

            height: calc( #{$content-height} - #{$header-height} );

            display: flex;
            display: -webkit-flex;

            .content {
                width: $content-width;
            }
        }

        .loading {
            height: 100%;
            width: 100%;
            .loading_icon {
                display: block;
                margin: 0 auto;
                padding-top: 20%;
            }
        }
    }
</style>
