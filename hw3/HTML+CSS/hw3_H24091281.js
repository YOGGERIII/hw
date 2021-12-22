bigbox = document.querySelectorAll('.bigbox');
function fn() {
    setTimeout(function() {
        for (let i of bigbox) {
            i.classList.remove('move3');
            i.classList.add('move1');
        }
    }, 3000);

    setTimeout(function() {
        for (let i of bigbox) {
            i.classList.add('move2');
            i.classList.remove('move1');
        }
    }, 6000);
    
    setTimeout(function() {
        for (let i of bigbox) {
            i.classList.add('move3');
            i.classList.remove('move2');
        }
    }, 9000);
}

window.onload = function() {
    fn();
    setInterval(fn, 9000);
}