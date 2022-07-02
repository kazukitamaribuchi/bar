import { Account } from '@/views/index'
import {
    AccountHome,
    AccountLogin,
    AccountOrder,
    AccountOrderSelect,
    AccountOrderCheck,
    AccountOrderHistory,
    AccountOrderClose,
    AccountNewVisit,
    AccountBottle,
    AccountCustomer
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
            path: 'bottle',
            name: 'AccountBottle',
            component: AccountBottle,
        },
        {
            path: 'customer',
            name: 'AccountCustomer',
            component: AccountCustomer,
        },
    ]
}

export default routes
