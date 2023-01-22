
let btn = document.getElementById("button");

function randomH() {
    return Math.floor(Math.random() * 360);
}
function randomS() {
    return Math.floor(Math.random() * 101);
}

function rgb2hex(rgb) {
    rgb = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    function hex(x) {
        return ("0" + parseInt(x).toString(16)).slice(-2);
    }
    return "#" + hex(rgb[1]) + hex(rgb[2]) + hex(rgb[3]);
}

function generateShades() {
    let randomHue = randomH();
    let randomSat = randomS();
    let s = 110;
    

    
    for (var i = 1; i < 5; i++) {
        let el = document.getElementById("color-box-" + i);
        el.style.display = 'block';
        el.style.backgroundColor = "hsl(" + randomHue + ", " + randomSat + "%, " + (s= s - 20) + "%)";

        el.addEventListener('mouseenter', e =>{
            el.style.cursor = 'pointer';
            el.innerText = rgb2hex(el.style.backgroundColor);
            el.style.fontFamily = 'Poppins, sans-serif';
            el.style.fontSize = '1.5rem';
        })

        el.addEventListener('mouseleave', e =>{
            el.innerText = '';
        })

        el.addEventListener('click', e =>{
            navigator.clipboard.writeText(rgb2hex(el.style.backgroundColor));

        })

    }

}

generateShades();

btn.addEventListener("click", () => {
    generateShades();
});