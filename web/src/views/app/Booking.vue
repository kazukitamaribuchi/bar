<template>
    <b-container
        id="booking_wrap"
        fluid
    >
        <Header/>
        <b-row class="content_wrap">
            <Sidebar/>
            <div class="content">
                <div align="right" style="color: white; position: absolute; top: 105px; right: 80px; font-size: 15px; float: right; width: 300px;">
                    システム時刻: {{ currentTime }}
                </div>
                <router-view/>
            </div>
        </b-row>
    </b-container>
</template>

<script>
import Header from '@/components/common/Header'
import Sidebar from '@/components/common/Sidebar'
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'BookingItem',
    data: () => ({
    }),
    components: {
        Header,
        Sidebar,
    },
    computed: {
        ...mapGetters([
            'currentTime'
        ]),
    },
    created () {
        this.getCurrentTime()
    },
    methods: {
        ...mapActions([
            'getCurrentTime',
        ]),
    }
}
</script>

<style lang="scss" scoped>
    #booking_wrap {
        height: $home-height;
        .content_wrap {

            background-color: $theme-color2;

            min-height: calc( #{$content-height} - #{$header-height} );

            display: flex;
            display: -webkit-flex;

            .content {
                width: $content-width;
                height: $content-height;
            }
        }
    }
</style>
