<template>
    <div id="isauth-wrap">
        isAuth
    </div>
</template>

<script>

export default {
    name: 'IsAuthItem',
    mounted: function () {
        if (this.$store.state.isAuth) {
            this.$router.push({name: 'Home'})
        } else {
            this.$router.push({name: 'Login'})
        }
    }
}
</script>
