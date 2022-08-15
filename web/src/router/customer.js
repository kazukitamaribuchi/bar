import { Customer } from '@/views/index'
import { CustomerList, CustomerDetail } from '@/components/index'

const routes = {
    path: '/customer',
    name: 'Home',
    component: Customer,
    children: [
        {
            path: '',
            name: 'CustomerList',
            component: CustomerList,
            meta: {
                title: 'CustomerListDao'
            }
        },
        {
            path: ':id',
            name: 'CustomerDetail',
            component: CustomerDetail,
            meta: {
                title: 'CustomerDetailだよ'
            }
        }
    ]
}

export default routes
