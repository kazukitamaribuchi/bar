<template>
    <div id="header_wrap">
        <div>
            <i
                class='bx bx-menu header-hum'
            ></i>
        </div>
        <div class="header-title">
            {{ headerTitle }}
        </div>
    </div>
</template>

<script>

const title = {
    'AccountHome': 'ホーム',
    'AccountOrderSelect': 'オーダー',
    'AccountOrderCheckSelect': '注文確認',
    'AccountNewVisit': '新規入店',
    'AccountBottle': 'ボトル',
    'AccountCustomer': '顧客情報照会',
}

export default {
    name: 'HeaderItem',
    data: () => ({
        activeItem: {}
    }),
    components: {
    },
    computed: {
        headerTitle () {
            return title[this.$route.name]
        }
    },
}
</script>

<style lang="scss" scoped>
#header_wrap {
    // background: $theme-color;
    // background: rgb(76, 169, 225);
    // box-shadow: 1px 2px 2px rgba(118, 215, 237, 0.5);
    // color: white;

    // border-bottom: 0.5px solid rgba(150, 150, 150, 0.5);

    height: 42px;
    padding-bottom: 3px;

    .header-title {
        height: 100%;
        text-align: center;
        align-items: flex-end;
        justify-content: center;
        display: flex;
    }
    .header-hum {
        font-size: 25px;
        cursor: pointer;
        position: absolute;
        top: 3px;
        left: 3px;
    }

    // background-color: $theme-color;
    // color: white;
    //
    // .header_title {
    //     padding-left: 1rem;
    //     color: $menu-text-color;
    //     text-decoration: none;
    //     // font-family: 'Anton', sans-serif;
    //     // font-family: 'Roboto Condensed', sans-serif;
    //     position: relative;
    //     top: 2px;
    //     font-weight: bold;
    //     font-size: 22px;
    // }
}

</style>
