import { Kitchen } from '@/views/index'
import {
    KitchenHome,
    KitchenLogin
} from '@/components/index'

const routes = {
    path: '/kitchen',
    component: Kitchen,
    children: [
        {
            path: '',
            name: 'KitchenHome',
            component: KitchenHome,
        },
        {
            path: 'login',
            name: 'KitchenLogin',
            component: KitchenLogin,
        },
    ]
}

export default routes
