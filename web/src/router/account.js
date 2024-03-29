import { Account } from '@/views/index'
import {
    AccountHome,
    AccountOrder,
    AccountOrderSelect,
    AccountOrderCheck,
    AccountOrderHistory,
    AccountOrderClose,
    AccountNewVisit,
    AccountNewCustomer,
    AccountNewBottle,
    AccountBottle,
    AccountCustomer,
    AccountProductDetail,
    AccountLogin
} from '@/components/index'

const routes = {
    path: '/account',
    component: Account,
    children: [
        {
            path: '',
            name: 'AccountHome',
            component: AccountHome,
        },
        {
            path: 'login',
            name: 'AccountLogin',
            component: AccountLogin,
        },
        {
            path: 'order_select',
            name: 'AccountOrderSelect',
            component: AccountOrderSelect,
        },
        {
            path: 'order_check_select',
            name: 'AccountOrderCheckSelect',
            component: AccountOrderSelect,
        },
        {
            path: 'order/:id',
            name: 'AccountOrder',
            component: AccountOrder,
        },
        {
            path: 'order/:id/product/:large/:middle/:small',
            name: 'AccountProductDetail',
            component: AccountProductDetail,
        },
        {
            path: 'order/:id/check',
            name: 'AccountOrderCheck',
            component: AccountOrderCheck,
        },
        {
            path: 'order/:id/history',
            name: 'AccountOrderHistory',
            component: AccountOrderHistory,
        },
        {
            path: 'order/:id/close',
            name: 'AccountOrderClose',
            component: AccountOrderClose,
        },
        {
            path: 'newvisit',
            name: 'AccountNewVisit',
            component: AccountNewVisit,
        },
        {
            path: 'newcustomer',
            name: 'AccountNewCustomer',
            component: AccountNewCustomer,
        },
        {
            path: 'bottle',
            name: 'AccountBottle',
            component: AccountBottle,
        },
        {
            path: 'newbottle',
            name: 'AccountNewBottle',
            component: AccountNewBottle,
        },
        {
            path: 'customer',
            name: 'AccountCustomer',
            component: AccountCustomer,
        },
    ]
}

export default routes
