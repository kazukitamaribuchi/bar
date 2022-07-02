<template>
    <span class="basic_checkbox_wrap">
        <label class="typeA-checkbox">
            <input type="checkbox" v-model="localChecked">
            <div class="indicator"></div>
        </label>
    </span>
</template>

<script>
import { Const } from '@/assets/js/const'
import _ from 'lodash'
const Con = new Const()

export default {
    name: 'CheckboxFormItem',
    props: {
        value: {
            type: Boolean,
            required: false,
            default: false,
        },
    },
    created () {

    },
    data: () => ({
        checked: false,
    }),
    computed: {
        localChecked: {
            get: function () {
                return this.value
            },
            set: function (value) {
                this.$emit('input', value)
            },
        },
    }
}

</script>
<style lang="scss" scoped>
    label {
        margin-bottom:15px;
        padding-left:30px;
        display:block;
        font-size:18px;
        cursor:pointer;
        position:relative;
    }

    input {
        position:absolute;
        z-index:-1;
        opacity:0;
    }

    .indicator {
        width:20px;
        height:20px;
        background:#e6e6e6;
        position:absolute;
        top:2px;
        left:0;
        // border-radius:50%;
    }

    label:hover input ~ .indicator,
    label input:focus ~ .indicator{
    	background:#ccc;
    }

    label input:checked ~ .indicator{
    	background:rgba(0,154,219,1);
    }

    label:hover input:not([disabled]):checked ~ .indicator{
    	background:rgba(0,154,219,.7);
    }

    .typeA-radio input:checked ~ .indicator{
    	background: #e87a90;
    }

    .typeA-radio:hover input:not([disabled]):checked ~ .indicator{
    	background:rgba(232,122,144,.7);
    }

    label input:disabled ~ .indicator,
    .typeA-radio input:disabled ~ .indicator{
    	background:#e6e6e6;
    	opacity:0.6;
    	pointer-events:none;
    }

    .indicator::after{
    	content:'';
    	display:none;
    	position:absolute;
    }

    label input:checked ~ .indicator::after{
    	display:block;
    }

    .typeA-checkbox .indicator::after{
    	width:5px;
    	height:8px;
    	border:solid #fff;
    	border-width:0 2px 2px 0;
    	left:8px;
    	top:4px;
    	transform:rotate(45deg);
    }

    .typeA-checkbox input:disabled ~ .indicator::after{
    	border-color:#7b7b7b;
    }

    .typeA-radio .indicator::after{
    	width:6px;
    	height:6px;
    	border-radius:50%;
    	background:#fff;
    	top:7px;
    	left:7px;
    }

    .typeA-radio input:disabled ~ .indicator::after{
    	background:#7b7b7b;
    }
</style>
