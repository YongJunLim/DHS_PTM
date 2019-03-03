var burger = document.querySelector('.burger');
var nav = document.querySelector('#'+burger.dataset.target);

burger.addEventListener('click', function(event) {
    burger.classList.toggle('is-active');
    nav.classList.toggle('is-active');
});