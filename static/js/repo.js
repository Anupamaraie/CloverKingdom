burger = document.querySelector('.burger')
navbar = document.querySelector('.navbar')
Search = document.querySelector('.Search')
nav = document.querySelector('.nav')


burger.addEventListener('click',()=>{
    Search.classList.toggle('v-class');
    nav.classList.toggle('v-class');
    navbar.classList.toggle('h-nav');

})