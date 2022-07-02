import { Sales } from '@/views/index'
import { SalesList, SalesDetail } from '@/components/index'

const routes = {
    path: '/sales',
    component: Sales,
    children: [
        {
            path: '',
            name: 'SalesList',
            component: SalesList,
            meta: {
                title: 'SalesListDao'
            }
        },
        {
            path: ':id',
            name: 'SalesDetail',
            component: SalesDetail,
            meta: {
                title: 'SalesDetailだよ'
            }
        }
    ]
}

export default routes
