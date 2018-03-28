import Sidebar from './SideBar.vue'

const SidebarStore = {
    showSidebar: false,
    sidebarLinks: [{
            name: 'Dashboard',
            icon: 'ti-panel',
            path: '/admin/overview'
        },
        {
            name: 'Users',
            icon: 'ti-user',
            path: '/admin/users'
        },
        {
            name: 'Companies',
            icon: 'ti-home',
            path: '/admin/companies'
        },
        {
            name: 'Settings',
            icon: 'ti-settings',
            path: '/admin/settings'
        },
        {
            name: 'Login',
            icon: 'ti-settings',
            path: '/admin/login'
        }
    ],
    displaySidebar(value) {
        this.showSidebar = value
    }
}

const SidebarPlugin = {

    install(Vue) {
        Vue.mixin({
            data() {
                return {
                    sidebarStore: SidebarStore
                }
            }
        })

        Object.defineProperty(Vue.prototype, '$sidebar', {
            get() {
                return this.$root.sidebarStore
            }
        })
        Vue.component('side-bar', Sidebar)
    }
}

export default SidebarPlugin