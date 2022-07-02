import { Cast } from '@/views/index'
import { CastList, CastDetail } from '@/components/index'

const routes = {
    path: '/cast',
    component: Cast,
    children: [
        {
            path: '',
            name: 'CastList',
            component: CastList,
            meta: {
                title: 'CastListDao'
            }
        },
        {
            path: ':id',
            name: 'CastDetail',
            component: CastDetail,
            meta: {
                title: 'CastDetailだよ'
            }
        }
    ]
}

export default routes
