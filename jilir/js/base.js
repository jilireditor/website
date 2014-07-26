function main() {
    // Resize the header on scroll
    window.addEventListener('scroll', function(e){
        var distanceY = window.pageYOffset || document.documentElement.scrollTop,
            shrinkOn = 100,
            header = document.querySelector("header");
        if (distanceY > shrinkOn) {
            header.classList.add("smaller");
        } else {
            header.classList.remove("smaller");
        }
    });

    // After page has loaded
    document.addEventListener('DOMContentLoaded', function() {
        [].forEach.call(document.getElementsByClassName('issue-title'), function(el) {
            el.addEventListener('click', function() {
                el.parentNode.classList.toggle('issue-open');
            })
        });

        [].forEach.call(document.getElementsByClassName('masthead-title'), function(el) {
            el.addEventListener('click', function() {
                el.parentNode.classList.toggle('masthead-open');
            })
        })
    })
}

window.onload = main();
