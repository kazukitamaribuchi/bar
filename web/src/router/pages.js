import { Home, Login, IsAuth } from '@/views/index'

const routes = [
    {
        path: '/',
        name: 'IsAuth',
        component: IsAuth,
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
    },
    // {
    //     path: '/home',
    //     name: 'Home',
    //     component: Home,
    // },
]

export default routes
