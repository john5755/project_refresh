<template>
  <nav  class="navbar navbar-expand">
    <div class="container-fluid">
      <!-- class="collapse navbar-collapse" -->
      <div class="collapse navbar-collapse" id="navbarSupportedContent">        
        <ul class="navbar-nav justify-content-between align-items-center">
          <li class="nav-item d-flex">
            <router-link :to="{ name: 'background' }" class="nav-link active text-light" aria-current="page" >
              <img class="img-link" src="https://dewey.tailorbrands.com/production/brand_version_mockup_image/428/7344073428_5514cc72-cf0e-4a59-9340-c9d4920a0976.png?cb=1653553204" alt="">
            </router-link>
            <router-link :to="{ name: 'searchname', params:{query:''} }" class="nav-link active text-light" aria-current="page" >
              <img class="img-link" src="https://dewey.tailorbrands.com/production/brand_version_mockup_image/968/7344109968_3677157d-725e-4146-87f5-e0f924bbc6ad.png?cb=1653553163" alt="">
            </router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'home' }" class="nav-link active text-light home-btn" aria-current="page" >
              <img class="img-logo" src="https://dewey.tailorbrands.com/production/brand_version_mockup_image/258/7343953258_a05c0df9-9037-4d8e-a845-63430e3f3e28.png?cb=1653549034" alt="">
              <!-- <img class="img-logo" src="https://dewey.tailorbrands.com/production/brand_version_mockup_image/114/7343835114_8aee2df1-8754-4590-97c3-093206dde7ba.png?cb=1653546152" alt=""> -->
            </router-link>
          </li>
          <li v-if="isLoggedIn" class="nav-item">
            <router-link :to="{ name: 'logout' }" class="nav-link active text-light" aria-current="page" >
              <button class="btn btn-rounded btn-outline logout-btn" >Logout</button>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn']),
    },
  }
</script>

<style>
.navbar-nav{
  width: 100%;
  color: rgb(10, 28, 38);
}

.home-btn{
  position: relative;
  right: 1.65em;
}

.logout-btn {
  color: #525252;
  border: 3px solid #525252; /* Green */
  color: #525252;
  height: 33px;
}

/* .navbar{
  position: fixed;
  top: 0;
} */
.img-logo{
  width : 90px;
  height: 66px;
}

.img-link{
  height: 33px;
}
</style>
