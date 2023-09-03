import { createRouter, createWebHistory } from 'vue-router'
import { authGuard } from "@auth0/auth0-vue";


import HomeView from "@/views/HomeView.vue";
import ProtectedView from "@/views/ProtectedView.vue"
import AdminView from "@/views/AdminView.vue"
import PublicView from "@/views/PublicView.vue"
import CallbackView from "@/views/CallbackView.vue"
import ProfileView from "@/views/ProfileView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/protected',
      name: 'protected',
      component: ProtectedView,
      beforeEnter: authGuard,
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminView,
      beforeEnter: authGuard,
    },
    {
      path: '/public',
      name: 'public',
      component: PublicView,
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
    },
    {
      path: "/callback",
      name: "callback",
      component: CallbackView,
    },
    // {
    //   path: "/:catchAll(.*)",
    //   name: "Not Found",
    //   component: NotFoundPage,
    // },
  ]
})

export default router
