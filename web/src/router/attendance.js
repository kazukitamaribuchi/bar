import { Attendance } from '@/views/index'
import { AttendanceList } from '@/components/index'

const routes = {
    path: '/attendance',
    component: Attendance,
    children: [
        {
            path: '',
            name: 'AttendanceList',
            component: AttendanceList,
            meta: {
                title: 'AttendanceListDao'
            }
        }
    ]
}

export default routes
