import DashboardLayout from '../components/Dashboard/Layout/DashboardLayout.vue'
// GeneralViews
import NotFound from '../components/GeneralViews/NotFoundPage.vue'

// Admin pages
import Overview from 'src/components/Dashboard/Views/Overview.vue'
import UserProfile from 'src/components/Dashboard/Views/UserProfile.vue'
import Users from 'src/components/Dashboard/Views/Users.vue'
import Companies from 'src/components/Dashboard/Views/Companies.vue'
import Settings from 'src/components/Dashboard/Views/Settings.vue'
import Login from 'src/components/Dashboard/Views/Login.vue'

const routes = [{
        path: '/',
        component: DashboardLayout,
        redirect: '/admin/overview'
    },
    {
        path: '/admin',
        component: DashboardLayout,
        redirect: '/admin/overview',
        children: [{
                path: 'overview',
                name: 'overview',
                component: Overview
            },
            {
                path: 'users',
                name: 'users',
                component: Users
            },
            {
                path: 'companies',
                name: 'companies',
                component: Companies
            },
            {
                path: 'settings',
                name: 'settings',
                component: Settings
            },
            {
                path: 'login',
                name: 'login',
                component: Login
            }
        ]
    },
    { path: '*', component: NotFound }
]

/**
 * Asynchronously load view (Webpack Lazy loading compatible)
 * The specified component must be inside the Views folder
 * @param  {string} name  the filename (basename) of the view to load.
function view(name) {
	 var res= require('../components/Dashboard/Views/' + name + '.vue');
	 return res;
};**/

export default routes