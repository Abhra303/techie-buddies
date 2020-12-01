let front = document.querySelector('.front');
let frontWrapper = document.querySelector('.front-wrapper');
let headerTexts = document.querySelectorAll('.heading-text');

let scrollMover = document.querySelector('#scroll-mover');
let scrollBar = document.querySelector('#scroll-bar');

let status = false;
let height = scrollBar.offsetHeight * 2 ;
let i = 1;
function autoscroll(){
    function f(){
    scrollBar.scrollTop = i;
    if(!status){
        i = i + 140;
        if(i >= height){
        status = true;
        }
    }
    else if(status){
        i = 1;
        status = false;
    }
    }f();
    setInterval(f,2100);

}
autoscroll();

function changeElems(){
    function f(){
    document.querySelectorAll('.heading-text')[0].style.animationName = 'slide';
    document.querySelectorAll('.heading-text')[0].style.animationDuration = '1s';
    document.querySelectorAll('.heading-text')[0].parentNode.insertBefore(document.querySelectorAll('.heading-text')[0],null);
    document.querySelectorAll('.heading-text')[0].style.animationName = 'rise';
    document.querySelectorAll('.heading-text')[0].style.animationDuration = '1s';
    };
    setInterval(f,2100);
}
changeElems();
