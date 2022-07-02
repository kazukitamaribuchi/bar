<template>
    <div>
    </div>
</template>

<script>
import { Const } from '@/assets/js/const'
import _ from 'lodash'
const Con = new Const()

export default {
    name: 'ListViewItem',
    props: {
        viewData: {
            type: Array,
            required: true,
            default: () => ([])
        },
        type: {
            type: Number,
            required: true,
            default: 0,
        },
    },
    data: () => ({
    }),

}

</script>
